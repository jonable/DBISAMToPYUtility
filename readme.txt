DBISAM Utility.

Utility to pass a SQL string to a DBISAM database (via QueryEventPath) and return either an XML string or python object with the query's results.
Can be imported into a python module or run from the command line. 

/path/to/dbisam_utility SQL STATEMENT

or

from dbisam_utility import query, parse_xml

def run(query_string):
	xml = query(query_string, utility_path="path/to/quereventpath_util.exe")
	rows_as_dict = list(parse_xml(xml))	
	return rows_as_dict



This program depends on the QueryEventPath program installed on the same machine as the database. See QueryEventPath for more information.