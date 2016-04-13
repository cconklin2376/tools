import hashlib   # HashCalc

import string, random  # id_generator




# this can also be used by passing a string and removing all of the file stuff
def HashCalc(fname):
   try:
      f = file(rootPath + objectPath + fname,'rb')
      Data =f.read()
      MD5 = hashlib.md5(Data).hexdigest()
   except:
      errFile = open((rootPath + errFileName), 'w')
      #print 'Failed To Open File ' + (rootPath + objectPath + fname)
      errFile.write('MD5 error: Failed To Open File ' + (rootPath + objectPath + fname))
      errFile.close()
      sys.exit()
   f.close()
   return MD5


def id_generator(size = 4, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for x in range(size))



