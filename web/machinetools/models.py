from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

from machinetools.utils import compress_image


class StanokGroup(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = RichTextUploadingField(config_name='default', blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Группа станков'
        verbose_name_plural = 'Группы станков'
        ordering = ['name']

    def __str__(self):
        return self.name


class Stanok(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    group = models.ForeignKey(StanokGroup,
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name='Группа станков')
    power = models.FloatField(verbose_name='Мощность, кВт')
    rotation_frequency = models.FloatField(verbose_name='Частота вращения, Об/мин')
    spindle_cone = models.CharField(max_length=50, verbose_name='Конус шпинделя')
    torque = models.FloatField(verbose_name='Крутящий момент, Н*м')
    description = RichTextUploadingField(config_name='default', blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Станок'
        verbose_name_plural = 'Станки'
        ordering = ['group']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stanok_detail', kwargs={'pk': self.pk})


class StanokImage(models.Model):
    stanok = models.ForeignKey(Stanok, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=True, null=True, upload_to='stanok/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                              verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение станка'
        verbose_name_plural = 'Изображения станка'

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)


class WorkpieceType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Вид обрабатываемой детали'
        verbose_name_plural = 'Виды обрабатываемой детали'
        ordering = ['name']

    def __str__(self):
        return self.name


class ProcessingType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Вид обработки'
        verbose_name_plural = 'Виды обработок'
        ordering = ['name']

    def __str__(self):
        return self.name


class ApplicationArea(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Область применения'
        verbose_name_plural = 'Области применения'
        ordering = ['name']

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    workpiece_type = models.ForeignKey(WorkpieceType,
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       verbose_name='Вид обрабатываемой детали')
    processing_type = models.ForeignKey(ProcessingType,
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        verbose_name='Вид обработки')
    application_area = models.ForeignKey(ApplicationArea,
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         verbose_name='Область применения')
    description = RichTextUploadingField(config_name='default', blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('instrument_detail', kwargs={'pk': self.pk})


class InstrumentFile(models.Model):
    instrument = models.ForeignKey(Instrument,
                                   on_delete=models.CASCADE,
                                   related_name='files')
    file = models.FileField(blank=True, null=True, upload_to='instrument/', verbose_name='Файл')

    class Meta:
        verbose_name = 'Файл инструмента'
        verbose_name_plural = 'Файлы инструмента'

    def __str__(self):
        return self.file.name


class InstrumentImage(models.Model):
    instrument = models.ForeignKey(Instrument,
                                   on_delete=models.CASCADE,
                                   related_name='images')
    image = models.ImageField(blank=True, null=True, upload_to='instrument/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                              verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение инструмента'
        verbose_name_plural = 'Изображения инструмента'

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)


class RiggingType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Вид оснастки'
        verbose_name_plural = 'Виды оснасток'
        ordering = ['name']

    def __str__(self):
        return self.name


class Rigging(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    rigging_type = models.ForeignKey(RiggingType,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     verbose_name='Вид оснастки')
    description = RichTextUploadingField(config_name='default', blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Оснастка'
        verbose_name_plural = 'Оснастки'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rigging_detail', kwargs={'pk': self.pk})


class RiggingFile(models.Model):
    rigging = models.ForeignKey(Rigging,
                                on_delete=models.CASCADE,
                                related_name='files')
    file = models.FileField(blank=True, null=True, upload_to='rigging/', verbose_name='Файл')

    class Meta:
        verbose_name = 'Файл оснастки'
        verbose_name_plural = 'Файлы оснастки'

    def __str__(self):
        return self.file.name


class RiggingImage(models.Model):
    rigging = models.ForeignKey(Rigging,
                                on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(blank=True, null=True, upload_to='rigging/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                              verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение оснастки'
        verbose_name_plural = 'Изображения оснастки'

    def __str__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)


class Manual(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    file = models.FileField(upload_to='manual/', verbose_name='Файл')

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'
        ordering = ['name']

    def __str__(self):
        return self.name


class ModernBladeProcessing(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    preview = models.ImageField(upload_to='modern_blade_processing/',
                                validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                                verbose_name='Превью')
    content = RichTextUploadingField(config_name='default', verbose_name='Контент')

    class Meta:
        verbose_name = 'Современная лезвийная обработка'
        verbose_name_plural = 'Современные лезвийные обработки'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mbp_detail', kwargs={'pk': self.pk})
