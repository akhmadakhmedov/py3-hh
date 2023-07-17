from django.shortcuts import render, redirect, HttpResponse
from .models import Worker, Resume
from .forms import ResumeEditForm
# Create your views here.
def workers(request):
    workers = Worker.objects.all()
    context = {'workers': workers}
    return render(request, 'workers.html', context)

def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    # SELECT * FROM Worker WHERE id=(id)
    context = {'worker': worker_object}
    return render(request, 'worker.html', context)

def resume_list(request):
    resume_query = Resume.objects.all()
    return render(
        request, 'resume/resume_list.html',
        {'resumes': resume_query}
    )

def resume_info(request, id):
    resume_object=Resume.objects.get(id=id)
    return render(
        request, 'resume/resume_detail.html',
        {'resume': resume_object}
    )

def my_resume(request):
    if request.user.is_authenticated:
        resume_query = Resume.objects.filter(worker=request.user.worker)
        # resume_query = request.user.worker.resume.all()
        return render(
            request, 'resume/resume_list.html',
            {'resumes': resume_query}
        )
    else:
        return redirect('home')

def add_resume(request):
    template = 'resume/resume_add.html'
    if request.method == 'GET':
        # show the FORM
        return render(request, template)
    elif request.method == 'POST':
        # add resume to Data Base
        new_resume = Resume()
        new_resume.worker = request.user.worker
        new_resume.title = request.POST['form-title']
        new_resume.text = request.POST['form-text']
        new_resume.save()
        return HttpResponse('New resume has been added')

def resume_edit(request, id):
    resume_object = Resume.objects.get(id=id)
    if request.method == 'GET':
        form = ResumeEditForm(instance=resume_object)
        return render(request, "resume/resume_edit.html", {'form': form})

    elif request.method == 'POST':
        form = ResumeEditForm(data=request.POST, instance=resume_object)
        if form.is_valid():
            obj = form.save()
            return redirect(resume_info, id=obj.id)
        else:
            return HttpResponse("Form is not valid")































