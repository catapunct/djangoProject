from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from student.filters import StudentFilter
from student.forms import StudentForm
from student.models import Student
from student.serializers import StudentSerializer


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'  # pagina .HTML unde va fi RANDAT/AFISAT formularul
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('create_student')  # dupa ce vom da click pe butonul de salvare,
    # vom fi redirectionati catre homepage.
    permission_required = 'student.add_student'

    def get_context_data(self, **kwargs):
        data = super(StudentCreateView, self).get_context_data(**kwargs)
        students = Student.objects.all()
        data['all_students'] = students

        return data

# Folosim CreateView (view generic in django) pentru a adauga si sa salvam date intr-o tabela, pe baza unui formular.


# STEP1 : VA DEFINITI MODELUL IN MODELS.PY
# STEP2: IN FISIERUL VIEWS.PY DIN APLICATIA STUDENT VA DEFINITI O CLASA CARE MOSTENESTE CREATEVIEW(TEMPLATE_NAME, MODEL, FIELDS, SUCCESS_URL)
# STEP3: ADAUGAM URL PENTRU CLASA DEFINITA
# STEP4: VOM SCRIE IN FISIER HTML (MENTIONAT IN VARIABILA TEMPLATE_NAME) COD PENTRU GENERAREA FORMULARLUI

class StudentsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'
    permission_required = 'student.view_list_of_students'


    def get_context_data(self, **kwargs):
        data = super(StudentsListView, self).get_context_data(**kwargs)

        students = Student.objects.all()  # stochez toti studentii din tabela student_student
        my_filter = StudentFilter(self.request.GET, queryset=students)  # pe baza cautarilor din formularul de search
        # voi cauta prin toti studentii din tabela (satele nu se saleaza, prin metoda GET)
        students = my_filter.qs
        data['all_students'] = students
        data['my_filter'] = my_filter

        return data


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.change_student'


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.delete_student'


@login_required
@permission_required('student.delete_by_modal')
def delete_student_modal(request, pk):
    Student.objects.filter(id=pk).delete()
    return redirect('list-of-students')


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student/details_student.html'
    model = Student
    permission_required = 'student.view_student'


class StudentApi(APIView):

    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

