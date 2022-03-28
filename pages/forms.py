from django import forms

from pages.models import AddNews


class AddNewsForm(forms.ModelForm):
    name = forms.CharField(label='Name*:', widget=forms.TextInput(attrs={'class': 'contact-form-text'}))
    title = forms.CharField(label='Title*:', widget=forms.TextInput(attrs={'class': 'contact-form-text'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-form-text'}),required=False)
    source = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-sc'}),required=False)
    description = forms.CharField(label='Description*:', widget=forms.Textarea(attrs={'class': 'contact-form-text'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-sc'}),required=False)

    class Meta:
        model = AddNews
        fields = ('name', 'email', 'title', 'source', 'category', 'description', 'image')
