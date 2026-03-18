from django.contrib import admin

# Register your models here.
from django.contrib import admin
from sonapur.models import Agenda,Program,TeamMember,CoverPage,Talent
from django.utils.html import format_html

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_en')
    fieldsets = (
        ('नेपाली सामग्री (Nepali)', {
            'fields': ('title', 'description'),
        }),
        ('English Content', {
            'fields': ('title_en', 'description_en'),
        }),
    )

from django.contrib import admin
from .models import Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'title_en', 'date', 'location', 'location_en', 'image')
        }),
        ('Description & Guests', {
            # Removed 'full_details' and 'full_details_en' 
            # Replaced strictly with the fields from your models.py
            'fields': ('guests', 'guests_en', 'description', 'description_en')
        }),
        ('Photo Gallery', {
            'fields': ('photo_1', 'photo_2', 'photo_3'),
        }),
        ('Video Gallery', {
            'fields': ('video_1', 'video_2', 'video_3'),
        }),
    )
    
    # These columns appear in the list view of the admin panel
    list_display = ('title', 'date', 'location')
    
    # Optional: Adds a search bar and filters to your admin panel
    search_fields = ('title', 'location')
    list_filter = ('date',)

@admin.register(CoverPage)
class CoverPageAdmin(admin.ModelAdmin):
    # This shows the image filename and a small preview in the list
    list_display = ('image', 'thumbnail_preview')

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto; border-radius: 5px;" />', obj.image.url)
        return "No Image"

    thumbnail_preview.short_description = 'Preview'
    
    
#team member admin

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'contact_number', 'email')
    search_fields = ('name', 'position', 'email')
    list_filter = ('position',)
    
    fieldsets = (
        ('General Info', {
            'fields': ('image', 'contact_number', 'email')
        }),
        ('नेपाली विवरण (Nepali)', {
            'fields': ('name', 'position')
        }),
        ('English Details', {
            'fields': ('name_en', 'position_en')
        }),
    )


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name_en', 'name_ne', 'created_at')
    
    # Fields to search in the admin
    search_fields = ('name_en', 'name_ne', 'description_en', 'description_ne')
    
    # Filters on the right sidebar
    list_filter = ('created_at',)

    # Organizing the detail/edit form
    fieldsets = (
        ("Basic Information", {
            'fields': ('name_ne', 'name_en', 'description_ne', 'description_en')
        }),
        ("Media Uploads", {
            'fields': ('video_file', 'thumbnail'),
            'description': "Upload the talent's video and an optional cover image."
        }),
    )
    

#footer admin 
from django.contrib import admin
from .models import FooterSettings

@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    # Limits the admin to only one instance of FooterSettings
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    fieldsets = (
        ('Contact Information', {
            'fields': ('phone', 'email', 'address_ne', 'address_en')
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'tiktok_url')
        }),
        ('Location Map', {
            'fields': ('google_maps_embed_url',)
        }),
    )