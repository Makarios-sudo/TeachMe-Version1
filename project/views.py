
from django.core import paginator
from django.shortcuts import render
from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import TutorialForm, ReviewForm
from .utility import searchTutorial, paginationTutorials
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.

def home(request):  
    context = {}  
    return render(request, 'homepage.html', context)



def aboutPage(request):
    return render(request, 'aboutPage.html')


def becomeTutor(request):
    return render(request, 'becomeTutor.html')

# getting all the tutorials, pagination and search 
def tutorials(request):

    tutorials, searchQuery = searchTutorial(request)
    custom_range, tutorials = paginationTutorials(request, tutorials, 8)

    context = {'tutorials':tutorials, "searchQuery":searchQuery, 'custom_range':custom_range}
    return render(request, 'projects/tutorials.html', context)


#@login_required(login_url='userLogin')
def singleTutorial(request, pk): 
    
    tutorial = Tutorial.objects.get(id=pk)
    # tags = tutorial.tags.all() -----------> another alternative for querying the many to many relationsip (tag) associated with the tutorial model
    #reviews = reviews.review_set.all() ---------> another alternative for foreignkey child-object associated with the tutorial model
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tutorial = tutorial
            review.save()
            return redirect('singleTutorial',  pk=tutorial.id )  


    context = {'tutorial':tutorial, 'form':form,  }
    return render(request, 'projects/singleTutorial.html', context)


# creating new tutorial
@login_required(login_url='userLogin')
def createTutorial(request):
    profile = request.user.profile
    form = TutorialForm()
    
    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            
            messages.info(request, 'A new Tutorial have been successfully created')
            return redirect('account')

    context = {'form':form, 'profile':profile}
    return render(request, 'projects/createTutorial.html', context)


# updating an existing tutorial
@login_required(login_url='userLogin')
def updateTutorial(request, pk):
    tutorial = Tutorial.objects.get(id=pk)
    form = TutorialForm(instance=tutorial)

    if request.method == 'POST':
        form = TutorialForm(request.POST, instance=tutorial)
        if form.is_valid():
            form.save()
            messages.info(request, 'Update was successful')
            return redirect('account')

    context = {'form':form, 'object':tutorial}
    return render(request, 'projects/updateTutorial.html', context)


#  deleting an existing tutorial 
@login_required(login_url='userLogin')
def deleteTutorial(request, pk):
    tutorial = Tutorial.objects.get(id=pk)

    if request.method=='POST':
        tutorial.delete()
        messages.info(request, 'Delete was successful')
        return redirect('account')

    context = { 'object': tutorial}
    return render (request, 'projects/deleteTutorial.html', context )






    

    



