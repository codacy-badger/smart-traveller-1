from django.contrib.auth.forms  import UserCreationForm, UserChangeForm
from .models import CustomUser, Agent

class CustomUserCreationForm(UserCreationForm):
    """
    A form for registering new users with all required field.
    """
    class Meta:
        """
        Expose required fields.
        """
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating users with all required field.
    """
    class Meta:
        """
        Expose required fields.
        """
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class AgentCreationForm(UserCreationForm):
    """
    A form for registering new agent with all required field.
    """
    class Meta:
        """
        Expose required fields.
        """
        model = Agent
        fields = ('username', 'email', 'first_name', 'last_name')

class AgentChangeForm(UserChangeForm):
    """
    A form for updating agent with all required field.
    """
    class Meta:
        """
        Expose required fields.
        """
        model = Agent
        fields = UserChangeForm.Meta.fields
