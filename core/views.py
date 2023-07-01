from django.shortcuts import render, HttpResponse
from .models import Vacancy
# Create your views here.

def homepage(request):
    return render(request=request, template_name='index.html')

def about(request):
    return HttpResponse('''
                        <div>We are one of the best company in the world</div>
                        ''')

def contact(request):
    return HttpResponse('''
                        <div>
                            <b>Phone: 0755 057501<br>
                            <b>Email: ahmedov.thy@gmail.com
                        </div>
                        ''')

def address(request):
    return HttpResponse('''
                        <ul>
                            <li>Pakhta abad str 144</li>
                            <li>Osh City, Osh District</li>
                        </ul>
                        ''')

def vacancy_list(request):
    vacancies = Vacancy.objects.all() # v DJANGO ORM "SELECT * FROM Vacancies"
    context = {'vacancies': vacancies} # context data for jinja2
    return render(request, 'vacancies.html', context)