from django.db import models

# Create your models here.

class Mode(models.Model):
    mode_id = models.CharField(max_length=10, unique=True )
    led = models.CharField(max_length=3)
    servo_1 = models.IntegerField(default=0,null=True)
    servo_2 = models.IntegerField(default=0,null=True)
    servo_3 = models.IntegerField(default=0,null=True)
    servo_4 = models.IntegerField(default=0,null=True)


    def __str__(self):
        return f"{self.mode_id}"
    