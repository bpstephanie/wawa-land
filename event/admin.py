from django.contrib import admin
from .models import Event, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'age_range')
    search_fields = ['title', 'age_range']
    list_filter = ('age_range',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('event_about',)

# Register your models here.
admin.site.register(Review)