from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200, default="Better IT Partner For Your Business")
    description = models.TextField(default="We are team of experienced developers and designers working on different area")
    image = models.ImageField(upload_to='heroes/', blank=True, null=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)

    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_date = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact from {self.name}"

class Career(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title