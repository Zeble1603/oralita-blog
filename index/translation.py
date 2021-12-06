from modeltranslation.translator import translator, TranslationOptions
from .models import Especialidad

class EspecialidadTranslationOptions(TranslationOptions):
    fields = ('title', 'description','text','meta_description','meta_title',)



translator.register(Especialidad, EspecialidadTranslationOptions)