# Example:
# curl "http://commute.datashine.org.uk/getflows.php?msoa=E02000120&direction=both&mode=allflows" -H 'Content-Type:application/json'

import json_util
import csv_util
import bcolors
import sys
import json, csv
import requests

# 1. input_file
input_file = 'data/sample.csv'

# 2. output_file
output_file = 'data/output.csv'

# 3. headers
headers = ['d_id', 'o_id', 'allflows']

# 4. get request url from row
def get_request_url(r):
	id = r['msoa11cd']
	return 'http://commute.datashine.org.uk/getflows.php?msoa={0}&direction=both&mode=allflows'.format(id)

r_headers = {'Content-Type': 'application/json'}

def request_data(all_rows):
	rows = []
	count = 1
	total = len(all_rows)
	with open(output_file, 'wb') as csvout:
		spamwriter = csv.writer(csvout, dialect = 'excel')
		spamwriter.writerow(headers)

		for mosa in all_rows:
			print '\r', bcolors.OKBLUE + 'requesting {0}/{1} ...'.format(count, total) + bcolors.ENDC

			url = get_request_url(mosa)

			raw_result = requests.get(url, headers=r_headers)

			if raw_result:
				results = raw_result.json()

				for result in results:
					spamwriter.writerow(map(lambda x: result[x], headers))

			count += 1

	csvout.close()

def main():
	all_rows = csv_util.load_csv(input_file)

	request_data(all_rows)

if __name__ == "__main__":
	main()
