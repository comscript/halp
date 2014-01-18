import platform
import fnmatch
import os

distros = ['linux','ubuntu','debian','opensuse','arch','pclinuxos',
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

def getDistro():
  #lsb-release distros
  try:
    for file in os.listdir('/etc/'):
      if fnmatch.fnmatch(file, '*-release'):
        with open(file,'r') as f:
          data = f.read()
          data = string.lower(distroData)
          data = data.replaceAll("\\s+","")
          for distro in distros: 
            if data.find(distro) != -1:
              return distro
  return None


