from django.shortcuts import render
from .models import Recruiter
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecruiterUpdateForm
from django.urls import reverse_lazy


def recruiter_list(request):
    recruiters = Recruiter.objects.all()
    return render(request, 'recruit/list.html', {'recruiters': recruiters})

def recruiter_detail(request, pk):
    recruiter_object = Recruiter.objects.get(pk=pk)
    return render(request, 'recruit/detail.html', {'recruiter_object': recruiter_object})


class RecruitView(View):
    def get(self, request):
        recruiters = Recruiter.objects.all()
        return render(request, 'recruit/list.html', {'recruiters': recruiters})

class RecruitListView(LoginRequiredMixin,ListView):
    model = Recruiter

class RecruiterCreateView(CreateView):
    model = Recruiter
    fields = '__all__'
    success_url = reverse_lazy('recruiter-list-class')

class RecruiterUpdateView(View):
    template = 'recruit/update.html'

    def get_context(self, **kwargs):
        id = kwargs["id"]
        recruiter_object = Recruiter.objects.get(id=id)
        form = RecruiterUpdateForm(instance=recruiter_object)
        context = {}
        context["form"] = form
        context["recruiter"] = recruiter_object
        return context

    def my_render(self, request, context):
        return render(request,
                      self.template,
                      context
                      )

    def get(self, request, *args, **kwargs):
        context = self.get_context(**kwargs)
        return self.my_render(request, context)


    def post(self, request, *args, **kwargs):
        context = self.get_context(**kwargs)
        context["form"] = RecruiterUpdateForm(instance=context["recruiter"], data=request.POST)
        form = context["form"]

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Info edited')
        else:
            messages.add_message(request, messages.WARNING, 'Failed')
        return self.my_render(request, context)


class RecruiterGenericUpdateView(UpdateView):
    model = Recruiter
    fields = [f.name for f in Recruiter._meta.get_fields() if f.name not in ['id', 'user']]
    template_name = 'recruit/generic_update.html'
    success_url = reverse_lazy('recruiter-list-class')