import re
import string

import environment as env


def getBrowsers(password):
  p = env.newProcess(['sudo','-S','update-alternatives','--config','x-www-browser'])
  data = p.communicate(password+"\n\n")
  data = data[0][:data[0].find(":")]#TODO: Figure out why update-alternatives prints twice sometimes.
  strBrowsers = re.findall(R"(\*?\s?\d{1}[\s]+/[a-zA-Z0-9\.\-/]*)",data)
  browsers = []
  #print strBrowsers
  for ind,strBrowser in enumerate(strBrowsers):
    default = True if (strBrowser.find("*") != -1) else False
    strBrowser = strBrowser + " "
    browser = re.findall(R"(/{1}[a-zA-Z0-9\-\.]+\s{1})",strBrowser)
    browser = browser[0]
    browser = browser.lstrip("/").rstrip(None)
    browsers.append((ind,browser,default))

  return browsers


def setDefault(browser,password):
  browsers = getBrowsers(password)
  index = -1
  for b in browsers:
    if browser == b[1]:
      index = b[0]
  
  if index != -1:
    p = env.newProcess(['sudo','-S','update-alternatives','--config','x-www-browser'])
    p.communicate(password+"\n"+str(index)+"\n")
    return True
  else:
    return False
 

 def installBrowser(browser,password):
   if browser == 'chromium-browser'
   or browser == 'firefox'
   or browser == 'opera':
     env.install(browser,password)
     return True
   else:
     return False

