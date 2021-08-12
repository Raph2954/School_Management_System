from django.contrib import admin
from django.db import models
from multipleselectionfield import MultipleSelectionField
from phonenumber_field.modelfields import PhoneNumberField
#from result_app.forms import ResultForm


ROLES = (
    (1, 'Proprietor'),
    (2, 'Vice principal'),
    (3, 'Dean'),
    (4, 'ICT Director'),
    (5, 'Class Teacher')
)
SEX_CHOICE = (
    (1, 'male'),
    (2, 'female')
)
TERMS = (
    (1, 'First Term'),
    (2, 'Second Term'),
    (3, 'Third Term')
)
TUITION = (
    (1, 'Yes'),
    (2, 'No')
)


#models for the teacher entry
class Teacher(models.Model):
    First_Name = models.CharField(max_length=250)
    Last_Name = models.CharField(max_length=250)
    Date_Of_Birth = models.DateField
    Sex = MultipleSelectionField(choices=SEX_CHOICE, max_choices=1, null=True)
    Phone_Number = PhoneNumberField(null=True)
    Email = models.EmailField(null=True, blank=True)
    Address = models.CharField(max_length=500)
    Date_Of_incorporation = models.DateField
    Qualification = models.CharField(max_length=300)
    Subjects_Handling = models.ForeignKey('Subjects', on_delete=models.CASCADE, default=False)
    Admin_Role = MultipleSelectionField(help_text='what\'s your position in the school', choices=ROLES, max_choices=1,
                                        default=None, null=True)
    Photo = models.ImageField(upload_to='media/users/%Y/%m/%d/', default=None)
    State_of_origin = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.First_Name


class Subjects(models.Model):
    Subject_name = models.CharField(max_length=300)
    Class_allocated = models.ForeignKey('Class', on_delete=models.CASCADE, null= False, default= True)
    #Teacher_In_Charge = models.ForeignKey('Teacher',default=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.Subject_name


class Student(models.Model):
    Image = models.ImageField (upload_to='image',default=False)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    Date_of_birth = models.DateField(default=True)
    #Present_class = models.ForeignKey('Class', on_delete=models.CASCADE,default=False)
    Address = models.CharField(max_length=500)
    Gender = models.ForeignKey('Gender', on_delete=models.CASCADE,default=None, null=False)
    Guardians_Phone_Number = models.CharField(max_length=11)
    PaidTuition = models.ForeignKey('Fees', on_delete=models.CASCADE, null=False, default=True)
    Current_class = models.ForeignKey('Class', on_delete=models.CASCADE,default=None)
    #Add_Result = models.Prefetch(lookup=ResultForm)
    #Upload_Result = models.FileField(upload_to='files', default=True, null=True)
    #AddResultOnline = (on_delete=models.CASCADE, default=False)

    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.first_name



class Class(models.Model):
    Class_Name = models.CharField(max_length=8, null= False)
    #Class_Teacher_Name = models.ForeignKey('secondary.Teacher', on_delete=models.CASCADE, default=False)
    Number_Of_Students_In_Class = models.IntegerField(default=0)
    Number_Of_Students_That_Have_Paid_Fees = models.IntegerField(default=0)
    Number_Of_Students_Owing_Outstanding_Debt = models.IntegerField(default=0)



    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.Class_Name

class Fees(models.Model):
    school_fees_status = models.CharField(max_length=30, null=False)

    class Meta:
        verbose_name_plural = 'Fees'

    def __str__(self):
        return self.school_fees_status

class Gender(models.Model):
    gender = models.CharField(max_length=30, null=False)

    class Meta:
        verbose_name_plural = 'genders'

    def __str__(self):
        return self.gender


