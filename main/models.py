from django.db import models

# Create your models here.
class TaskCartegory(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class  Meta:
        db_table = 'task_categories'

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(TaskCartegory, on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'tasks'

