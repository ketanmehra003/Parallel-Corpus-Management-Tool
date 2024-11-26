from django.apps import AppConfig


class CorpusManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'corpus_manager'

    def ready(self):
        from . import signals
