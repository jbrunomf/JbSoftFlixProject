from django.db import models
from django.core.validators import MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.PROTECT, related_name='reviews')
    rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5, "A nota máxima para o review deve ser 5."),
        ]
    )
    review_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie.title
