import subprocess
import os




umount = subprocess.Popen(['sudo', 'umount', '-l', f"{temp}/root.x86_64"], stdout=subprocess.STDOUT, stderr=subprocess.STDOUT)
umount.wait()

remove = subprocess.Popen(['sudo', 'rm', '-rf', f"{temp}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
remove.wait()