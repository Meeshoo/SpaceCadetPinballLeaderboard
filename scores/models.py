from django.db import models
import json

class scores(models.Model):
    playerid = models.IntegerField(default=None, blank=True, null=True)
    name = models.TextField(max_length=30)
    score = models.IntegerField()

    def getPlayerID(nameToGet):
        
        # Get objects with name and put into list
        scoresForPlayer = list(scores.objects.filter(name = nameToGet))

        # take one (first I guess)
        item = scoresForPlayer[0]

        # Get ID associated with name
        playerID = item.playerid

        #return ID
        return playerID

    # NOT FINISHED YET
    def setPlayerID(playerName):

        if playerName == "Mitch":
    
            scoresForPlayer = scores.objects.filter(name = "Mitch")

            for s in scoresForPlayer:
                s.playerid = 1
                s.save()

        if playerName == "Reggo":
    
            scoresForPlayer = scores.objects.filter(name = "Reggo")

            for s in scoresForPlayer:
                s.playerid = 2
                s.save()
        
        if playerName == "Defaultsound":
        
            scoresForPlayer = scores.objects.filter(name = "Defaultsound")

            for s in scoresForPlayer:
                s.playerid = 3
                s.save()

    def submitData(postData):

        def validScore(score):
            if score == -999:
                return False
            elif score > 9999999:
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

        retrievedScores = []
        retrievedNames = []

        retreivedObjects = scores.objects.all()
        objectList = list(retreivedObjects)

        for o in objectList:
            s = o.score
            n = o.name
            retrievedScores.append(s)

        postData_dict = json.loads(postData.decode('utf-8'))
        dataList = list(postData_dict.values())

        #Save 1st score to DB
        for x in range(0,10,2):
            scoreToCheck = int(dataList[int(x)+1])
            nameToCheck = dataList[int(x)]
            if validScore(scoreToCheck) and validName(nameToCheck) and noDuplicate(nameToCheck, scoreToCheck, objectList):
                scoreEntry = scores(name=dataList[x], score=dataList[x+1])
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
            print ("ERROR BRO: NO SCORES IN DB")
            return "Noscores"