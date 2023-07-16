from django.shortcuts import render, HttpResponse, redirect
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

def vacancy_add(request):
    if request.method == 'POST':
        new_vacancy = Vacancy(
            title=request.POST['title'],
            salary=int(request.POST['salary']),
            description=request.POST['description'],
            email=request.POST['email'],
            contacts=request.POST['contacts'],
        )
        new_vacancy.save()
        return redirect(f'/vacancy/{new_vacancy.id}/') #new_vacancy.id
    return render(request, 'vacancy/vacancy_form.html')

def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.method == 'POST':
        vacancy.title = request.POST['title']
        vacancy.salary = int(request.POST['salary'])
        vacancy.description = request.POST['description']
        vacancy.email = request.POST['email']
        vacancy.contacts = request.POST['contacts']
        vacancy.save()
        return redirect(f'/vacancy/{vacancy.id}/') 
    return render(request,
                  'vacancy/vacancy_edit_form.html',
                  {'vacancy': vacancy}
                  )
