from django.db import models

class Agenda(models.Model):
    title = models.CharField(max_length=200, help_text="Enter agenda title (e.g., युवा सशक्तीकरण)")
    description = models.TextField(help_text="Enter a short description")
    title_en = models.CharField(max_length=200, verbose_name="Title (English)", blank=True, null=True)
    description_en = models.TextField(verbose_name="Description (English)", blank=True, null=True)

    def __str__(self):
        return self.title



class Program(models.Model):
    title = models.CharField(max_length=200, help_text="Example: Teej Program")
    image = models.ImageField(upload_to='programs/', help_text="Upload program photo")
    date = models.DateField()
    location = models.CharField(max_length=255)
    guests = models.CharField(max_length=255, help_text="Main guests of the event")
    description = models.TextField(help_text="What was done in the program?")
    
    title_en = models.CharField(max_length=200, verbose_name="Title (English)", blank=True, null=True)
    location_en = models.CharField(max_length=255, verbose_name="Location (English)", blank=True, null=True)
    guests_en = models.CharField(max_length=255, verbose_name="Guests (English)", blank=True, null=True)
    description_en = models.TextField(verbose_name="Description (English)", blank=True, null=True)
    
    photo_1 = models.ImageField(upload_to='programs/gallery/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='programs/gallery/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='programs/gallery/', blank=True, null=True)

    # --- Gallery: 3 Video Files ---
    video_1 = models.FileField(upload_to='programs/videos/', blank=True, null=True)
    video_2 = models.FileField(upload_to='programs/videos/', blank=True, null=True)
    video_3 = models.FileField(upload_to='programs/videos/', blank=True, null=True)

    def __str__(self):
        return self.title

class CoverPage(models.Model):
    image=models.ImageField(upload_to='cover_pages/',help_text="Upload_cover_page_photo")
    def __str__(self):
        return self.image.name
    


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team_photos/')
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True) # Fixed typo here
    
    name_en = models.CharField(max_length=255, verbose_name="Name (English)", blank=True, null=True)
    position_en = models.CharField(max_length=200, verbose_name="Position (English)", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.position})"

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"


# talennt model

from django.db import models

class Talent(models.Model):
    # Name fields
    name_ne = models.CharField(max_length=200, verbose_name="Name (Nepali)")
    name_en = models.CharField(max_length=200, verbose_name="Name (English)")
    
    # Description fields
    description_ne = models.TextField(verbose_name="Description (Nepali)")
    description_en = models.TextField(verbose_name="Description (English)")
    
    video_file = models.FileField(
        upload_to='talents/videos/', 
        null=True, 
        blank=True, 
        help_text="Upload a video file from your gallery"
    )
    # Optional Thumbnail/Image
    thumbnail = models.ImageField(upload_to='talents/thumbnails/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = "Talent"
        verbose_name_plural = "Talents"
        

#social media links model
class FooterSettings(models.Model):
    # Contact Info
    phone = models.CharField(max_length=20, default="+977 ")
    email = models.EmailField(default="info@empoweredyouth.org")
    address_ne = models.CharField(max_length=255, verbose_name="Address (Nepali)")
    address_en = models.CharField(max_length=255, verbose_name="Address (English)")

    # Social Links
    facebook_url = models.URLField(blank=True, null=True)
    tiktok_url = models.URLField(blank=True, null=True)
    
    # Map
    google_maps_embed_url = models.TextField(
        help_text="Paste the 'src' attribute from the Google Maps embed iframe code."
    )

    class Meta:
        verbose_name = "Footer Setting"
        verbose_name_plural = "Footer Settings"

    def __str__(self):
        return "Global Footer Contact & Links"