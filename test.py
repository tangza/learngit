import os

import string
def listDirectory(folder):
	for fname in os.listdir(folder):
		print(fname)

# listDirectory('.')

def test():
	s = '中文'
	print(s.encode('utf-8'))
	print(s)
	s1 = u'统一编码'
	print(s1)
test()