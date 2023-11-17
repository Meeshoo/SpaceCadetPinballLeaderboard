import json
import datetime
from django.db import models

class scores(models.Model):
    name = models.TextField(max_length=30)
    score = models.IntegerField()
    date = models.TextField(max_length=50)

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
        retreivedObjects = scores.objects.all()
        objectList = list(retreivedObjects)
        objectList.sort(reverse = True, key = scoreSort)

        objectList = objectList[:10]

        count = 1

        for entry in objectList:
            entry.score = "{:,}".format(entry.score)
            entry.rank = count
            count += 1

        return objectList
