from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from users.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active and not user.is_superuser:
            auth_login(request, user)
	    return HttpResponseRedirect('/home')
        invalid_login = True
        login_form = LoginForm()
        return render_to_response('login.html', locals(), context_instance=RequestContext(request))
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/home')
        else:
            login_form = LoginForm()
        return render_to_response('login.html', locals(), context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html',locals(),context_instance=RequestContext(request))


def register(request):

    register_form = RegisterForm()
    errorinregistration = False
    registered = False
    if request.method=='POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            # Create the User
            new_user = User.objects.create_user(
                username = register_form.cleaned_data['username'],
                email = register_form.cleaned_data['email'],
                password = register_form.cleaned_data['password'],
                )    
            new_user.is_active=True #took from userportal
            new_user.save()
	    registered = True
            return HttpResponseRedirect('/login') 
	else:
	    errorinregistration = True
            return render_to_response('register.html' , locals() ,context_instance = RequestContext(request))
    else:
        return render_to_response('register.html' , locals() ,context_instance = RequestContext(request))

def logout(request):
    """
        View for logging out users from the session.
    """
    if request.user.is_authenticated():
        auth_logout(request)
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')
