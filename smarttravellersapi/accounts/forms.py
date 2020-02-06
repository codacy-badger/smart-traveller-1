from django.contrib.auth.forms  import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    A form for registering new users with all required field
    """
    class Meta:
        """"""
        model = CustomUser
        fields = ('username', 'email', 'firstname', 'lastname')

class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating users with all required field
    """
    class Meta:
        """"""
        model = CustomUser
        fields = UserChangeForm.Meta.fields
