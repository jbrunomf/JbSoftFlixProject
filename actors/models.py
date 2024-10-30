from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'United States'),
    ('UK', 'United Kingdom'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('RU', 'Russia'),
    ('BR', 'Brazil'),
    ('CN', 'China'),
    ('IN', 'India'),
)


class Actor(models.Model):
    name = models.CharField(max_length=150)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=3,
                                   choices=NATIONALITY_CHOICES,
                                   default='BR',
                                   blank=True,
                                   null=True)

    def __str__(self):
        return self.name
