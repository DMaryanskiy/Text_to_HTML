from django.shortcuts import render

from .forms import ConverterForm


def index(request):
    """ main view function for ckeditor text widget """
    form = ConverterForm()
    return render(request, 'index.html', {'form': form})
