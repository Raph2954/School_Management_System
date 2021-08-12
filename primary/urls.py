from django.urls import path, include
from primary.views import PupilDetail, TeacherDetail, ElementaryDetail, SubjectDetail


urlpatterns = [
    path('PrimaryTeacher/',TeacherDetail.as_view, name="PrimaryTeacher"),
    path('Pupil/', PupilDetail.as_view, name="pupil"),
    path('Elementary', ElementaryDetail.as_view, name="elementary"),
    path('Subject', SubjectDetail.as_view, name="subjects"),

]