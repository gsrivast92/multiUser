from django.shortcuts import render
from myprofile.forms import WorkerForm
from django.views.generic.edit import FormView,CreateView
from django.views.generic import TemplateView,ListView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from myprofile.models import Worker
from django.shortcuts import redirect


# Create your views here.

def worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.user, request.POST)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.User = request.user
            worker.save()
            return redirect('dashboard')
    else:
        form = WorkerForm(request.user)
    return render(request, 'myprofile.html', {'form': form})

class RegistrationComplete(TemplateView):
    template_name = 'registration_complete.html'
