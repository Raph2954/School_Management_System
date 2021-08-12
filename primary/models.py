from django.contrib import admin
from django.db import models
from multipleselectionfield import MultipleSelectionField

ROLES = (
    (1, 'Proprietor'),
    (2, 'Vice principal'),
    (3, 'Dean'),
    (4, 'ICT Director'),
    (5, 'Class Teacher')
)
SEX_CHOICE = (
    (1, 'male'),
    (2, 'female'),
)


class Teacher(models.Model):
    First_Name = models.CharField(max_length=250)
    Last_Name = models.CharField(max_length=250)
    Date_Of_Birth = models.DateField
    Sex = MultipleSelectionField(choices=SEX_CHOICE, max_choices=1, default=1)
    Phone_Number = models.IntegerField
    Address = models.CharField(max_length=500)
    Date_Of_incorporation = models.DateField
    Qualification = models.CharField(max_length=300)
    Subjects_Handling = models.ForeignKey('Subjects', on_delete=models.CASCADE, default=False)
    Admin_Role = MultipleSelectionField(choices=ROLES, max_choices=2, default=0)

    class Meta:
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.First_Name


class Subjects(models.Model):
    Subject_name = models.CharField(max_length=300)
    Class_allocated = models.ForeignKey('Elementary', on_delete=models.CASCADE, null=False, default=True)

    # Teacher_In_Charge = models.ForeignKey('Teacher',default=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.Subject_name


class Pupil(models.Model):
    Image = models.ImageField(upload_to='image', default=False)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    Date_of_birth = models.DateField(default=True)
    Present_class = models.ForeignKey('Elementary', on_delete=models.CASCADE, default=False)
    Address = models.CharField(max_length=500)
    sex = MultipleSelectionField(choices=SEX_CHOICE, max_choices=1, default=None)
    Guardians_Phone_Number = models.CharField(max_length=11)
    PaidTuition = models.BooleanField(default=False)
    NotPaidTuition = models.BooleanField(default=False)

    # Current_class = models.ForeignKey('Class', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.first_name


class Elementary(models.Model):
    Elementary_Name = models.CharField(max_length=8, null= False
                                       )
    # Class_Teacher_Name = models.ForeignKey('secondary.Teacher', on_delete=models.CASCADE, default=False)
    Number_Of_Class_Members = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.Elementary_Name


