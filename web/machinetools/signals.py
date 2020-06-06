import os

from django.db.models.signals import post_delete
from django.dispatch import receiver

from machinetools.models import Manual, RiggingImage, RiggingFile, InstrumentImage, InstrumentFile, StanokImage


def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


@receiver(post_delete, sender=InstrumentImage)
@receiver(post_delete, sender=RiggingImage)
@receiver(post_delete, sender=StanokImage)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        _delete_file(instance.image.path)


@receiver(post_delete, sender=RiggingFile)
@receiver(post_delete, sender=Manual)
@receiver(post_delete, sender=InstrumentFile)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        _delete_file(instance.file.path)
