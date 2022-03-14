from django.shortcuts import render
from .forms import DonationForm
from .models import Donation
# Create your views here.
def index(request):
    form = DonationForm()
    donations = Donation.objects.all()
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
        'donations': donations
    }
        
    return render(request,'donation/index.html',context)
