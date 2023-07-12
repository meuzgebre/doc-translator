import argparse
from doctranslator.controllers.translation_controller import TranslationController

def main():
    parser = argparse.ArgumentParser(description="TransLinguaDoc - Document Translator")
    parser.add_argument("--file_path", type=str, help="Path to the document file", required=True)
    parser.add_argument("--api_key", type=str, help="API key for the translation service", required=True)
    parser.add_argument("--target_language", type=str, help="Target language for translation", required=True)
    parser.add_argument("--source_language", type=str, help="Source language of the document (optional)")
    parser.add_argument("--file_type", type=str, help="File type of the document (optional)")
    parser.add_argument("--api_template", type=str, help="Path to API template for custom api call (optional)")

    args = parser.parse_args()    

    translation_controller = TranslationController()
    translated_file_path = translation_controller.translate_document(
        args.file_path,
        args.target_language,
        args.api_key
    )    

if __name__ == "__main__":    
    main()
