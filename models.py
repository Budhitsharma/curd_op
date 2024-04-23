from django.db import models

# Create your models here.
class Detailmodel(models.Model):
    Gender = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=30)
    email = models.EmailField(default="example@gmail.com")
    contact = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=Gender, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    join_date = models.DateField(null=True, blank=True)
    aadhar_no = models.IntegerField(null=True, blank=True)
    pan_no = models.CharField(max_length=15)
    skype_id = models.CharField(max_length=50)
    linkedin_id = models.CharField(max_length=100)
    qualification = models.CharField(max_length=50, default='')
    technology = models.CharField(max_length=50, default='')
    perv_company = models.CharField(max_length=50, default='')
    experience = models.IntegerField(null=True, blank=True)
    acc_no = models.IntegerField(null=True, blank=True)
    bank_name = models.CharField(max_length=30, default='')
    acc_name = models.CharField(max_length=30, default='')
    ifsc_code = models.CharField(max_length=15, default='')
    role = models.TextField(default='')
    image = models.ImageField(upload_to="myapp/images/", max_length=250, null=True, blank=True, default=None)

    def __str__(self):
        return self.name

