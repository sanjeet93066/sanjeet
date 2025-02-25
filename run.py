import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x prs')
    os.system('./prs')
elif bit == '32bit':
    os.system('chmod +x prs32')
    os.system('./prs32')
else:
    print('device not supported')
