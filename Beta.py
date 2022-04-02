import os, platform
os.system('git pull')
try:
    import requests
except:
    os.system('python3 -m pip install requests')
    os.system('python3 -m pip install bs4')
    os.system('python3 -m pip install futures')
    os.system('python3 -m pip install machine')
    os.system('python3 -m pip install mechanize')


import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from AFCT import bnsbuy
    bnsbuy()
elif bit == '32bit':
    from AFC import bnsbuy
    bnsbuy()
