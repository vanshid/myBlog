from django import forms
from .models import ConnectModel

# creating a form 
class ContactMe(forms.Form):

    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    email = forms.EmailField(max_length=200)

class ConnectForm(forms.ModelForm):
    
    class Meta:
        model = ConnectModel
        fields = "__all__"
