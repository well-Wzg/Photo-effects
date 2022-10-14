from django.contrib import messages
from django.core.mail import message
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView
from main_app import forms
from main_app import models

class IndexView(TemplateView):
    template_name = "main_app/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.ImageModelForm()
        context["history_images"] = models.ImageModel.objects.all().order_by("last_edit_time")
        return context

    def post(self,request,*args,**kwargs):
        form = forms.ImageModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Upload Success")
            return redirect('main_app:index')

        messages.success(request, "Upload Fail")
        return redirect('main_app:index')


class EditView(TemplateView):
    template_name = "main_app/edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        img_id = kwargs.get("id",None)
        context["img_obj"] = models.ImageModel.objects.get(id=img_id)
        return context
