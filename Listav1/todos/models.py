from django.db import models

class Todo(models.Model):
    title = models.CharField(verbose_name="Insira uma nova tarefa:", max_length=100, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    final_date = models.DateField(null=True)