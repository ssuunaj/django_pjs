from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterFrom

def register(request):
    #check if the request method is post
    if request.method == 'POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your are currently login')
            return redirect('login')
    else:
        form = RegisterFrom()
        return render(request,'users/register.html',{'form':form})


#in order to restrict access to a view we add a decorator to the view 
@login_required
def profilepage(request):
    return render(request,'users/profile.html')










