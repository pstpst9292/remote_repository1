from django import forms
class Feedback1Form(forms.Form):
    Name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    Rating=forms.IntegerField(
        label='Enter Your Rating',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating'
            }
        )
    )
    Mobile=forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Number'
            }
        )
    )
    Email=forms.EmailField(
        label='Enter Mail ID',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mail'
            }
        )
    )
    Feedback=forms.CharField(
        label='Enter Feedback',
        widget=forms.Textarea(
            {
                'class': 'form-control',
                'placeholder': 'Your Feedback'
            }
        )
    )