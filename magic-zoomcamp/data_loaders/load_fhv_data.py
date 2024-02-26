import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # urls = [
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-01.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-02.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-03.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-04.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-05.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-06.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-07.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-08.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-09.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-10.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-11.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2019-12.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-01.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-02.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-03.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-04.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-05.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-06.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-07.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-08.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-09.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-10.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-11.parquet',
    #     'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-12.parquet',
    #     ]
 
    # # all data
    # dfs = []

    # # get all yellow data
    # for url in urls:
    #     df = pd.read_parquet(url, engine='auto')
    #     dfs.append(df)

    # return pd.concat(dfs, ignore_index = True)
    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_2020-04.parquet'

    return pd.read_parquet(url, engine='auto')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
