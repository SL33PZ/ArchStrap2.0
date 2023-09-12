import os
import subprocess


app = subprocess.Popen(['python', 'lib/app.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app.wait()

file1 = open('lib/functions/umount.py', 'r')
file2 = open('lib/functions/umount_temp.py', 'w')


for line in file1.readlines():
    if not (line.startswith('temp=')):
            file2.write(line)
            
file1.close()
file2.close()

os.remove('lib/functions/umount.py')
os.rename('lib/functions/umount_temp.py', 'lib/functions/umount.py')

unmount = subprocess.Popen(['python', 'lib/functions/umount.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
unmount.wait()