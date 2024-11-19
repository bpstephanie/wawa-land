from django.db import models
from django.contrib.auth.models import User


AGES = (
    (0, "newborns"),
    (1, "0-12 months"),
    (2, "2-3 years"),
    (3, "4-5 years"),
    (4, "5-8 years"),
    (5, "8-12 years"),
    (6, "13+"),
    (7, "All ages")
)


# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    event_about = models.TextField()
    age_range = models.IntegerField(choices=AGES, default=0)
    event_location = models.CharField(max_length=200, null=True)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ["-event_date"]

    def __str__(self):
        return self.title


# Review Model
class Review(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="reviews")
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.author}"
