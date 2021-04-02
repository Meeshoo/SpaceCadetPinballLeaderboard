from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import scores
from django.views.decorators.csrf import csrf_exempt

dataSent = False
name1 = "Not"
score1 = 0
name2 = "enough"
score2 = 0
name3 = "scores"
score3 = 0
name4 = "in"
score4 = 0
name5 = "database"
score5 = 0
name6 = "please"
score6 = 0
name7 = "submit"
score7 = 0
name8 = "10"
score8 = 0
name9 = "or more"
score9 = 0
name10 = "scores"
score10 = 0


@csrf_exempt
def index(request):

    global dataSent
    global name1,score1,name2,score2,name3,score3,name4,score4,name5,score5,name6,score6,name7,score7,name8,score8,name9,score9,name10,score10

    if request.method == 'GET':

        if scores.retrieveData() != "Not enough scores in DB":
            name1,score1,name2,score2,name3,score3,name4,score4,name5,score5,name6,score6,name7,score7,name8,score8,name9,score9,name10,score10 = scores.retrieveData()

        return TemplateResponse(request, 'index.html', {"n1":name1, "s1":score1, "n2":name2, "s2":score2, "n3":name3, "s3":score3, "n4":name4, "s4":score4, 
        "n5":name5, "s5":score5, "n6":name6, "s6":score6, "n7":name7, "s7":score7, "n8":name8, "s8":score8, "n9":name9, "s9":score9, 
        "n10":name10, "s10":score10})

    elif request.method == 'POST':
        data = request.body

        scores.submitData(data)
        

        dataSent = True

        return HttpResponse("Post")







        # WORKING POST
        #score.scores = request.body
        #print (score.scores)
        #return HttpResponse("Post")
        #scoresData.save()