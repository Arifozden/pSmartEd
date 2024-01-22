from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True,verbose_name='Course Name', help_text='Enter the course name')
    description = models.TextField(blank=True,null=True,verbose_name='Description', help_text='Enter the course description')
    image = models.ImageField(upload_to='courses/%Y/%m/%d/',verbose_name='Image', help_text='Upload the course image', default='courses/default.jpg')
    date= models.DateTimeField(auto_now=True,verbose_name='Date', help_text='Enter the date of the course')
    availabe = models.BooleanField(default=True,verbose_name='Available', help_text='Check if the course is available')

    def __str__(self):
        return self.name