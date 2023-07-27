from django.shortcuts import render, HttpResponse, redirect
from .models import Vacancy, Company
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import VacancyForm, CompanyForm, VacancyEditForm
from .filters import VacancyFilter

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
    #vacancies = Vacancy.objects.all() # v DJANGO ORM "SELECT * FROM Vacancies"
    #context = {'vacancies': vacancies} # context data for jinja2
    vacancy_filter = VacancyFilter(request.GET, queryset=Vacancy.objects.all())
    context={"vacancy_filter": vacancy_filter}
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
    vacancy_list = Vacancy.objects.filter(title__icontains=word)
    context = {'vacancies': vacancy_list}
    return render(request, 'vacancies.html', context)

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            # authorisation
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Error username or password")

    return render(request, 'auth/sign-in.html')

def sign_out(request):
    logout(request)
    return redirect(sign_in)


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

def vacancy_add_via_django_form(request):
    if request.method == 'POST':  # Adding
        form = VacancyForm(request.POST)
        if form.is_valid():
            new_vacancy = form.save()
            return redirect(f'/vacancy/{new_vacancy.id}/')

    vacancy_form = VacancyForm()
    return render(request,
                  'vacancy/vacancy_django_form.html',
                  {'vacancy_form': vacancy_form}
                  )

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

def vacancy_django_edit(request, id):
    vacancy_object = Vacancy.objects.get(id=id)
    if request.method == 'GET':
        form = VacancyEditForm(instance=vacancy_object)
        return render(request, "vacancy/vacancy_django_edit.html", {'form': form})

    elif request.method == 'POST':
        form = VacancyEditForm(data=request.POST, instance=vacancy_object)
        if form.is_valid():
            obj = form.save()
            return redirect(vacancy_detail, id=obj.id)
        else:
            return HttpResponse("Form is not valid")


def create_company(request):
    context = {}

    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return HttpResponse('Ready!')
    company_form = CompanyForm()
    context['form'] = company_form
    return render(request, 'company/create.html', context)

def company_edit(request, id):
    company_object = Company.objects.get(id=id)

    if request.method == 'POST':
        form = CompanyForm(data=request.POST, instance=company_object)
        if form.is_valid():
            form.save()
            return HttpResponse('Ready')
    form = CompanyForm(instance=company_object)
    return render(request, 'company/edit.html', {'form': form})