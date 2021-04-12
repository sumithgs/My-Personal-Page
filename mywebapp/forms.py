from django import forms
from .models import Certificates, Projects


class ProjectForm(forms.ModelForm):
    image = forms.FileField(required=False)

    class Meta():
        model = Projects
        fields = '__all__'
        """
        widgets = {
            'title': forms.TextInput(attrs={'class': 'titlefield'}),
            'description': forms.Textarea(attrs={'class': 'descriptionfield'}),
            'create_date': forms.TextInput(attrs={'class': 'create_datefield'}),

        }"""


class CertificatesForm(forms.ModelForm):
    images = forms.FileField(required=False)

    class Meta():
        model = Certificates
        fields = '__all__'
