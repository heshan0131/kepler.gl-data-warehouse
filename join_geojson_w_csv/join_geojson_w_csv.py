# -*- coding: utf-8 -*-
import json_util
import csv_util
import bcolors
import sys

# Join geojson and csv

# 1. csv input
csv_file = 'data/sample.csv'

# 2. geojson input
geojson_in = 'data/sample_geojson.json'
geojson_out = 'data/sample_geojson_output.json'

# 3. columns to add from csv
items = ['Poverty Estimate, All Ages', 'Poverty Percent, All Ages', 'Median Household Income']

# 4. items to keep from original geojson feature properties, when empty keep everything
properties_keep = []

# 5. get key from geojson properties to match
def json_key(f):
	return f['properties']['STATE'] + '-' + f['properties']['COUNTY']

# 6. get key from csv to match
def csv_key(r):
	return r['State FIPS Code'] + '-' + r['County FIPS Code']

def append_to_json(geojson, item_dict):
	for f in geojson['features']:
		key = json_key(f)

		if not key in item_dict:
			print bcolors.FAIL + 'cannot find item {0}'.format(key) + bcolors.ENDC
			continue

		for item in items:
			f['properties'][item] = item_dict[key][item]

	return geojson

def main():
	geojson = json_util.load_json(geojson_in)
	item_meta = csv_util.load_csv(csv_file)

	item_dict = {}
	for c in item_meta:
		key = csv_key(c)
		item_dict[key] = c

	matched = append_to_json(geojson, item_dict)

	json_util.save_to_json(matched, geojson_out)

if __name__ == "__main__":

	main()
