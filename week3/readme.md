create an external table from GCS
```
create or replace external table `zoomcamp-de-course-413206.nyc_taxi_data.external_green_taxi_data_2022`
options (format = 'parquet',
uris = ['gs://loading-data-zoomcamp/nyc_green_data_2022/*.parquet']);
```

create non partitioned table from external table
```
create or replace table `zoomcamp-de-course-413206.nyc_taxi_data.non_partitioned_green_taxi_data_2022`
as 
(select * from `zoomcamp-de-course-413206.nyc_taxi_data.external_green_taxi_data_2022`)
```

```
select count(distinct PULocationID) from `nyc_taxi_data.non_partitioned_green_taxi_data_2022`
```