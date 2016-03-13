"""
A better way to manage google chrome bookmarks or any 
other bookmarks file that is json and has the same 
fields.

1) export bookmarks to the parent (pybookmarks) directory
2) 



"""
from pprint import pprint
import json

def load(bookmark_file):
	with open(bookmark_file, 'r') as fin:
		block = fin.read()
		return json.loads(block)

def get_object_by_id(bkjs,id):
	for x in bkjs:
		if x['id'] == id:
			return x	


def test_print(s):
	pprint(s)


def main():
	k = load('bookmarks.json')
	test_print(k[5])
	get_object_by_id(k, '400')

if __name__ == '__main__':
	main()
