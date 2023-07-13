import argparse
import os
from doctranslator.controllers.translation_controller import TranslationController

def main():
    """
    Main function to execute the FTP login program.
    """
    parser = argparse.ArgumentParser(description="TransLinguaDoc - Document Translator")
    parser.add_argument("--file_path", type=str, help="Path to the document file", required=True)
    parser.add_argument("--api_key", type=str, help="API key for the translation service", required=True)
    parser.add_argument("--target_language", type=str, help="Target language for translation", required=True)
    parser.add_argument("--source_language", type=str, help="Source language of the document (optional)")    
    parser.add_argument("--engine", type=str, help="The API engine to use for translating (optional)")
    parser.add_argument("--api_template", type=str, help="Path to API template for custom api call (optional)")

    args = parser.parse_args()    
    
    # Validate file extension if provided
    if args.file_type and args.file_type.lower() not in ["docx", "pdf"]:
        print("Invalid file type. Supported types are 'docx' and 'pdf'.")
        exit()

    # Validate file existence
    if not os.path.isfile(args.file_path):
        print("File does not exist.")
        exit()

    translation_controller = TranslationController()
    translated_file_path = translation_controller.translate_document(
        args.file_path,
        args.api_key,
        args.target_language,
        args.source_language,
        args.engine
        args.api_template
    )
    # translation_controller.translate_document(document_file, target_language, api_key)

if __name__ == "__main__":    
    main()
