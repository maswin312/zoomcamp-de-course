if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print(f"processing : Rows with 0 Passanger :{data['passenger_count'].isin([0]).sum()}")
    print(f"processing : Rows with 0 Distance :{data['trip_distance'].isin([0]).sum()}")
    
    data_clean = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    data_clean["lpep_pickup_date"] = data_clean["lpep_pickup_datetime"].dt.date
    # Specify your transformation logic here
    name_mapping = {"VendorID" : "vendor_id",
                    "RateCodeID" : "rate_code_id",
                    "PULocationID" : "pu_location_id",
                    "DOLocationID" : "do_location_id",
                    }
    data_clean = data_clean.rename(columns=name_mapping)
    return data_clean


@test
def test_output(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum()==0, "They're ride with 0 passenger"
    assert output['trip_distance'].isin([0]).sum()==0, "They're ride with 0 distance"
    assert "vendor_id" in output.columns, "No vendor_id as column name"