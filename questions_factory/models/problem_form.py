from django import forms

DOMAIN_CHOICES = (('Natural', 'Naturels'), ('Integer', 'Entiers'), ('Rational', 'Rationnels'))
IMAGE_CHOICES = (('Rational', 'Rationnels'), ('Complex', 'Complexes'), ('Integer', 'Entiers'))


class ProblemForm(forms.Form):
    domain = forms.ChoiceField(widget=forms.Select, choices=DOMAIN_CHOICES)
    image = forms.ChoiceField(widget=forms.Select, choices=IMAGE_CHOICES)


class ArithmeticForm(ProblemForm):
    range_from = forms.FloatField(widget=forms.TextInput, required=True)
    range_to = forms.FloatField(widget=forms.TextInput, required=True)
