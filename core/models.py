from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='No details')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Kontakti')

    def __str__(self):
        return self.title
