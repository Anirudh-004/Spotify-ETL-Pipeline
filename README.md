# Spotify-ETL-Pipeline
ETL pipeline using Spotify API to extract data, transform it, and load it into AWS S3. AWS Lambda handles extraction and transformation, storing raw and processed data in separate S3 buckets. AWS Glue crawler builds a metadata catalog, and the final dataset is loaded into Snowflake for analysis.
