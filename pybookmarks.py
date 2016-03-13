"""
A better way to manage google chrome bookmarks or any 
other bookmarks file that is json and has the same 
fields.

1) export bookmarks to the parent (pybookmarks) directory
2) 



"""
from pprint import pprint
import json
import Bookmark


def load(bookmark_file):
   with open(bookmark_file, 'r') as fin:
      block = fin.read()
      return json.loads(block)

def main():
   k = load('../bookmarks.json')   	
   test = k[5]
   pprint(test)
   BK = Bookmark.Bookmark(test['dateAdded'], test['index'], test['id'],test['parentId'],test['title'],test['url'])
   print(BK.get_url())

if __name__ == '__main__':
	main()
