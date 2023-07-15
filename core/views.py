from django.shortcuts import render, HttpResponse
from .models import Vacancy
from django.contrib.auth.models import User

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

def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id) # one object
    candidates = vacancy_object.candidate.all() #list
    context = {
        'vacancy': vacancy_object,
        'candidates_list': candidates
        }
    return render(request, 'vacancy/vacancy_page.html', context)

def search(request):
    word = request.GET['keyword']
    vacancy_list = Vacancy.objects.filter(title__contains=word)
    context = {'vacancies': vacancy_list}
    return render(request, 'vacancies.html', context)

def add_vacancy(request):
    template = 'vacancy/vacancy_add.html'
    if request.method == 'GET':
        # show the FORM
        return render(request, template)
    #elif request.method == 'POST':
    #    # add resume to Data Base
    #    new_vacancy = Vacancy()
    #    new_vacancy.worker = request.user.worker
    #    new_resume.title = request.POST['form-title']
    #    new_resume.text = request.POST['form-text']
    #    new_resume.save()
    #    return HttpResponse('New resume has been added')

def reg_view(request):
    if request.method == 'POST':
        user= User(
            username = request.POST['username']
        )
        user.save()
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponse('Completed')

    return render(
        request,
        'auth/register.html'
    )
