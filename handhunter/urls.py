
from django.contrib import admin
from django.urls import path
from core.views import *
from worker.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path("about/", about),
    path('contact/', contact),
    path('address/', address),
    path('vacancies/', vacancy_list),
    path('add-vacancy/', vacancy_add),
    path('add-vacancy-df/', vacancy_add_via_django_form),
    path('vacancy/<int:id>/', vacancy_detail, name='vacancy-info'),
    path("vacancy-edit/<int:id>/", vacancy_edit, name='vacancy-edit'),
    path("vacancy-django-edit/<int:id>/", vacancy_django_edit, name='vacancy-django-edit'),
    path('workers/', workers),
    path("worker/<int:id>/", worker_info),
    path('resume-list/', resume_list),
    path("resume-info/<int:id>/", resume_info),
    path('my-resume/', my_resume, name='my-resume'),
    path('add-resume/', add_resume, name='add-resume'),
    path("resume-edit/<int:id>/", resume_edit, name='resume-edit'),
    path("search/", search, name='search'),
    path('registration/', reg_view, name='reg'),
    path('create_company', create_company, name='create-company'),
    path('company_edit/<int:id>/', company_edit, name='company-edit'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ...:8000/static/my_style.css  #.../handhunter/core/static/my_style.css
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

