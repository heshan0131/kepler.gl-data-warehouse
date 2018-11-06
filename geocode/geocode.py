# -*- coding: utf-8 -*-
import json_util
import json
import csv_util
import bcolors
import sys
import urllib2

# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='

# 1. replace api_key with yours
api_key = ''

# 2. input file name
csv_file = 'data/sample.csv'

# 3. output file name (will create if doesn't exist)
out_file = 'data/geolocated.csv'

# 4. column names where the address are stored
keys = ['asylum', 'origin']

key_url = '&key=' + api_key

def geolocate(place):
	request_url = geocode_url + place.replace(' ', '+') + key_url

	d = urllib2.urlopen(request_url)
	result = json.load(d)

	return result['results'][0] if result['status'] == 'OK' else False

def geolocate_rows(rows):
	item_dict = {}
	failed = {}

	for row in rows:
		for key in keys:
			name = row[key]
			if (not name in item_dict) and (not name in failed):
				location = geolocate(name)

				if location:
					item_dict[name] = location['geometry']['location'] # {"lat": -0.789275, "lng": 113.921327}
					print bcolors.OKGREEN + 'geolocation ' + name + ' success' + bcolors.ENDC

				else:
					failed[name] = True
					print bcolors.FAIL + 'geolocation ' + name + ' failed' + bcolors.ENDC

	return {'success': item_dict, 'failed': failed}

def append_to_csv(rows, locations):
	for row in rows:
		for key in keys:
			name = row[key]

			if name in locations:
				loc = locations[name]

				row[key + '_lat'] = loc['lat']
				row[key + '_lng'] = loc['lng']

			else:
				row[key + '_lat'] = ''
				row[key + '_lng'] = ''

	return rows

def dict_to_rows(rows):
	all_rows = []
	header = rows[0].keys()
	header.sort()
	for r in rows:
		all_rows.append(
			map(lambda x : r[x], header)
		)

	print all_rows
	return [header, all_rows]

def main():
	all_rows = csv_util.load_csv(csv_file)
	result = geolocate_rows(all_rows)

	added = append_to_csv(all_rows, result['success'])

	csv_rows = dict_to_rows(added)

	csv_util.save_to_csv(csv_rows[0], csv_rows[1], out_file)

if __name__ == "__main__":
	main()
