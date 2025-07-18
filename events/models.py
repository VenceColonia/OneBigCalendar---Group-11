from django.db import models

class EventCard(models.Model):
    TAG_CHOICES = [
        ('LIONS', 'LIONS'),
        ('COA', 'COA'),
    ]

    TYPE_CHOICES = [
        ('Talk', 'Talk'),
        ('Concert', 'Concert'),
        ('Conference', 'Conference'),
        ('Party', 'Party'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    tag = models.CharField(max_length=10, choices=TAG_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True)
    created_at = models.DateTimeField("Event Date and Time")
    hosted_by = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.title

# Create your models here.
