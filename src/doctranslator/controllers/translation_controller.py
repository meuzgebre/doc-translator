from doctranslator.services.translation_service import TranslationService

class TranslationController:
    def __init__(self):
        self.translation_service = TranslationService()
            
    def translate_document(self, file_path, api_key, target_language, source_language, engine, api_template):
        self.translation_service.set_api_key(api_key)
        translated_file_path = self.translation_service.translate_document(file_path, api_key, target_language, source_language, api_template)
        print(f"Translation completed. Translated document saved as '{translated_file_path}'."
