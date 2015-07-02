from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from . import forms
from .lib import integer_to_roman


def home(request, integer=None):
    """
    Renders a form that can convert integers into roman numbers.
    """
    form = forms.IntegerToRomanForm(request.POST or None)

    if request.POST and form.is_valid():
        return redirect(home, form.cleaned_data['integer'])

    numeral = integer_to_roman(int(integer)) if integer is not None else None
    return render_to_response('home.html', RequestContext(request, {
        'form': form,
        'integer': integer,
        'numeral': numeral
    }))
