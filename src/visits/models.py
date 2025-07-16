from django.db import models

# Create your models here.
class Page_Visit(models.Model):
    # db -> table 
    # id -> primary key -> autofield -> 1,2,3,4,5

    path = models.TextField(blank = True, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.path} - {self.timestamp} - {self.count}"