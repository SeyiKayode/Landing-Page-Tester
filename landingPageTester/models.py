from django.db import models

# Create your models here.
class Traffic(models.Model):
    page_url = models.URLField(max_length=300)
    stats = models.IntegerField()

    def __str__(self):
        return '%s %s' % ('Page URL:', self.page_url)


