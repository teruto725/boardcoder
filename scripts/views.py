from pprint import pprint

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .forms import ScriptCreateForm
from .models import Script
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateScriptView(CreateView, LoginRequiredMixin ):
    model = Script
    form_class = ScriptCreateForm
    template_name = "scripts/create.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print("s")
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.save()
            #messages.success(self.request, "OK,upload:"+obj.name)
            return HttpResponseRedirect(reverse('scripts:index'))
        else:
            raise Http404("Question does not exist")


class ListScriptView(ListView,LoginRequiredMixin):
    model = Script
    template_name = "scripts/index.html"
    context_object_name = "scripts"

    def get_queryset(self):# can do filter
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class DeleteScriptView(DeleteView,LoginRequiredMixin):
    model = Script
    success_url = reverse_lazy("scripts:index")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, "Delete "+self.object.name)
        return self.delete(request, *args, **kwargs)

