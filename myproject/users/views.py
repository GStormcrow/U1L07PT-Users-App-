from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST) #submitted with data
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else: #get method
        form = UserCreationForm()
    context = {
        'active_link': 'register',
        'form':form
    }
    return render(request, 'users/register.html', context)