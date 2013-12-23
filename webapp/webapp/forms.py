from django import forms
import random
import string

from models import License, UserLicense


class GetStartedForm(forms.Form):
    license = forms.ModelChoiceField(queryset=License.objects.all(), empty_label="Choose type")


class BaseLicenseForm(forms.Form):
    """
    Basic License Creation Form
    will be used for most of the licenses
    """

    year = forms.DateField()
    author = forms.CharField(max_length=500)


class OrgLicenseForm(BaseLicenseForm):
    """
    Form for licenses with organisations parameter
    """

    organisation = forms.CharField(max_length=500)


class UserLicenseForm(forms.ModelForm):
    """
    license creation form
    """

    class Meta:
        model = UserLicense
        fields = ['license_type', 'author', 'year', 'organisation']

    def save(self):
        char_set = string.ascii_lowercase + string.digits
        su = ''.join(random.sample(char_set * 6, 6))

        try:
            while True:
                UserLicense.objects.get(short_url=su)
                su = ''.join(random.sample(char_set * 6, 6))
        except UserLicense.DoesNotExist:
            self.short_url = su

        super(UserLicenseForm, self).save()