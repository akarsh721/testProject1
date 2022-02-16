from django.db import models

# GENDER_CHOICES = (
#    ('M', 'Male'),
#    ('F', 'Female'),
#    ('O','Other')
   
# )

# Create your models here.
class RegisterUser(models.Model):

   firstName = models.CharField(max_length=20)
   lastName = models.CharField(max_length=20)
   username = models.CharField(max_length=30)
   password = models.CharField(max_length=20)
   cnfpswd = models.CharField(max_length=20)
   country = models.CharField(max_length=20)
   age = models.PositiveIntegerField(null=True)
   contact = models.PositiveBigIntegerField(null=True, blank=True)
   gender = models.CharField(max_length=11)
   profile = models.ImageField(upload_to='ProfileImages',null=True,blank=True)
   

   def __str__(self) -> str:
       return self.firstName 

class userQuestion(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    fileupload = models.FileField(upload_to='UploadedFile',null=True,blank=True)
    description = models.TextField()
    queriedBy = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title