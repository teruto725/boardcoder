from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import SignUpForm



class UserCreateView(CreateView):
    model = CustomUser
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")#nameからurlを生成できる


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "accounts/detail.html"

    # override
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.request.user.is_authenticated:
            print("A")
            messages.error(self.request,"ログインしてください")
            return HttpResponseRedirect(reverse('accounts:login'))
        elif self.object.pk == self.request.user.pk:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            messages.error(self.request, "権限がありません")
            return HttpResponseRedirect(reverse('home:home'))
