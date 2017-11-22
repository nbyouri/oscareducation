# coding=utf-8
from django import forms

DOMAIN_CHOICES = (('Integer', 'Entiers'), ('Rational', 'Rationnels'))
IMAGE_CHOICES = (('Rational', 'Rationnels'), ('Complex', 'Complexes'), ('Integer', 'Entiers'))

GENERATOR_CHOICE = (("ArithmeticProblem", "Equation du second degrée"),
                    ("SimpleInterestProblem", "Problème d'intêret"),
                    ("StatisticsProblem", "Problème de statistiques"),
                    ("VolumeProblem", "Problèmes de volumes"))


class GeneratorChoiceForm(forms.Form):
    generator_name = forms.ChoiceField(widget=forms.Select, choices=GENERATOR_CHOICE, label='Nom du générateur')


class ArithmeticForm(GeneratorChoiceForm):
    range_from = forms.FloatField(widget=forms.TextInput, required=True, label='Interval inférieur')
    range_to = forms.FloatField(widget=forms.TextInput, required=True, label='Interval supérieur')
    domain = forms.ChoiceField(widget=forms.Select, choices=DOMAIN_CHOICES, label='Domaine')
    image = forms.ChoiceField(widget=forms.Select, choices=IMAGE_CHOICES, label='Image')

    def clean(self):
        cleaned_data = super(ArithmeticForm, self).clean()
        range_from = cleaned_data.get("range_from")
        range_to = cleaned_data.get("range_to")

        # Checking instance to avoid problem with 0 values
        if isinstance(range_from, float) and isinstance(range_to, float):
            if range_from >= range_to:
                msg = "L'interval inférieur ne peut pas être plus grand ou égal au supérieur."
                self.add_error('range_from', msg)
            if (range_to - range_from) < 5:
                msg = "Fournissez un interval de valeurs supérieur ou égal à 5"
                self.add_error('range_from', msg)


class SimpleInterestForm(GeneratorChoiceForm):
    TIME_CHOICES = (('year', 'Années'), ('month', 'Mois'))

    time_placed = forms.ChoiceField(widget=forms.Select, choices=TIME_CHOICES, label='Temps de placement')
    type_rate = forms.ChoiceField(widget=forms.Select, choices=TIME_CHOICES, label='Ratio appliqué par')


class StatisticsForm(GeneratorChoiceForm):
    range_from = forms.FloatField(widget=forms.TextInput, required=True, label='Interval inférieur des valeurs')
    range_to = forms.FloatField(widget=forms.TextInput, required=True, label='Interval supérieur des valeurs')
    nb = forms.IntegerField(widget=forms.TextInput, required=True, label='Nombre d''éléments')

    def clean(self):
        cleaned_data = super(StatisticsForm, self).clean()
        range_from = cleaned_data.get("range_from")
        range_to = cleaned_data.get("range_to")
        nb = cleaned_data.get("nb")
        if isinstance(range_from, float) and isinstance(range_to, float) and isinstance(nb, int):
            if range_from >= range_to:
                msg = "L'interval inférieur ne peut pas être plus grand ou égal au supérieur."
                self.add_error('range_from', msg)
            if (range_to - range_from) < 1:
                msg = "Fournissez un interval de valeurs supérieur ou égal à 1"
                self.add_error('range_from', msg)
            if (nb < 5):
                msg = "Le nombre d''élément doit être au minimum de 5"
                self.add_error('nb', msg)


class VolumeProblemForm(GeneratorChoiceForm):
    OBJECT_TYPE = (('cylinder', 'Cylindre'),
                   ('pyramid', 'Pyramide'),
                   ('cone', 'Cône'),
                   ('prism', 'Prisme'),
                   ('cube', 'Cube'))

    object_type = forms.ChoiceField(widget=forms.Select, choices=OBJECT_TYPE, label='Figure')
    range_from = forms.FloatField(widget=forms.TextInput, required=True, label='Interval inférieur')
    range_to = forms.FloatField(widget=forms.TextInput, required=True, label='Interval supérieur')

    def clean(self):
        cleaned_data = super(VolumeProblemForm, self).clean()
        range_from = cleaned_data.get("range_from")
        range_to = cleaned_data.get("range_to")
        if isinstance(range_from, float) and isinstance(range_to, float):
            if range_from <= 0 or range_to <= 0:
                msg = "Les valeurs doivent être plus grandes que 0."
                self.add_error('range_from', msg)
            if range_from >= range_to:
                msg = "L'interval inférieur ne peut pas être plus grand ou égal au supérieur."
                self.add_error('range_from', msg)
            if (range_to - range_from) < 1:
                msg = "Fournissez un interval de valeurs supérieur ou égal à 1"
                self.add_error('range_from', msg)
