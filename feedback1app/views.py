from django.shortcuts import render
from feedback1app.models import Feedback1Data
from feedback1app.forms import Feedback1Form
from django.http.response import HttpResponse
import datetime

date=datetime.datetime.now()
def Feedback_view(request):
    if request.method=='POST':
        fform1=Feedback1Form(request.POST)
        if fform1.is_valid():
            name1=request.POST.get('Name')
            rating1=request.POST.get('Rating')
            mobile1=request.POST.get('Mobile')
            mail1=request.POST.get('Email')
            feedback2=request.POST.get('Feedback')

            data=Feedback1Data(
                Name=name1,
                Rating=rating1,
                Mobile=mobile1,
                Email=mail1,
                Date=date,
                feeb=feedback2
            )
            data.save()
            feedback1=Feedback1Data.objects.all()
            fform1=Feedback1Form()
            return render(request,'feedback1.html',{'fform1':fform1,'feedback1':feedback1})
    else:
        feedback1=Feedback1Data.objects.all()
        fform1=Feedback1Form()
        return render(request,'feedback1.html',{'fform1':fform1,'feedback1':feedback1})

