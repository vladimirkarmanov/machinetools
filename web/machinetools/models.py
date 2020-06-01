from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


class StanokGroup(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа станков'
        verbose_name_plural = 'Группы станков'


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
    description = models.TextField(max_length=2000, verbose_name='Описание')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stanok_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Станок'
        verbose_name_plural = 'Станки'


class StanokImage(models.Model):
    stanok = models.ForeignKey(Stanok, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=True, null=True, upload_to='stanok/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                              verbose_name='Изображение')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Изображение станка'
        verbose_name_plural = 'Изображения станка'


class WorkpieceType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид обрабатываемой детали'
        verbose_name_plural = 'Виды обрабатываемой детали'


class ProcessingType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид обработки'
        verbose_name_plural = 'Виды обработок'


class ApplicationArea(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Область применения'
        verbose_name_plural = 'Области применения'


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
    description = models.TextField(max_length=2000, verbose_name='Описание')
    file1 = models.FileField(blank=True, null=True, verbose_name='Файл 1')
    file2 = models.FileField(blank=True, null=True, verbose_name='Файл 2')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('instrument_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'


class InstrumentImage(models.Model):
    instrument = models.ForeignKey(Instrument,
                                   on_delete=models.CASCADE,
                                   related_name='images')
    image = models.ImageField(blank=True, null=True, upload_to='instrument/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                              verbose_name='Изображение')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Изображение инструмента'
        verbose_name_plural = 'Изображения инструмента'


class Manual(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    file = models.FileField(blank=True, null=True, verbose_name='Файл')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'


class RiggingType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид оснастки'
        verbose_name_plural = 'Виды оснасток'


class Rigging(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    rigging_type = models.ForeignKey(RiggingType,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     verbose_name='Вид оснастки')
    description = models.TextField(max_length=2000, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оснастка'
        verbose_name_plural = 'Оснастки'


class RiggingImage(models.Model):
    rigging = models.ForeignKey(Rigging,
                                on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(blank=True, null=True, upload_to='rigging/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
                              verbose_name='Изображение')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Изображение оснастки'
        verbose_name_plural = 'Изображения оснастки'
