class Utils:
    @staticmethod
    def text_file_to_string(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
