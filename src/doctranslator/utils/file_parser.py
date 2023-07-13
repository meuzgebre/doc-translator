def get_file_name_with_language_extension(file_path, target_language):
    try:
        file_name = file_path.split("/")[-1]
        file_name_parts = file_name.split(".")
        base_name = ".".join(file_name_parts[:-1])
        extension = file_name_parts[-1]

        return f"{base_name}_translated_{target_language}.{extension}"
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
