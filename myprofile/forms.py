from django.forms import ModelForm
from .models import Worker
from django.contrib.auth.models import User
from django import forms



class WorkerForm(ModelForm):
    userKey = forms.ModelChoiceField(queryset=Worker.objects,empty_label=None)
    class Meta:
        model = Worker
        fields =['firstName', 'lastName', 'userKey','userId','password']
        # exclude = ('userKey',)
    def __init__(self, username, *args, **kwargs):
        super(WorkerForm, self).__init__(*args, **kwargs)
        self.fields['userKey'].queryset = User.objects.filter(username=username)
