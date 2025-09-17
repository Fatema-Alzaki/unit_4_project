from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import PrintJob, Material, Printer, PrintHistory
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Home page
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


# Home with login view
class Home(LoginView):
    template_name = 'home.html'


# --- PrintJob Views ---
class PrintJobList(ListView):
    model = PrintJob
    template_name = "printjobs/printjob_list.html"   # ✅ fixed underscore
    context_object_name = "printjobs"


class PrintJobDetail(DetailView):
    model = PrintJob
    template_name = "printjobs/printjob_detail.html"
    context_object_name = "printjob"


class PrintJobCreate(LoginRequiredMixin, CreateView):
    model = PrintJob
    fields = ['name', 'stl_file', 'material', 'weight_grams', 'estimated_time', 'status', 'printers']
    template_name = "printjobs/printjob_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        
        # Create PrintHistory entries for each selected printer
        for printer in form.instance.printers.all():
            PrintHistory.objects.create(
                print_job=form.instance,
                printer=printer,
                started_at=form.instance.created_at,
                success=True  # default to True, update later if needed
            )
        return response



class PrintJobUpdate(UpdateView):
    model = PrintJob
    fields = ['name', 'material', 'weight_grams', 'estimated_time', 'status']
    template_name = "printjobs/printjob_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        
        if form.instance.status in ['C', 'F']:  # Completed or Failed
            for history in PrintHistory.objects.filter(print_job=form.instance):
                from django.utils import timezone
                history.finished_at = timezone.now()
                history.success = (form.instance.status == 'C')
                history.save()
        
        return response



class PrintJobDelete(DeleteView):
    model = PrintJob
    template_name = "printjobs/printjob_confirm_delete.html"
    success_url = '/printjobs/'


# --- Material Views ---
class MaterialList(ListView):
    model = Material
    template_name = "materials/material_list.html"
    context_object_name = "materials"


class MaterialDetail(DetailView):
    model = Material
    template_name = "materials/material_detail.html"
    context_object_name = "material"


class MaterialCreate(CreateView):
    model = Material
    fields = ['name', 'color', 'cost_per_gram']
    template_name = "materials/material_form.html"


class MaterialUpdate(UpdateView):
    model = Material
    fields = ['name', 'color', 'cost_per_gram']
    template_name = "materials/material_form.html"


class MaterialDelete(DeleteView):
    model = Material
    template_name = "materials/material_confirm_delete.html"
    success_url = '/materials/'


# --- Printer Views ---
class PrinterList(ListView):
    model = Printer
    template_name = "printers/printer_list.html"
    context_object_name = "printers"


class PrinterDetail(DetailView):
    model = Printer
    template_name = "printers/printer_detail.html"
    context_object_name = "printer"


class PrinterCreate(CreateView):
    model = Printer
    fields = ['name', 'location', 'status']
    template_name = "printers/printer_form.html"
    success_url = '/printers/'

class PrinterUpdate(UpdateView):
    model = Printer
    fields = ['name', 'location', 'status']
    template_name = "printers/printer_form.html"


class PrinterDelete(DeleteView):
    model = Printer
    template_name = "printers/printer_confirm_delete.html"
    success_url = '/printers/'


from .models import PrintJob, Material, Printer, PrintHistory

class PrintJobHistoryList(ListView):
    model = PrintHistory
    template_name = "history/history_list.html"
    context_object_name = "histories"

    def get_queryset(self):
        return PrintHistory.objects.filter(print_job_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['printjob'] = PrintJob.objects.get(pk=self.kwargs['pk'])
        return context


class PrinterHistoryList(ListView):
    model = PrintHistory
    template_name = "history/history_list.html"
    context_object_name = "histories"

    def get_queryset(self):
        return PrintHistory.objects.filter(printer_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['printer'] = Printer.objects.get(pk=self.kwargs['pk'])
        return context
    

class PrintHistoryDetail(DetailView):
    model = PrintHistory
    template_name = "history/history_detail.html"
    context_object_name = "history"