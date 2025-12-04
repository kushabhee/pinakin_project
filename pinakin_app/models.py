from django.db import models

class TimeStampedModel(models.Model):
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('published', 'Published'),
        ],
        default='published',
        help_text="Draft = Hidden from website, Published = Visible"
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Automatically set when created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Automatically updates on every save")

    class Meta:
        abstract = True


class HeroSection(TimeStampedModel):
    title = models.CharField(max_length=200, default="Better IT Partner For Your Business")
    description = models.TextField(default="We are team of experienced developers and designers working on different area")
    image = models.ImageField(upload_to='heroes/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hero Section"


class Service(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)

    def __str__(self):
        return self.name


class PortfolioItem(TimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name


class TeamMember(TimeStampedModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact from {self.name}"


class Career(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title