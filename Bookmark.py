
"""
search_tools.py

The data format of the bookmarks 
exported file is as follows:

{u'dateAdded': u'2014-02-17T18:05:25.670Z',
 u'id': u'1750',
 u'index': 3,
 u'parentId': u'337',
 u'title': u'',
 u'url': u'http://www.amazon.com/'}

"""
class Bookmark:
   'Storage class for bookmark entries'
   bkmkCount = 0

   def __init__(self, dateadd, id, index, parent, title, url):
      self.id = id
      self.dateadd = dateadd
      self.index = index
      self.parent = parent
      self.title = title
      self.url = url
      Bookmark.bkmkCount += 1
   
   def displayCount(self):
     print "Total Bookmarks  %d" % Bookmark.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

   def get_entry_date(self, fmt='Y-m-d'):
      ''' Return the date string of the entry in
	    the specified format. If format not found
	    then return the full dateAdded form entry'''
      if fmt == 'Y-m-d':
         return self.dateadd[:13]
      elif fmt == 'Y/m/d':
         return self.dateadd[:13].replace('-','/')
      else:
         return self.dateadd

   def get_url(self):
      return self.url



