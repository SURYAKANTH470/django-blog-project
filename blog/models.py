from django.db import models
from django.utils import timezone  # ✅ Add this

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)  # ✅ Default added
