############################# CORRECTION ###############################
import os,subprocess

var=subprocess.run("ls -l", shell=True)
print(var)

pid = os.fork()         # Create child
if pid == 0:
     # Child process
    os.execvp("ls", ["ls","-l"])
else:
    os.wait()