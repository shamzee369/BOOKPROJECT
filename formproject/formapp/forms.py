from django import forms

from.models import book,author



class authorform(forms.ModelForm):
    class Meta:
        model=author

        fields=['name']

class bookform(forms.ModelForm):
    class Meta:
        model=book

        fields='__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the bookname'}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':'Enter the authorname'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the price'})


                                            }