from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import DetailView
from django.shortcuts import render
from primary.models import Teacher, Pupil, Subjects, Elementary


class TeacherDetail(DetailView):
    queryset = Teacher.objects.order_by('teacher__First_Name')
    template_name = "teacherslist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Teacher_list']= Teacher.objects.all()
        return context


class PupilDetail(DetailView):
    queryset = Teacher.objects.order_by('Pupil__first_name')
    template_name = "admissions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Pupil_list'] = Pupil.objects.all()
        return context


class SubjectDetail(DetailView):
    queryset = Subjects.objects.order_by('Subject_name')
    template_name = "courses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject_list'] = Subjects.objects.all()
        return context


class ElementaryDetail(DetailView):
    queryset = Elementary.objects.order_by('Class_Name')
    template_name = "programs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Class_list'] = Elementary.objects.all()
        return context




