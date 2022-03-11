from django.shortcuts import render
from volunteers.models import Volunteer
# Create your views here.
def index(request):
   
    return render(request,'donation/index.html')
