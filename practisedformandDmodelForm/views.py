from django.shortcuts import render
 
# Create your views here.
def home(request): 
     if request.method == "POST":
        name=request.POST.get('username')
        email=request.POST.get('email')
        return render(request,'home.html',{'name':name,'email':email})
     else:
      return render(request,'home.html')
