import platform
import fnmatch
import os
import string
import sys

allDistros = ['linuxmint','ubuntu','debian','opensuse','arch','pclinuxos',
    'centos','mageia','slackware','crunchbang']

def isLinux():
  if platform.system() == 'Linux':
    return True
  else:
    return False

def getOS():
  return string.lower(platform.system())

def getBits():
  if platform.system().find('64') == -1:
    return 32
  else:
    return 64

def getDistros():
  distros = []
  for file in os.listdir('/etc/'):
    if file.find('release') != -1:
      with open('/etc/'+file,'r') as f:
        data = f.read()
        data = string.lower(data)
        data = data.replace("\\s+","")
        for distro in allDistros:
          if data.find(distro) != -1:
            distros.append(distro)
  return distros

