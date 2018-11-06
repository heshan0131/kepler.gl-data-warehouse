# kepler.gl data warehouse

Here are some useful Python scripts I used to request, process, prepare data for visualizing them in kepler.gl

## Env
runs in python 2.7

## List of Scripts
### 1. geocode

Run Google Geocode API to get latitude / longitude from an address

#### Usage
1. In terminal
```sh
cd geocode
```

2. sign up on google maps api and get an api key. You can get an api key for free with limited rates.

3. Create a csv file with a list of places in the data folder.

4. Open `geocode.py`
- Edit `api_key` with your google api key
- Edit `csv_file` with path to the input csv file
- Edit `out_file` with path to the output file, which will be created if doesn't exist.
- Edit `keys` with a list column names that the address are stored, for each row you can have multiple address for geocoding. If the name of the column is `place` The result will be added to the row as `place_lat` and `place_lng` column.

5. run
```sh
python geocode.py
```

### 2. join_geojson_w_csv
Join a geojson file where geometries are stored with a csv file where more metrics are stored. The output is a new geojson file with metrics added to its feature properties

#### Usage
1. In terminal
```sh
cd join_geojson_w_csv
```

2. Put geojson and csv file in data folder

3. Open `join_geojson_w_csv.py`
- Edit `csv_file` with path to the input csv file.
- Edit `geojson_in` with path to the input geojson.
- Edit `geojson_out` with path to the output geojson, which will be created if doesn't exist.
- Edit `items`with a list of columns to be added to the geojson feature properties
- Edit `properties_keep` with a list of properties to keep in the geojson feature proerpties. When list is empty, all will be copy over.
- Edit `json_key()` function, to return the key from properties to match items in csv
- Edit `csv_key()` function, to return the key from each row to match items in geojson

4. run script inside directory
```sh
python join_geojson_w_csv.py
```

### 3.http_request
Send simple http request from an array of input. Put response in a csv file. Expect response to be an array of object.

#### Usage
1. In terminal
```sh
cd http_request
```

2. activate your [virtualenv](https://virtualenv.pypa.io/en/latest/)
```sh
virtualenv ENV
source /path/to/ENV/bin/activate
```

3. Open `http_request.py`
- Edit `input_file` with path to the input csv.
- Edit `output_file` with path to the output csv, which will be created if doesn't exist.
- Edit `headers` with a list of keys to be added to the output csv. Each key should be contained in the json response
- Edit `get_request_url()` to return the request url given each row.

4. run script inside directory
```sh
python http_request.py
```
