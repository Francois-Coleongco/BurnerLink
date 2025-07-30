from django.db import models
import secrets

MAX_SLUG_LENGTH=20

class BurnerLink(models.Model):
    message = models.TextField(default="")
    slug = models.CharField(max_length=MAX_SLUG_LENGTH, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_one_time = models.BooleanField(default=True)
    visits = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = secrets.token_urlsafe(6)[:MAX_SLUG_LENGTH]
        super().save(*args, *kwargs)
