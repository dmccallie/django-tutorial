# testing forms

from django import forms

class TestForm(forms.Form):
    
    name = forms.CharField(label="Your name", max_length=100)
    
    email = forms.EmailField(label="Your email", max_length=100)
    
    message = forms.CharField(label="Your message", widget=forms.TextInput(
        attrs={"size": "40", "placeholder": "Enter your message here", 
               "class": "border-4"}), 
    )
    cc_myself = forms.BooleanField(label="CC yourself", required=False,
                widget=forms.CheckboxInput(attrs={"class": "rounded text-pink-500"}))
    
    age = forms.IntegerField(label="Your age", min_value=0, max_value=100,
                widget=forms.NumberInput(attrs={"type": "number", "class": "border-4 mr-2"}))
