from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as maps_models

class ObjectAdmin(LeafletGeoAdmin):
    list_display = ('id', 'title', 'type', 'description')
    empty_value_display = '-nevypln&ecaron;no-'
    list_display_links = ('title', 'id')
    search_fields = ['id', 'title', 'type']

admin.site.register(maps_models.ObjectSpot, ObjectAdmin)
admin.site.register(maps_models.ObjectPoint, ObjectAdmin)


