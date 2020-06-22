# django imports
from django.db import models
from slugify import slugify
from django.contrib.auth.models import User
import secrets

# third party imports
from markdownx.models import MarkdownxField

# app imports
from note_utils.model_utils import RowInformation


class Note(RowInformation):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=256, null=False, blank=False)
    text = MarkdownxField()
    is_public = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Notes"

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = "{}-{}".format(slugify(self.title), secrets.token_hex(4))

        super(Note, self).save(*args, **kwargs)

    def publish(self):
        if not self.slug:
            self.slug = "{}-{}".format(slugify(self.title), secrets.token_hex(4))

        self.is_public = True
        self.save()

        return self.slug
