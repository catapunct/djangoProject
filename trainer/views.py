from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from student.models import Student
from trainer.forms import TrainerForm
from trainer.models import Trainer


class TrainerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('list-of-trainers')
    permission_required = 'trainer.add_trainer'


class TrainerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'
    permission_required = 'trainer.view_list_of_trainers'


#STEP1: VA DEFINITI IN VIEWS.PY O NOUA CLASA NUMITA TrainerListView -> ListView (template_name, model, context_object_name)
#STEP2: VA DEFINITI URL IN urls.py din aplicatia trainer si il veti adauga in meniul aplicatie din interfata
#STEP3: VA DEFINITI ACEA PAGINA .HTML DAR ELEMENTELE VOR FI ASEZATE SUB FORMA DE CARD


# STEP1: DEFINIM O NOUA CLASA TrainerUpdateView unde vom folosi UPDATEVIEW (template_name, model, form_class, success_url)
# STEP2: VOM DEFINI UN NOU URL IN URLS.PY
# STEP3: ADAUGAREA URL IN DROPDOWN-UL DIN LIST OF TRAINERS


class TrainerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('list-of-trainers')
    permission_required = 'trainer.change_trainer'


class TrainerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'trainer/details_trainer.html'
    model = Trainer
    permission_required = 'trainer.view_trainer'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        all_students_per_trainer = Student.objects.filter(trainer_id=self.kwargs['pk'])
        data['all_student_per_trainer'] = all_students_per_trainer

        return data

