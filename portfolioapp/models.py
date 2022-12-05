from django.db import models



class Projects(models.Model):
    title = models.CharField(max_length=180)
    comment = models.TextField(max_length=300, blank=True)
    image = models.ImageField(upload_to='portfolioapp/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
