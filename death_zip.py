import zipfile
import os
import shutil

os.mkdir("0")
for i in range(1):
	file = open("0/%i" %i, "w")
	file.write("0" * 1024 * 1024 * 500)

file.close()