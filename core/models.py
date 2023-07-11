from django.db import models
from worker.models import Worker, Resume
class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(default='No details')
    is_relevant = models.BooleanField(default=True)
    email = models.EmailField()
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    candidate = models.ManyToManyField(
        to=Worker,
        blank=True
    )

    category = models.ForeignKey(
        to='Category',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name='категория'
    )

    def __str__(self):
        return self.title

    class META:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['salary']


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(default='Address does not shown')
    staff_quantity = models.IntegerField()
    is_hunting = models.BooleanField(default=False)


    def __str__(self):
        return self.name


