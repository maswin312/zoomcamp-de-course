create an external table from GCS

```sql
create or replace external table `zoomcamp-de-course-413206.nyc_taxi_data.external_green_taxi_data_2022`
options (format = 'parquet',
uris = ['gs://loading-data-zoomcamp/nyc_green_data_2022/*.parquet']);
```

create non partitioned table from external table
```sql
create or replace table `zoomcamp-de-course-413206.nyc_taxi_data.non_partitioned_green_taxi_data_2022`
as 
(select * from `zoomcamp-de-course-413206.nyc_taxi_data.external_green_taxi_data_2022`)
```

```sql
-- non partitioned table estimated 6.41 MB data
select count(distinct PULocationID) from `nyc_taxi_data.non_partitioned_green_taxi_data_2022`

-- external table estimated 0 B data
select count(distinct PULocationID) from `nyc_taxi_data.external_green_taxi_data_2022`

```

Create partitioned and clustered table from external table
```sql
create or replace table `zoomcamp-de-course-413206.nyc_taxi_data.partitioned_green_taxi_data_2022`
partition by date(lpep_pickup_datetime)
cluster by PULocationID
as 
(select * from `zoomcamp-de-course-413206.nyc_taxi_data.external_green_taxi_data_2022`)
```

compare estimated bytes processed between non-partitioned and partitioned table
```sql
-- non partitioned table estimated 12.82 MB data
select count(distinct PULocationID) from `nyc_taxi_data.non_partitioned_green_taxi_data_2022`
where date(lpep_pickup_datetime) between date '2022-06-01' and date '2022-06-30'

-- partitioned table estimated 1.12 MB data
select count(distinct PULocationID) from `nyc_taxi_data.partitioned_green_taxi_data_2022`
where date(lpep_pickup_datetime) between date '2022-06-01' and date '2022-06-30'

```