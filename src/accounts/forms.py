from django import  forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()  # email field added
#
#     class Meta:
#         model: User
#         fields = ['username', 'email', 'password1', 'password2']


class UserRegisterForm(UserCreationForm):
    # Custom email field for registration
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    # These lines of code are used to give all Login form's fields a class
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    # User model's form fields

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )

    # Email validation for registration
    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')


class UserLoginForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'password1', )
