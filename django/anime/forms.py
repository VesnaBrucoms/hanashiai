from django import forms


class SearchForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['query'].widget.attrs['class'] = 'form-control'

    query = forms.CharField(max_length=256)
