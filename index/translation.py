from modeltranslation.translator import translator, TranslationOptions
from .models import Especialidad

class EspecialidadTranslationOptions(TranslationOptions):
    fields = ('title', 'description','text',)


translator.register(Especialidad, EspecialidadTranslationOptions)