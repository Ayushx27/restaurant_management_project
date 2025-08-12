from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
        description = models.TextField()
            phone_number = models.CharField(max_length=20, default="(555) 123-4567")
                
                    def __str__(self):
                            return self.name