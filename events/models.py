from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField('Vemue Name', max_length=250)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=120)
    phone = models.CharField('Contaact Phone', max_length=250)
    web = models.URLField('Website')
    email_address = models.EmailField('Email')
    
    def __str__(self):
        return self.name
    
class MyclubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
        



class Events(models.Model):
    name = models.CharField('Events Name', max_length=250)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyclubUser, blank=True)
    
    def __str__(self):
        return self.name
