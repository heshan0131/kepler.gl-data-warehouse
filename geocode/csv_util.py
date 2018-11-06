import csv
import bcolors

def save_to_csv(header, rows, filename):
	print bcolors.OKBLUE + 'save to {0}'.format(filename) + bcolors.ENDC

	with open(filename, 'wb') as csvout:
		spamwriter = csv.writer(csvout, dialect = 'excel')
		spamwriter.writerow(header)
		for r in rows:
			spamwriter.writerow(r)
	csvout.close()


def load_csv(path_to_file):
	rows = []
	print bcolors.OKGREEN + 'loading {0} ...'.format(path_to_file) + bcolors.ENDC

	with open(path_to_file, 'rb') as csvfile:
		csvreader = csv.DictReader(csvfile, dialect = 'excel')
		for row in csvreader:
			rows.append(row)
	return rows
	csvfile.close()
