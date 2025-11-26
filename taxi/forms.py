from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver, Car


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number", )

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        if not license_number:
            raise ValidationError("Required field")
        if len(license_number) != 8:
            raise ValidationError("Input 8 symbols")
        if (not license_number[:3].isalpha()
                or not license_number[:3].isupper()):
            raise ValidationError("Input 3 letters")
        if not license_number[3:].isdigit():
            raise ValidationError("Input 8 digits")
        return license_number


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        if not license_number:
            raise ValidationError("Required field")
        if len(license_number) != 8:
            raise ValidationError("Input 8 symbols")
        if (not license_number[:3].isalpha()
                or not license_number[:3].isupper()):
            raise ValidationError("Input 3 letters")
        if not license_number[3:].isdigit():
            raise ValidationError("Input 8 digits")
        return license_number


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
