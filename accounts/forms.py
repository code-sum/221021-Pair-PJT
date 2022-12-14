from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email')
        labels = {
      'username': '계정',
      'password1': '비밀번호',
      'password2': '비밀번호 확인',
      'email' : '이메일'
    }

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')