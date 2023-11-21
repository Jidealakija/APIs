from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    slug = models.SlugField(max_length=300)
    author = models.ManyToManyField(User)
    pages = models.IntegerField()
    date_published = models.DateField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to='book_image', blank=True, null=True )

    class Meta:
        verbose_name_plural = 'Book'

    def __str__(self):
        return self.title