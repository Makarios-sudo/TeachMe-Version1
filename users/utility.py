from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage




#Search tutors 
def searchTutor(request):

    searchQuery = ''

    if request.GET.get("searchQuery"):
        searchQuery = request.GET.get('searchQuery')
        
    #skills = Skill.object.filter(name__iexact=searchQuery)-- to query a foriegnkey query

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=searchQuery) |
        Q(intro__icontains=searchQuery) 
        #Q(skill__in=skills) ------------------- For querying the child object
         )

    return profiles, searchQuery





def paginationProfiles(request, profiles, result):
    page = request.GET.get('page')
    results = 3
   
    paginator =Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
   

    return custom_range, profiles

    