# Dataset provenance

## `work/data/zipcodesUSDummy.json`

SparkWork contains a small nine-row JSON sample with these fields:

- `zip_code`
- `latitude`
- `longitude`
- `city`
- `state`
- `county`

The historical README attributes the sample to the public `millbj92/US-Zip-Codes-JSON` repository. During the 2026 refresh, that upstream repository was verified to publish an MIT license and to describe the data as a list of US ZIP codes with the same location fields.

Source repository:

```text
https://github.com/millbj92/US-Zip-Codes-JSON
```

The local sample is retained because it is small, non-personal geographic reference data used solely to demonstrate JSON ingestion, explicit schema definition, DataFrame aggregation, and Spark SQL. Attribution must remain with the sample/documentation.

No claim is made here about a separate governmental source, data-collection method, or provenance chain beyond what the linked upstream repository itself documents.
