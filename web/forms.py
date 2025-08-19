from django import forms
from django.forms import ModelForm
from .models import room
from .models import update,cash_expenditure, message, Msg
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError



class cash_expenditureForm(ModelForm):
    class Meta:
        model=cash_expenditure
        fields='__all__'
        exclude = ['host']
        
class RoomForm(ModelForm):
    class Meta:
        model=room
        fields='__all__'
        exclude = ['host']

class MsgForm(ModelForm):
    class Meta:
        model=Msg
        fields='__all__'
        exclude = ['host']

class MessageForm(ModelForm):
    class Meta:
        model=message
        fields='__all__'
        exclude = ['host']        



   
        
  

class UpdateForm(ModelForm):
    class Meta:
        model=update
        fields='__all__'


         

class CustomUserCreationForm(UserCreationForm): 
    username = forms.CharField(required=True)  
    email = forms.EmailField(required=True)  
   

    class Meta:  
        model = User  
        fields = ('username', 'email',  'password1', 'password2')

    def clean_username(self):  
        username = self.cleaned_data.get('username')  
        if User.objects.filter(username=username).exists():  
            raise ValidationError("This username is already taken.")  
        return username       