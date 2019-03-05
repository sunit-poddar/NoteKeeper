# django imports
from django.db import models

# app imports
from note_utils.model_utils import RowInformation


class Note(RowInformation):
    title = models.CharField(max_length=256, null=False, blank=False)
    text = models.TextField(help_text="Put in your notes here")

    class Meta:
        verbose_name_plural = "Notes"

    def save(self, *args, **kwargs):
        super(Note, self).save(*args, **kwargs)
