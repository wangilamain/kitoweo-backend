from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProjectConfig(AppConfig):
    name = 'kitoweo'
    verbose_name = ('kitoweo')

    def ready(self):
        import project.signals