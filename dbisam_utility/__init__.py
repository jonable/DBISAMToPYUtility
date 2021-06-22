import sys, os
from dbisam_utility import query, parse_xml


def get_utility_path():
	return os.path.abspath('./bin/dbisam_utility.exe')

def main(query_string):
	xml = query(query_string, utility_path=get_utility_path())
	rows_as_dict = list(parse_xml(xml))	
	return rows_as_dict


if __name__ == '__main__':
	if len(sys.argv) > 1 and os.path.is_file(sys.args[1]):		
		query_string = open(sys.args[1], 'r').read()
		parsed = main(query_string, utility_path=get_utility_path())