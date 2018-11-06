import json
import bcolors

def load_json(path_to_file):
  with open(path_to_file, 'rb') as json_file:
    print bcolors.OKGREEN + 'loading {0} ...'.format(path_to_file) + bcolors.ENDC
    json_data = json.load(json_file, encoding="latin-1")

  json_file.close()
  return json_data

def save_to_json(json_data, filename):
  with open(filename, 'w') as outfile:
    print bcolors.OKGREEN + 'json dump' + bcolors.ENDC
    json.dump(json_data, outfile)
  outfile.close()
