from .models import Tutorial
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage



# search tutorial 
def searchTutorial(request):
    searchQuery = ''
    if request.GET.get('searchQuery'):
        searchQuery = request.GET.get('searchQuery')
    
    tutorials = Tutorial.objects.filter(
        Q(name__icontains=searchQuery)|
        Q(description__icontains=searchQuery)
    )

    return tutorials, searchQuery



# paginator 
def paginationTutorials(request, tutorials, result):

    page = request.GET.get('page')
    results = 8
    paginator =Paginator(tutorials, results)

    try:
        tutorials = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        tutorials = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        tutorials = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
   

    return custom_range, tutorials