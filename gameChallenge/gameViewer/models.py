from django.db import models
from django.template.defaultfilters import slugify

class Game(models.Model):
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length= 50)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    publisher = models.CharField(max_length=50)
    n_players = models.IntegerField()
    slug = models.SlugField(unique=True)

    # Process data on save, assign slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    # String interpretations
    class Meta:
        verbose_name_plural = 'Games'

    def __str__(self):
        return self.name
