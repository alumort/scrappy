from django.db import models
from django.core.validators import MinValueValidator

class ScrapedItem(models.Model):
    source = models.URLField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BookCategory(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

class Book(models.Model):
    book_title = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    category = models.ForeignKey(BookCategory, on_delete=models.PROTECT)

class BookSnapshot(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    price = models.DecimalField(validators=[MinValueValidator(1)], max_digits=10, decimal_places=2)
    in_stock = models.BooleanField()
    scraped_at = models.DateTimeField(auto_now_add=True)