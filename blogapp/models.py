from django.db import models



class Blogs(models.Model):
    blog_title = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title
