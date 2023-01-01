from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':110,'b':220,'c':330}
    return render(request,'operations.html',d)