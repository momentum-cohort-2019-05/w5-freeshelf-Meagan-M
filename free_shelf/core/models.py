from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the Book Title")
    author = models.CharField(max_length=200, help_text="Enter the Author Name")
    description = models.TextField(max_length=3000, help_text='Type Book Description Here')
    url = models.URLField(unique = True)
    date_added = models.DateField(auto_now_add= True)


    def __str__(self):
        """String for representing the Model object."""
        return self.title

    class Meta:
        ordering = ['-date_added']


class Category(models.Model):
    category_name = models.CharField(max_length=200, help_text="Enter the Book Category")
    url = models.URLField(unique = True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        """String for representing the Model object."""
        return self.category_name

            