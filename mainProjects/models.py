from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

from django.db.models.fields import FloatField

class Project(models.Model):
    email = models.EmailField(max_length=254)
    title = models.CharField( max_length= 70)
    desc = models.CharField(max_length=700,blank=True,null=True)
    enroll_no = models.IntegerField()
    year = models.CharField( max_length=1)
    sec = models.CharField( max_length=1)
    git_link = models.CharField(max_length=70)
    live_link = models.CharField(max_length=70,blank=True,null=True)
    screenshot = models.ImageField( upload_to="projects/images",blank=True,null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_on = models.DateField(auto_now_add=True)
    updated_on =models.DateField(auto_now=True)
    
    

    def __str__(self):
        return self.title + " | " + str(self.submitted_by)

    class Meta:
        managed = True
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        
        
        
        
        
class Remarks(models.Model):
    rating = models.FloatField()
    remarks = models.CharField( max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project , related_name="projects" , on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.project.title + " | " + str(self.author)

    class Meta:
        verbose_name = 'Remarks'
        verbose_name_plural = 'Remarks'
        
class Contact(models.Model):
    favmovie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    PhoneNo = models.IntegerField()
    Email = models.CharField(max_length=50,default="")
    Descriptionn = models.CharField(max_length=50,default="")
    pub_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name
    