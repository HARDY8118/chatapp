from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from .forms import UserForm

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

class SignupView(FormView):
    template_name = 'signup.djt'
    form_class = UserForm
    success_url = '/thanks'

    def form_valid(this,form):

        # print(form.cleaned_data)
        user=form.save()
        user.set_password(user.password)
        user.save()

        return HttpResponse('THENKS')

    def form_invalid(this,form):
        return HttpResponse(form.error,status=500)        

def SigninView(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(req,user)
            return HttpResponseRedirect(reverse('user:profile'))            
        else:
            return render(req,'signin.djt',context={'error':'Unauthorized'})
    else:
        return render(req,'signin.djt')

@login_required
def ProfileView(req):
    user_={
        'first_name':req.user.first_name,
        'last_name':req.user.last_name,
        'username':req.user.username,
        'email':req.user.email,
    }
    return render(req,'profile.djt',context=user_)
        
@login_required
def SignoutView(req):
    logout(req)
    return render(req,'signin.djt',context={'info':'Successfully signed out'})
