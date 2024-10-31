from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250)
    genre = models.ForeignKey('genres.Genre', on_delete=models.PROTECT, related_name='movies')
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    actors = models.ManyToManyField('actors.Actor', related_name='movies')
    synopsis = models.TextField()

    def __str__(self):
        return self.title
