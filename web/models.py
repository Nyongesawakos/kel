from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    firstname=models.CharField(max_length=255)
    Lastname=models.CharField(max_length=255)
    description =models.TextField(null=True, blank=True)

class tips(models.Model):
    name=models.CharField(max_length=200)  
    description=models.TextField(null=True, blank=True)

class topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name 
class cash_expenditure(models.Model):
    name =models.CharField(max_length=100)
    date =models.DateField(max_length=20)
    Amount=models.CharField(max_length=45)
    updated=models.DateTimeField(auto_now=True, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    class Meta:
     ordering = ['-updated', '-created']

    def __str__(self):
      return self.Amount or ""



class room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic=models.ForeignKey(topic, on_delete=models.SET_NULL, null=True) 
    cash_expenditure=models.ForeignKey(cash_expenditure, on_delete=models.SET_NULL, null=True)
    Firstname = models.CharField(null=True, blank=True, max_length=200)
    name=models.CharField(max_length=255)
    lastName = models.CharField(null=True, blank=True, max_length=200)
    Email = models.EmailField(null=True, blank=True, max_length=200)
    phone = models.CharField(null=True, blank=True, max_length=200)
    identity= models.CharField(null=True, blank=True, max_length=255)
    description=models.TextField(null=True, blank=True)
    amount=models.IntegerField(max_length=10, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
     return self.identity if self.identity is not None else "Unnamed"
    
class message(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE) 
    room=models.ForeignKey(room, on_delete=models.CASCADE) 
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    

    class Meta:
          ordering = ['-updated', '-created']

    def __str__(self):
     return self.body or ""

    

class Msg(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE)
    room=models.ForeignKey(room, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True ,max_length=100)
    updated= models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
          ordering = ['-updated', '-created']

    def __str__(self):
     return self.body or ""

    
    
class update(models.Model):
        owner= models.ForeignKey(User,on_delete=models.CASCADE)
        room=models.ForeignKey(room,on_delete=models.CASCADE)
        instalment=models.CharField(null=True,blank=True,max_length=255)
        welfare_ded=models.CharField(null=True,blank=True,max_length=255)
        kitty=models.CharField(null=True,blank=True,max_length=255)
        bbf=models.CharField(null=True,blank=True,max_length=255)
        current_loan=models.CharField(null=True,blank=True,max_length=255)
        total_loan=models.CharField(null=True,blank=True,max_length=255)
        interest=models.CharField(null=True,blank=True,max_length=255)
        deductable=models.CharField(null=True,blank=True,max_length=255)
        Total_deductions = models.DecimalField(max_digits=10, decimal_places=1)
        #month = models.CharField(null=True, blank=True, max_length=100)
        select= 'Select' 
        JANUARY = 'JANUARY'  
        FEBRUARY = 'FEBRUARY'  
        MARCH = 'MARCH'
        APRIL= 'APRIL'
        MAY = 'MAY'
        JUNE = 'JUNE'
        JULY = 'JULY'
        AUGUST = 'AUGUST'
        SEPTEMBER = 'SEPTEMBER'
        OCTOBER = 'OCTOBER'
        NOVEMBER = 'NOVEMBER'
        DECEMBER = 'DECEMBER'

        CHOICES = [
        (select,'select'),
        (JANUARY,'January'),
        (FEBRUARY,'February'),
        (MARCH,'March'),
        (APRIL ,'April'),
        (MAY ,'May'),
        (JUNE ,'June'),
        (JULY  ,'July'),
        (AUGUST, 'August'),
        (SEPTEMBER ,'September'),
        (OCTOBER ,'October'),
        (NOVEMBER ,'November'),
        (DECEMBER ,'December'),

    ]
        month = models.CharField(null=True, blank=True, max_length=100)  
        choice = models.CharField(  
        max_length=100,  
        choices=CHOICES,  
        default=select,  
    )
        updated=models.DateTimeField(auto_now=True)
        created=models.DateTimeField(auto_now_add=True)

        class Meta:
          ordering = ['-updated', '-created']

        def __str__(self):
          return self.choice if self.choice is not None else "Unnamed"



        

    

    

   
        




  
    






