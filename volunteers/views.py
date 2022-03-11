from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from volunteers.models import Volunteer
# Create your views here.
@login_required
def index(request):
    voluntees = Volunteer.objects.all()
    context = {
        'volunteers': voluntees,
    }
    return render(request,'volunteers/index.html',context)

