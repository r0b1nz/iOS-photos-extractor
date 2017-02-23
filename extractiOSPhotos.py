import os
import shutil
rootdir = 'c:\\Users\\xxxxxxx\\Documents\\BackUps\\TotalBackup'
copyTo = 'c:\\Users\\xxxxxxx\\Documents\\BackUps\\Destination'

counter = 0

for subdir, dirs, files in os.walk(copyTo):
    for file in files:
    	counter = counter + 1
    	try:
    		shutil.copy2(os.path.join(subdir, file), copyTo)
    	except Exception as e:
    		print("Error: " + str(os.path.join(subdir, file)) + "to " + str(copyTo) + str(e))
        # print(os.path.join(subdir, file))

print(str(counter))