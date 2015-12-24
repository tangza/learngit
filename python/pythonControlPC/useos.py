# encoding: UTF-8

import os
import subprocess

def testOS():
	os.system('ping www.baidu.com')

def testCmdFromFile():
	f = open('cmd.txt', 'r')
	cmd = f.readline()
	os.system(cmd)
	f.close()

def testSubprocess():
	p = subprocess.Popen('dir', shell=True)
	p.wait()

# testOS()
# testCmdFromFile()
testSubprocess()