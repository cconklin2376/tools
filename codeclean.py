''' 
codeclean.py


possible feature list:
- line numbers that contain comments
- TODO, todo, etc finding line numbers
- hard coded parameters exist error - checks to see if commented parm lines
- total line count with src lines and blank lines
- reports multi blank line areas 
- even mutiples for tabs or space indentions

- input file and creates its own copy for output


created 9-23-14
cconklin


$ python codeclean.py audit /path/to/file

or 

$ python codeclean.py clean /path/to/file


'''

import os
import sys
import difflib

# these can be edited to custom proofing
TAB_SIZE = 4
MAX_BLANK_LNS = 3
CLEANSE_TEXT = ['TODO:', 'todo:', '--p_']
#CLEANSE_TEXT = ['TODO:', 'todo:', '-- p_', '--p_']
SOLOS = ['EXCEPTION', 'UTL_FILE.FCLOSE_ALL']
usage = '''

codeclean.py usage:

Audit mode:
$ python codeclean.py audit /path/to/file
(outputs suggested changes list)

or 

Clean mode
$ python codeclean.py clean /path/to/file
(creates a copy if original with modification)

'''


def Proof(content):
	lncnt = 0
	warn_cnt = 0
	tot_blank_ln_cnt = 0
	src_ln_cnt = 0
	comm_ln_cnt = 0
	curr_blank_ln = 0
	for line in content:
		lncnt += 1
		space_cnt = 0

		# check proper tabs and indentation
		space_cnt = (len(line) - len(line.lstrip(' ')))
		if space_cnt % TAB_SIZE:
			print("\tPadding Indentation line " + str(lncnt) + " improper indent " + str(space_cnt) + " spaces")
			#print(">> " + line)
			warn_cnt +=1
			#break


		tokens = line.split()

		# count blank lines, comment lines and src lines
		if len(tokens) == 0:
			tot_blank_ln_cnt += 1
			curr_blank_ln += 1
			if curr_blank_ln > MAX_BLANK_LNS:
				print("\tWARNING: max blank lines exceeded at line " + str(lncnt))
				warn_cnt += 1
				curr_blank_ln = 0
		elif tokens[0] == '--':
			comm_ln_cnt += 1
		else: 
			src_ln_cnt += 1


		# check for single tokens
		if len(tokens) == 1 and tokens[0] not in SOLOS:
			print("\tStray token '" + line.strip() + "' on line " + str(lncnt))
			#print("\t" + str(lncnt) + ": " + line)
			warn_cnt +=1
		# check for personal syntax gotchas
		for t in tokens:
			if(difflib.get_close_matches(t, CLEANSE_TEXT)):
				print("\tWarning possible flaw found '" + t + "' on line " + str(lncnt))
				warn_cnt +=1

	print("\n\nParsing complete. Lines: " + str(lncnt) + ". Warnings: " + str(warn_cnt) + ".")
	print("src lines: " + str(src_ln_cnt) + "    commented lines: " + str(comm_ln_cnt) + "   blank lines: " + str(tot_blank_ln_cnt) + "\n\n")

def CleanFile(src):
	# check that dir is writable for clone or exit
	'''
	try:
		filepath = src + '.mod'
		filehandle = open( filepath, 'w' )
	except IOError:
		sys.exit( 'Unable to write to file ' + filepath )

	filehandle.write("ok")
	'''
	pass


def AuditFile(src):
	if(os.path.isfile(src)):
		print("\n\n\nProcessing file '" + src + "'\n")
		
		with open(src, 'r') as infile:
			file_content = infile.readlines()
			Proof(file_content)
			#print(content)
	else:
		print("\n\n\nError(111): File '" + src + "' does not exist. " + usage)
		sys.exit()


def main():
	if len(sys.argv) != 3:
		print("Error: " + usage)
		sys.exit()
	else:
		mode = sys.argv[1]
		code_file_name = sys.argv[2]

		if(mode == 'clean'):
			print('cleaning ' + code_file_name)
			CleanFile(code_file_name)
		elif(mode == 'audit'):
			print('auditing ' + code_file_name)
			AuditFile(code_file_name)
		else:
			print("\n\n\nError(104): mode '" + mode + "' not available. " + usage)
			sys.exit()



if __name__ == '__main__':
	main()












