from django.contrib import admin

from .models import (
    StanokImage, Stanok, InstrumentImage,
    Instrument, ApplicationArea, ProcessingType,
    WorkpieceType, StanokGroup, Manual)


class StanokImageInline(admin.TabularInline):
    model = StanokImage
    extra = 2


class StanokAdmin(admin.ModelAdmin):
    inlines = [StanokImageInline]
    list_display = ['name', 'group', 'power', 'rotation_frequency', 'spindle_cone', 'torque']
    list_display_links = ['name']
    list_filter = ['group']
    search_fields = ['name', 'description']


class InstrumentImageInline(admin.TabularInline):
    model = InstrumentImage
    extra = 2


class InstrumentAdmin(admin.ModelAdmin):
    inlines = [InstrumentImageInline]
    list_display = ['name', 'workpiece_type', 'processing_type', 'application_area']
    list_display_links = ['name']
    list_filter = ['workpiece_type', 'processing_type', 'application_area']
    search_fields = ['name', 'description']


admin.site.register(StanokGroup)
admin.site.register(Stanok, StanokAdmin)

admin.site.register(ApplicationArea)
admin.site.register(ProcessingType)
admin.site.register(WorkpieceType)
admin.site.register(Instrument, InstrumentAdmin)

admin.site.register(Manual)
