from django.db import models

class admit_card(models.Model):
    name = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    sign_image = models.ImageField(upload_to='sign_images/', null=True, blank=True)
    date_of_birth = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    def __str__(self):
        return self.email