from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import loan_offer


class offer_form(forms.ModelForm):
    class Meta:
        model = loan_offer
        fields = '__all__'


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **krwargs):
        super(SignupForm, self).__init__(*args, **krwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'USERNAME'
        self.fields['username'].help_text = '<div class="form_text text-muted"><small>Required. 150 characters or ' \
                                            'fewer.Letters,digits and @/./+/-/_ only.</small></div> '

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'PASSWORD'
        self.fields['password1'].help_text = '<div class="form-text text-muted"><small><ul><li>Your password ' \
                                             'can&#39;t be too similar to your other personal ' \
                                             'information.</li><li>Your password must contain at least 8 ' \
                                             'characters.</li><li>Your password can&#39;t be a commonly used ' \
                                             'password.</li><li>Your password can&#39;t be entirely ' \
                                             'numeric.</li></ul></small></div> '

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = 'RETYPE PASSWORD'
        self.fields['password2'].help_text = '<div class="form-text text-muted"><small>Enter the same password as ' \
                                             'before, ' \
                                             'for verification.</small></div> '


class UserUpdateForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
