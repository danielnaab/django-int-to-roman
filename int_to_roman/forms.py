from django import forms
from django.utils.translation import ugettext as _


class IntegerToRomanForm(forms.Form):
    integer = forms.IntegerField(
        label=_('Integer to Convert'),
        min_value=1,
        max_value=3999,
        required=True
    )
