from django import forms
from django.db.models import fields
from .models import NotionModel
from django.forms import ModelForm, widgets

class NotionForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(NotionForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['about'].required = False
    
    class Meta:
        model = NotionModel 
        fields = ('aim', 'about', 'impt', 'comp')   
        widgets = {
            'aim':widgets.TextInput(attrs={
                'class':'form-control',
                'aria-describedby':'button-addon1',
                "aria-label":"Example text with button addon"  
            }),
            'about':widgets.Textarea(attrs={
                'class':"form-control",
                'id':"floatingTextarea2",
                'style':"height: 100px",
                'placeholder':"Leave a comment here"
            }),
            'impt':widgets.CheckboxInput(attrs={
                'class':"form-check-input",
                'id':"flexCheckDefault",
            })
        }