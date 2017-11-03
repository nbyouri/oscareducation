from django import forms


class ProblemForm(forms.Form):

    def __init__(self):
        super(ProblemForm, self).__init__()
        domain_choices = (('Natural', 'Naturels'), ('Integer', 'Entiers'), ('Rational', 'Rationnels'))
        self.domain = forms.ChoiceField(widget=forms.Select, domain=domain_choices)
        image_choices = (('Natural', 'Naturels'), ('Rational', 'Rationnels'))
        self.image = forms.ChoiceField(widget=forms.Select, image=image_choices)

