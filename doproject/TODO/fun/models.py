from django.db import models

# Create your models here.

class List(models.Model):
    Task=models.CharField(max_length=100,blank=False)
    Description=models.TextField(blank=True)
    status=models.BooleanField(default=True)
    class Meta:
        verbose_name={"List"}
        verbose_name_plural={"List"} 
    def __str__(self):
        return self.Task
    
        


