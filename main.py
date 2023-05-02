from subprocess import *
import time

Popen('python app.py')
time.sleep(1)
Popen('python botapp.py')

# subprocess.run("python app.py & python botapp.py", shell=True)