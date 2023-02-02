from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.http import HttpResponse
from django.shortcuts import render

from forms_2_2023.web.validators import validate_text, validate_priority, ValueInRangeValidator


class ToDoForm(forms.Form):
    text = forms.CharField(
        validators=(
            validate_text,
        ),
    )
    is_done = forms.BooleanField(
        required=False,
    )
    priority = forms.IntegerField(
        validators=(
            validate_priority,
            MinValueValidator(1),
            ValueInRangeValidator(1, 10),
        ),
    )

    def clean_text(self):
        pass

    def clean_priority(self):
        raise ValidationError('Error?!!!!!')

    def clean_is_done(self):
        pass



def index(request):
    if request.method == 'GET':
        form = ToDoForm()
    else:
        form = ToDoForm(request.POST)
        if form.is_valid():
            return HttpResponse('all is valid')
    context = {
        'form':form,
    }
    return render(request, 'index.html', context)
