# coding: utf-8
from django.db import models
from django.contrib.admin import widgets as admin_widgets
from .widgets import UEditorWidget, AdminUEditorWidget


class UEditorField(models.TextField):

    def __init__(
            self,
            verbose_name=None,
            width=600,
            height=300,
            toolbars="full",
            imagePath="",
            filePath="",
            upload_settings={},
            settings={},
            command=None,
            event_handler=None,
            **kwargs):
        self.ueditor_settings = locals().copy()
        kwargs["verbose_name"] = verbose_name
        del self.ueditor_settings["self"], self.ueditor_settings[
            "kwargs"], self.ueditor_settings["verbose_name"]
        super(UEditorField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': UEditorWidget(attrs=self.ueditor_settings)}
        defaults.update(kwargs)
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = AdminUEditorWidget(
                attrs=self.ueditor_settings)
        return super(UEditorField, self).formfield(**defaults)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^DjangoUeditor\.models\.UEditorField"])
except:
    pass
