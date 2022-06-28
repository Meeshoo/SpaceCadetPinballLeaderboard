import json
import datetime

from django.db import models
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.models import Model


class scores(Model):
    class Meta:
        table_name = "SpaceCadetPinballLeaderboard"
        region = "eu-west-1"
    name = UnicodeAttribute(hash_key=True)
    score = NumberAttribute(range_key=True)
    date = UnicodeAttribute()

    def submitData(postData):

        def validScore(score):
            if score == -999:
                return False
            elif score > 999999999:
                return False
            else:
                return True

        def noDuplicate(newEntryName, newEntryScore, entries):
            for e in entries:
                if newEntryName == e.name and newEntryScore == e.score:
                    return False
            else:
                return True

        def validName(name):
            if '<' not in name:
                return True
            else:
                return False

        retreivedObjects = scores.scan()
        objectList = list(retreivedObjects)

        postData_dict = json.loads(postData.decode('utf-8'))
        dataList = list(postData_dict.values())

        date = str(datetime.date.today()) + " " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute)

        #Save 1st score to DB
        for x in range(0,10,2):
            scoreToCheck = int(dataList[int(x)+1])
            nameToCheck = dataList[int(x)]
            if validScore(scoreToCheck) and validName(nameToCheck) and noDuplicate(nameToCheck, scoreToCheck, objectList):
                print(dataList[x], dataList[x+1], date)
                scoreEntry = scores(name=dataList[x], score=dataList[x+1], date=date)
                scoreEntry.save()

    def retrieveData():

        retrievedNames = []
        retrievedScores = []

        def scoreSort(obj):
            return obj.score

        # Get all DB objects and sort by score
        retreivedObjects = scores.scan()
        objectList = list(retreivedObjects)
        objectList.sort(reverse = True, key = scoreSort)

        # Put scores into list
        for o in objectList:
            n = o.name
            s = f'{o.score:,}'
            retrievedNames.append(n)
            retrievedScores.append(s)
            
        # Return top 10
        if len(retrievedNames) > 1:
            name1 = retrievedNames[0]
            score1 = retrievedScores[0]
            name2 = retrievedNames[1]
            score2 = retrievedScores[1]
            name3 = retrievedNames[2]
            score3 = retrievedScores[2]
            name4 = retrievedNames[3]
            score4 =retrievedScores[3]
            name5 = retrievedNames[4]
            score5 = retrievedScores[4]

            name6 = retrievedNames[5]
            score6 = retrievedScores[5]
            name7 = retrievedNames[6]
            score7 = retrievedScores[6]
            name8 = retrievedNames[7]
            score8 = retrievedScores[7]
            name9 = retrievedNames[8]
            score9 =retrievedScores[8]
            name10 = retrievedNames[9]
            score10 = retrievedScores[9]
			

            return name1,score1,name2,score2,name3,score3,name4,score4,name5,score5,name6,score6,name7,score7,name8,score8,name9,score9,name10,score10

        else:
            return "Not enough scores in DB"

