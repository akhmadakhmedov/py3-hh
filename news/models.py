from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='article_new_object')
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)
    user_views = models.ManyToManyField(
        to=User,
        related_name="new_views",
        blank=True
    )
    #likes_users = models.ManyToManyField(
    #    to=User,
    #    null=True,
    #    blank=True
    #)

    def __str__(self):
        return self.title
class NewsViews(models.Model):
    user = models.ForeignKey(
         to=User,
         on_delete=models.CASCADE
     )
    new = models.ForeignKey(
         to=News,
         on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        unique_together = [['user', 'new']]

