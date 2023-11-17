from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import scores
from django.views.decorators.csrf import csrf_exempt

dataSent = False

@csrf_exempt
def index(request):

    if request.method == 'GET':

        data = scores.retrieveData()

        return TemplateResponse(request, 'index.html', {"data":data})

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