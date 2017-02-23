import os
import shutil
rootdir = 'c:\\Users\\rgautam\\Documents\\BackUps\\TotalBackup'
copyTo = 'c:\\Users\\rgautam\\Documents\\BackUps\\Destination'

counter = 0
check = False
inIt = 0

for subdir, dirs, files in os.walk(copyTo):
    for dir in dirs:
    	print(os.path.join(subdir, file))
    	# try:
    	# 	shutil.copy2(os.path.join(subdir, file), copyTo)
    	# except Exception as e:
    	# 	print("Error: " + str(os.path.join(subdir, file)) + "to " + str(copyTo) + str(e))
        # print(os.path.join(subdir, file))

print(str(inIt))