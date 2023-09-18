from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


class CustomLoginView(LoginView):

    def post(self, request, *args, **kwargs):
        context = super(CustomLoginView, self).get_context_data(*args, **kwargs)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context['form'] = self.get_form()
            context['errors'] = 'Usuario o contraseña incorrectos.'
            return render(request, self.template_name, context)