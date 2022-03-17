from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Converter


class ConverterForm(forms.ModelForm):
    """ form for ckeditor text widget """
    body = forms.CharField(widget=CKEditorWidget, label='Text editor')
    class Meta:
        model = Converter
        fields = ('body', )
