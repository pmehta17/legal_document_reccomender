import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class TextCleaner:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        tokens = word_tokenize(text.lower())  # Tokenize and lowercase
        cleaned_tokens = [token for token in tokens if token.isalpha() and token not in self.stop_words]
        cleaned_text = ' '.join(cleaned_tokens)
        return cleaned_text

    def process_file(self, file_path, output_folder):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            cleaned_text = self.clean_text(text)
            output_file_path = os.path.join(output_folder, os.path.basename(file_path))
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(cleaned_text)

    def clean_folder(self, input_folder, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for file_name in os.listdir(input_folder):
            if file_name.endswith('.txt'):
                file_path = os.path.join(input_folder, file_name)
                self.process_file(file_path, output_folder)
