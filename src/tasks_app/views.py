from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from tasks_app.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks_app/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(is_complete=False).count()

        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'is_complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'is_complete']
    success_url = reverse_lazy('tasks')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_superuser and self.object.user != request.user:
            return redirect(reverse_lazy('tasks'))
        return super().get(request, *args, **kwargs)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name_suffix = '_delete'
    success_url = reverse_lazy('tasks')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_superuser and self.object.user != request.user:
            return redirect(reverse_lazy('tasks'))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
