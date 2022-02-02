from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Message, Profile, Skill
from django.db.models import Q
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import userRegistrationForm, AccountForm, CreateAccountForm, MessageForm
from .utility import searchTutor, paginationProfiles



# Create your views here.
def userLogin(request):
    page = 'Login'

    if request.user.is_authenticated:
        return redirect('tutorials')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exit, Please Register')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tutorials')
        else:
            messages.error(request, 'Username or Password is Incorrect')
        
    context = {'page':page}
    return render(request, 'users/login_Register.html', context )



def userRegister(request):
    form = userRegistrationForm()

    if request.method == "POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "Registration was successful")
            return redirect("userLogin")
        else:
            messages.error(request, "Registeration was unsuccessful, please try again")

    context = {'form': form}
    return render(request, 'users/login_Register.html', context )


def userLogout(request):
    logout(request)
    return redirect('homepage')
    


def profile(request):
    profiles, searchQuery = searchTutor(request)
    
    custom_range, profiles = paginationProfiles(request, profiles, 3)

    context = { 'profiles': profiles, 'searchQuery':searchQuery, 'custom_range':custom_range}
    return render(request, 'users/profile.html', context)




def singleProfile(request, pk):
    
    profile = Profile.objects.get(id=pk)
    skills = profile.skills.all()
    
    context = { 'profile':profile, 'skills':skills, }
    return render(request, 'users/singleProfile.html', context)


@login_required(login_url='userLogin')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skills.all()

    context = {'profile': profile, 'skills':skills}
    return render(request, 'users/account.html', context)



def createAccount(request):
    page = 'createAccount'
    form = CreateAccountForm()

    context = {'page': page, 'form':form}
    return render(request, 'users/userAccount.html', context)


@login_required(login_url='userLogin')
def updateAccount(request):
    page = 'updateAccount'
    account = request.user.profile
    form = AccountForm(instance = account)
    

    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance = account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update was successful')
            
            return redirect('account')

    context = {'form': form, 'account':account, 'page':page}
    return render(request, 'users/userAccount.html', context)


@login_required(login_url='userLogin')
def inboxMessage(request):
    profile = request.user.profile
    inboxMessages = profile.messages.all()
    inboxTotal = inboxMessages.count()
    unread = inboxMessages.filter(is_read = False).count

    context = {'inboxMessages': inboxMessages, 'inboxTotal':inboxTotal, 'unread':unread, 'profile':profile}
    return render(request, 'users/inboxMessage.html', context)



def sendMessage(request, pk):
    
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.senderName = sender.name
                message.email = sender.email

            message.save()
            messages.success(request, 'Your message was Successfully Sent')

            return redirect('singleProfile', pk = recipient.id)

    context = {"form":form, 'recipient':recipient }
    return render(request, 'users/sendMessage.html', context)





@login_required(login_url='userLogin')
def viewMessage(request, pk):
    profile = request.user.profile
    messsageDetails = profile.messages.get(id=pk)

    if messsageDetails.is_read == False:
        messsageDetails.is_read = True
        messsageDetails.save()

    context = {'messsageDetails':messsageDetails, 'profile':profile}
    return render(request, 'users/viewMessage.html', context)





   