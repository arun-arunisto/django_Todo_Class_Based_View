from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm

# Create your views here.
class LoginPageView(View):
    template_name = 'user_auth/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form':form, 'message':message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return render(request, 'user_auth/home.html', context={'message':"Login Successfully!"})
        message = 'Login Failed!'
        return render(request, self.template_name, context={'form':form, 'message':message})
