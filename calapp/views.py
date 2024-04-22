from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'input.html')
def calculate(request):
    x=int(request.GET["t1"])
    y=int(request.GET["t2"])
    opt=request.GET["op"]
    result=" "
    if opt=="add":
        z=x+y
        result=result+"The sum is:"+str(z)
    elif opt=="sub":
        z=x-y
        result=result+"The sub is:"+str(z)
    elif opt=="mul":
        z=x*y
        result=result+"The mul is:"+str(z)
    else:
        z=x/y
        result=result+"The div is:"+str(z)
    return HttpResponse(result)



