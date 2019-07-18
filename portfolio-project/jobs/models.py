from django.db import models

# Create your models here.
class HelloWorld(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length=30)
'''
    def validate_mac_helloworld(self):
        if len(self.summary) <= 30:
            return self.summary.upper()
        else:
            return self.summary
'''
