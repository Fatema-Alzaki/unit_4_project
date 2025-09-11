from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import PrintJob, Material, Printer
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Home page
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def printjob_index(request):
    # Show only the jobs of the logged-in user
    printjobs = PrintJob.objects.filter(user=request.user)
    return render(request, 'printjobs/index.html', { 'printjobs': printjobs })

@login_required
def printjob_detail(request, printjob_id):
    printjob = PrintJob.objects.get(id=printjob_id)
    return render(request, 'printjobs/detail.html', { 'printjob': printjob })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('printjob-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

# Home with login view
class Home(LoginView):
    template_name = 'home.html'

# --- PrintJob Views ---
class PrintJobCreate(LoginRequiredMixin, CreateView):
    model = PrintJob
    fields = ['name', 'stl_file', 'material', 'weight_grams', 'estimated_time']

    def form_valid(self, form):
        form.instance.user = self.request.user  # assign current user
        return super().form_valid(form)

class PrintJobUpdate(UpdateView):
    model = PrintJob
    fields = ['name', 'material', 'weight_grams', 'estimated_time', 'status']

class PrintJobDelete(DeleteView):
    model = PrintJob
    success_url = '/printjobs/'

# --- Material Views ---
class MaterialCreate(CreateView):
    model = Material
    fields = '__all__'

class MaterialList(ListView):
    model = Material

class MaterialDetail(DetailView):
    model = Material

class MaterialUpdate(UpdateView):
    model = Material
    fields = ['name', 'color', 'cost_per_gram']

class MaterialDelete(DeleteView):
    model = Material
    success_url = '/materials/'

# --- Printer Views ---
class PrinterCreate(CreateView):
    model = Printer
    fields = '__all__'

class PrinterList(ListView):
    model = Printer

class PrinterDetail(DetailView):
    model = Printer

class PrinterUpdate(UpdateView):
    model = Printer
    fields = ['name', 'location', 'status']

class PrinterDelete(DeleteView):
    model = Printer
    success_url = '/printers/'
