from django.apps import AppConfig


class MachinetoolsConfig(AppConfig):
    name = 'machinetools'
    verbose_name = 'Machine Tools'

    def ready(self):
        import machinetools.signals
