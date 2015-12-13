import os

def listDirectory(folder):
	for fname in os.listdir(folder):
		print(fname)

listDirectory('.')