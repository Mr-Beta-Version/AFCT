import os, platform
os.system('git pull')
try:
    import requests
except:
    os.system('pip install requests')
    os.system('pip install bs4')
    os.system('pip install futures')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from AFCT import bnsbuy
    bnsbuy()
elif bit == '32bit':
    from AFC import bnsbuy
    bnsbuy()
