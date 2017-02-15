from django import forms
from django.core.exceptions import ValidationError

from .models import User, Company


class UserForm(forms.ModelForm):
    confirm_email = forms.EmailField(
        label="Confirm email",
        required=True,
    )

    class Meta:
        model = User
        fields = "__all__"
        exclude =[]
    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email

        return super(UserForm, self).__init__(*args, **kwargs)

    def clean(self):

        if (self.cleaned_data.get('email') !=
                self.cleaned_data.get('confirm_email')):
            raise ValidationError(
                "Email addresses must match."
            )

        return self.cleaned_data

class CompanyForm(forms.ModelForm):
    confirm_email = forms.EmailField(
        label="Confirm email",
        required=True,
    )

    class Meta:
        model = Company
        fields = "__all__"
        exclude =[]
    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email

        return super(CompanyForm, self).__init__(*args, **kwargs)

    def clean(self):

        if (self.cleaned_data.get('email') !=
                self.cleaned_data.get('confirm_email')):
            raise ValidationError(
                "Email addresses must match."
            )

        return self.cleaned_data
