#!/usr/bin/env python3
"""Representative local Spark validation for the 2026 portfolio refresh.

This does not assert that the compatibility image equals the original 2023 runtime.
It validates that the repository's representative DataFrame + Spark SQL behavior still
runs in the pinned refresh environment.
"""
from __future__ import annotations

import json
import platform
import sys
from pathlib import Path

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType, IntegerType, StringType, StructField, StructType

DATA = Path('/home/jovyan/work/data/zipcodesUSDummy.json')
EXPECTED = {'NY': 2, 'PR': 7}


def main() -> int:
    if not DATA.is_file():
        raise SystemExit(f'ERROR: missing dataset: {DATA}')

    raw = json.loads(DATA.read_text(encoding='utf-8'))
    assert len(raw) == 9, f'expected 9 JSON objects, got {len(raw)}'

    schema = StructType([
        StructField('zip_code', IntegerType(), False),
        StructField('latitude', DoubleType(), False),
        StructField('longitude', DoubleType(), False),
        StructField('city', StringType(), False),
        StructField('state', StringType(), False),
        StructField('county', StringType(), False),
    ])

    spark = (
        SparkSession.builder
        .master('local[1]')
        .appName('SparkWork2026Validation')
        .getOrCreate()
    )
    try:
        print(f'python={platform.python_version()}')
        print(f'pyspark={pyspark.__version__}')
        print(f'spark={spark.version}')
        print(f'master={spark.sparkContext.master}')
        print(f'default_parallelism={spark.sparkContext.defaultParallelism}')

        df = (
            spark.read
            .option('multiline', 'true')
            .schema(schema)
            .json(str(DATA))
        )
        row_count = df.count()
        assert row_count == 9, f'expected 9 Spark rows, got {row_count}'

        counts_df = {row['state']: row['count'] for row in df.groupBy('state').count().collect()}
        assert counts_df == EXPECTED, f'DataFrame counts mismatch: {counts_df!r}'

        df.createOrReplaceTempView('tb_codigo_zip')
        sql_rows = spark.sql(
            'SELECT state, COUNT(0) AS count FROM tb_codigo_zip GROUP BY state'
        ).collect()
        counts_sql = {row['state']: row['count'] for row in sql_rows}
        assert counts_sql == EXPECTED, f'Spark SQL counts mismatch: {counts_sql!r}'

        print(f'json_rows={row_count}')
        print(f'dataframe_counts={counts_df}')
        print(f'spark_sql_counts={counts_sql}')
        print('SPARKWORK_RUNTIME_VALIDATION=PASS')
        return 0
    finally:
        spark.stop()


if __name__ == '__main__':
    raise SystemExit(main())
