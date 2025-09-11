from django import forms
from .models import PrintJob, Material, Printer

class PrintJobForm(forms.ModelForm):
    class Meta:
        model = PrintJob
        fields = ['name', 'stl_file', 'material', 'weight_grams', 'estimated_time', 'status']
        widgets = {
            'estimated_time': forms.TextInput(
                attrs={'placeholder': 'hh:mm:ss (e.g. 05:30:00)'}
            ),
            'weight_grams': forms.NumberInput(
                attrs={'placeholder': 'Enter estimated weight in grams'}
            ),
        }


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'cost_per_gram', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Material name'}),
            'cost_per_gram': forms.NumberInput(attrs={'placeholder': '0.25'}),
            'color': forms.TextInput(attrs={'placeholder': 'Optional color'}),
        }


class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['name', 'status', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Printer name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Lab / Room location'}),
        }
