# SparkWork — 2026 evidence note

## Decision

SparkWork is best presented as a **historical local Spark/PySpark learning and engineering lab**, not as evidence of a production or multi-node Spark cluster.

## Original period

Repository commit history observed during the 2026 audit spans:

- first observed commit: `bbbded7` — 2023-06-05;
- last observed commit: `e8bd164372f187010e596cb2fe6846b301e132e1` — 2023-08-05.

The changes in this document, security hardening, and compatibility runtime are part of the 2026 portfolio refresh and must not be backdated into the original project period.

## Evidence index

| Claim | Evidence |
|---|---|
| Local containerized Spark/Jupyter environment | `docker-compose.yml`, `build/Dockerfile`, `start.sh` |
| Curated local service topology | `figs/sparkwork_architecture.png`, cross-checked against Compose, bind mounts, published ports, and notebook `local[1]` evidence |
| PySpark DataFrame use | `work/Spark_DataFrames_Ejemplo.ipynb` |
| Explicit local master | Notebook examples 2 and 3 use `master("local[1]")` |
| Nested-data transforms | `explode`, `explode_outer`, `posexplode`, `posexplode_outer` in the notebook |
| JSON + explicit schema | `StructType`/`StructField` and `spark.read...json(...)` in the notebook |
| Aggregation | `groupBy(...).count()` in the notebook |
| Spark SQL | temp view + `spark.sql(query)` in the notebook |
| Representative output | notebook outputs show NY=2 and PR=7 for the nine-row sample |
| Dataset provenance | historical README plus `docs/DATA_PROVENANCE.md` |
| 2026 runtime validation | `scripts/runtime_validation.py` and external bundle evidence after execution |

## What is not evidenced

The repository does not provide evidence for:

- a multi-node Spark standalone cluster;
- YARN or cloud-managed Spark;
- HDFS or Hive storage;
- RDD-focused workloads;
- Structured Streaming;
- MLlib;
- explicit repartition/coalesce/partitionBy tuning;
- cache/persist;
- broadcast joins;
- executor tuning, AQE analysis, Catalyst analysis, or measured performance improvements.

`groupBy` is a Spark aggregation and can trigger shuffle behavior internally, but the repository does not contain explicit shuffle analysis or tuning. Do not convert that implicit engine behavior into a performance claim.

## Runtime version limitation

The historical Dockerfile used an unpinned `jupyter/all-spark-notebook` base image. Therefore the repository alone does not preserve the exact original Spark, Scala, Java, or base-image build. The notebook metadata records Python 3.11.4, but notebook metadata is not enough to reconstruct the entire historical container.

For the 2026 refresh, the Dockerfile pins a documented Jupyter Docker Stacks compatibility tag. That pin is a reproducibility aid for the refresh; it is **not** represented as the original 2023 image.

## Security/publication refresh

The historical tree tracked `.env` and included a default notebook password while Compose used root/sudo-oriented settings. The 2026 refresh:

- removes `.env` from the current tracked tree without rewriting Git history;
- adds `.env` to `.gitignore` and keeps `.env.example` publishable;
- removes committed password/root/sudo configuration from Compose;
- binds notebook and Spark UI ports to `127.0.0.1`;
- uses Jupyter's generated token;
- keeps orchestrator metadata outside the repository.

If the historical default credential was ever reused anywhere else, rotate that external credential separately. This repository refresh cannot revoke credentials in other systems.

## Builder Journey role

A conservative narrative is:

```text
local data tooling
→ Spark DataFrame / Spark SQL foundations
→ later data platform engineering
→ cloud data architecture
```

SparkWork is useful as historical evidence of learning and applying Spark's higher-level data-processing model. It should not be inflated into a distributed-cluster or production-platform case study.
