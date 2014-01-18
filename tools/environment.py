import platform
import fnmatch
import os
import string
import sys
import subprocess

allDistros = {
'linuxmint':'apt',
'ubuntu':'apt',
'debian':'apt',
'opensuse':'zypper',
'arch':'pacman',
'pclinuxos':'apt',
'centos':'yum',
'mageia':'urpmi',
'redhat':'yum',
'fedora':'yum',
'slackware':'pkgtools',
'crunchbang':'apt'
}

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
        for distro in allDistros.keys():
          if data.find(distro) != -1:
            distros.append(distro)
  return list(set(distros))

def getPMSCandidates():
  managers = []
  distros = getDistros()
  for distro in distros:
    managers.append(allDistros[distro])
  return list(set(managers))

def isInstalled(package):
  for manager in getPMSCandidates():
    if manager == 'apt':
      p = subprocess.Popen(
          ["sudo","dpkg","-s",package],
          stdin = subprocess.PIPE,
          stdout = subprocess.PIPE,
          stderr = subprocess.PIPE
          )
      while p:
        line = p.stdout.readline()
        if not line:
          break
        if line.find("Package: ") != -1:
          return True
    elif manager == 'yum' or manager == 'zypper' or manager == 'urpmi':
      p = subprocess.Popen(
          ["sudo","rpm","-q", package],
          stdin = subprocess.PIPE,
          stdout = subprocess.PIPE,
          stderr= subprocess.PIPE
          )
      installed = True
      while p:
        line = p.stdout.readline()
        if not line:
          break
        if line.find('not installed') != -1:
          installed = False
      if installed:
        return True

  return False



