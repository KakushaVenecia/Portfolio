from django.shortcuts import render
from portfolio.models import Project, Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')


def myportfolio(request):
    projects =Project.objects.all()
    return render (request, 'work.html', {"projects": projects} )

def myportfolio_details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'work_detail.html', context)

def display_contact(request):
    contacts =Contact.objects.all()
    return render(request, 'contact.html', {"contacts":contacts})