from django import forms
from .models import Activity

class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = ('title', 'text', 'assigned_to', 'deadline')
        #fields = ('deadline',)
        #widgets = {'deadline': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm:ss", "pickTime": True}),}
