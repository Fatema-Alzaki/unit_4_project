from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Choices for job status
JOB_STATUS = (
    ('Q', 'Queued'),
    ('P', 'In Progress'),
    ('C', 'Completed'),
    ('F', 'Failed'),
)

class Material(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50, blank=True, null=True)
    cost_per_gram = models.DecimalField(max_digits=6, decimal_places=2)  # e.g., $0.25/g

    def __str__(self):
        return f"{self.name} ({self.color})" if self.color else self.name

    def get_absolute_url(self):
        return reverse('material-detail', kwargs={'pk': self.id})


class Printer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=(
            ('Available', 'Available'),
            ('Busy', 'Busy'),
            ('Maintenance', 'Maintenance'),
        ),
        default='Available'
    )

    def __str__(self):
        return f"{self.name} - {self.status}"


class PrintJob(models.Model):
    name = models.CharField(max_length=200)
    stl_file = models.FileField(upload_to="stl_files/")
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    weight_grams = models.FloatField()  # Estimated part weight in grams
    estimated_time = models.DurationField(help_text="Estimated print time (hh:mm:ss)")
    status = models.CharField(max_length=1, choices=JOB_STATUS, default='Q')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printers = models.ManyToManyField(Printer, blank=True, related_name="print_jobs")  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"

    def get_absolute_url(self):
        return reverse('printjob-detail', kwargs={'pk': self.id})

    @property
    def material_cost(self):
        """Calculate cost based on material weight."""
        if self.material:
            return self.weight_grams * float(self.material.cost_per_gram)
        return 0.0


class PrintHistory(models.Model):
    print_job = models.ForeignKey(PrintJob, on_delete=models.CASCADE, related_name="history")
    printer = models.ForeignKey(Printer, on_delete=models.SET_NULL, null=True, blank=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(blank=True, null=True)
    success = models.BooleanField(default=True)

    def __str__(self):
        return f"History for {self.print_job.name} on {self.printer}"

    class Meta:
        ordering = ['-started_at']
