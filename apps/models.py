from django.db import models

# Create your models here.
city = [
    ('k', 'Kathmandu'),
    ('p', 'Pokhara'),
    ('b', 'butwal'),
    ('d', 'dharan'),
    ('i', 'illam')
]


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(choices=city, max_length=20)
    phone_no = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
