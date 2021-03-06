from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from volunteers.models import Volunteer
# Create your views here.
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    voluntees = Volunteer.objects.all()
    context = {
        'volunteers': voluntees,
    }
    return render(request,'volunteers/index.html',context)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})