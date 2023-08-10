from django.shortcuts import render
from .models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views import View
from .forms import NewsUpdateForm
from django.contrib import messages


# Create your views here.

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/list.html', {'news': news})

def news_detail(request, pk):
    news_object = News.objects.get(pk=pk)
    return render(request, 'news/detail.html', {'news_object': news_object})

class NewsCreateView(CreateView):
    model = News
    fields = "__all__"
    success_url = reverse_lazy('news-list')

class NewsUpdateView(View):
    #template = 'news/update.html'

    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        news_object = News.objects.get(id=id)
        form = NewsUpdateForm(instance=news_object)
        context = {"form": form}
        context["news"] = news_object
        return render(
            request,
            "news/update.html",
            context
        )

    def post(self, request, *args, **kwargs):
        id = kwargs["id"]
        news_object = News.objects.get(id=id)
        form = NewsUpdateForm(instance=news_object, data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Successfully edited.")
        else:
            messages.add_message(request, messages.INFO, "Please check and enter your info's again.")
        context = {"form": form}
        context["news"] = news_object
        return render(
            request,
            "news/update.html",
            context
        )

def news_detail(request, id):
    new = News.objects.get(id = id)
    new.views_count +=1
    new.user_views.add(request.user)
    new.save()


    new_view_object = NewsViews.objects.get_or_create(
        new = new,
        user = request.user
    )
    return  render(request, 'news/detail.html', {"new": new})




