from winreg import *
import re
import time
import socket
import json
import requests
import sys

scoresDict = {}

enpoint = "https://pinball.etrash.pro/"

def getName(position):
    key = OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Plus!\Pinball\SpaceCadet', 0, KEY_ALL_ACCESS)
    
    keyName = str(position - 1) + ".Name"

    nameRaw = str(QueryValueEx(key, keyName))

    nameTemp1 = str(re.findall(r'\'(.*?)\'',nameRaw))
    nameTemp2 = nameTemp1.replace("\'", "")
    nameTemp3 = nameTemp2.replace("[", "")
    name = nameTemp3.replace("]", "")

    return name

def getScore(position):
    key = OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Plus!\Pinball\SpaceCadet', 0, KEY_ALL_ACCESS)

    keyName = str(position - 1) + ".Score"

    scoreRaw = str(QueryValueEx(key, keyName))

    scoreTemp1 = str(re.findall(r'\'(.*?)\'',scoreRaw))
    scoreTemp2 = scoreTemp1.replace("\'", "")
    scoreTemp3 = scoreTemp2.replace("[", "")
    score = scoreTemp3.replace("]", "")

    return score

while True:

    #Loop for getting vars
    for x in range(1, 6):
        try:
            scoresDict['name%s' % x] = getName(x)
            scoresDict['score%s' % x] = getScore(x)
        except:
            print ("Cannot find " + ('score%s' % x))


    #print (scoresDict)

    scoresJson = json.dumps(scoresDict).encode('utf-8')


    # SEND NAMES AND SCORES TO SERVER
	
    try:
        r = requests.post(url = enpoint, data = scoresJson) 
        print ("Sent")
    except:
        # Error but don't do anything
        continue
		
    sys.exit(0)