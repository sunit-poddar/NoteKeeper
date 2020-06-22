# django imports
from django.db import models
from slugify import slugify
from django.contrib.auth.models import User

# app imports
from note_utils.model_utils import RowInformation


class Note(RowInformation):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=256, null=False, blank=False)
    text = models.TextField(help_text="Put in your notes here")
    is_public = models.BooleanField(default=False)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Notes"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)
