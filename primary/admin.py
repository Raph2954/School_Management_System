from django.contrib import admin
from primary.models import Teacher
from primary.models import Pupil
from primary.models import Subjects
from primary.models import Elementary


class ElementaryAdmin(admin.ModelAdmin):
    List_display = ['Class_Name', 'Class_Teacher_Name', ]
    List_filter = ['Class_Name', 'Class_Teacher_Name', ]
    List_editable = ['Class_Name', 'Class_Teacher_Name', ]
admin.site.register(Elementary, ElementaryAdmin)

class PupilAdmin(admin.ModelAdmin):
    List_display = ['first_name', 'last_name', 'Date_of_birth', 'students_class', 'Address',
                    'sex', 'guardians_phone_number', 'Tuition_status', 'subjects_offered', ]
    List_filter = ['student_class', 'sex', 'Tuition_status', 'subjects_offered', ]
    List_editable = ['first_name', 'Lasts_name', 'Tuition_status', 'students_class', 'subject_offered', 'Address']
admin.site.register(Pupil, PupilAdmin)


class SubjectsAdmin(admin.ModelAdmin):
    List_display = ['Subject_name', 'Teacher_In_Charge', 'Class_allocated', ]
    List_filter = ['Subject_name', 'Teacher_In_Charge', 'Class_allocated', ]
    List_editable = ['Subject_name', 'Teacher_In_Charge', 'Class_allocated', ]
admin.site.register(Subjects, SubjectsAdmin)


class AddTeacherAdmin(admin.ModelAdmin):
    List_display = ['Class_Name', 'Class_Teacher_Name', ]
    List_filter = ['Class_Name', 'Class_Teacher_Name', ]
    List_editable = ['Class_Name', 'Class_Teacher_Name', ]
admin.site.register(Teacher, AddTeacherAdmin)
