from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(max_length=254, blank=True, verbose_name='Name')
    description = models.CharField(max_length=254, blank=True, verbose_name='Description')
    parameter = models.CharField(max_length=254, blank=True, verbose_name='Parameter')

    def __str__(self):
        return f'General Setting: {self.name}'


class ImageSetting(AbstractModel):
    name = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Name'
    )
    description = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Description'
    )
    file = models.ImageField(
        upload_to='images/',
        blank=True,
        verbose_name='Image'
    )

    def __str__(self):
        return f'Image Setting: {self.name}'


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order'
    )
    name = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Name'
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self):
        return f'Skill: {self.name}'


class Experience(AbstractModel):
    company_name = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Company Name',
    )
    job_title = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Job Title',
    )
    job_location = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Job Location',
    )
    start_date = models.DateField(
        verbose_name='Start Date'
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date'
    )

    def __str__(self):
        return f'Experience: {self.company_name}'


class Education(AbstractModel):
    school_name = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='School Name',
    )
    major = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Major',
    )
    department = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Department',
    )
    start_date = models.DateField(
        verbose_name='Start Date'
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date'
    )

    def __str__(self):
        return f'Education: {self.school_name}'


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order'
    )
    link = models.URLField(
        max_length=254,
        blank=True,
        verbose_name='Link',
    )
    icon = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Icon',
    )

    def __str__(self):
        return f'SocialMedia: {self.link}'


class Document(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order'
    )
    slug = models.SlugField(
        max_length=254,
        blank=True,
        verbose_name='Slug',
    )
    button_text = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Button Text',
    )
    file = models.FileField(
        upload_to='documents/',
        blank=True,
        verbose_name='File',
    )

    def __str__(self):
        return f'Document: {self.slug}'
