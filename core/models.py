from django.db import models


class Task(models.Model):
    url = models.CharField(max_length=200, verbose_name='Url')
    identifier = models.CharField(unique=True,
                                  max_length=8,
                                  verbose_name='Task identifier')
    analyzed_data = models.JSONField(default=dict, blank=True, verbose_name='Analyzed data')

    def __str__(self):
        return f'{self.identifier}: {self.url}'
