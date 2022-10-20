from django.forms import ModelForm
from .models import Maintain

class MaintainForm(ModelForm):
    class Meta:
        model = Maintain
        fields = ['date', 'service']