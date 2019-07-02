from django import forms

from leaflet.forms.widgets import LeafletWidget

class LocationForm(forms.ModelForm):
    title = forms.CharField(max_length=256)
    description = forms.TextField()
    type = forms.CharField(max_length=16)

    def __unicode__(self):
        return self.title

    class Meta:
        model = Location
        fields = ('title', 'description', 'type', 'geom')
        widgets = ('geom': LeafletWidget())