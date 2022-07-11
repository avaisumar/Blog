from .models import Post
from django.forms import ModelForm


class postform(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'