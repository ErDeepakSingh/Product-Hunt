from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=255)
    url=models.URLField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)
    votes_total=models.IntegerField(default=1)
    image=models.ImageField(default='image.png',upload_to="images")
    icon=models.ImageField(default='icon.jpg',upload_to="icons")
    body=models.TextField(max_length=400)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)


    def summary(self):
        return self.body[:100]
    def publish_date(self):
        return self.pub_date.strftime('%b %e, %Y')
    def __str__(self):
        return self.title
