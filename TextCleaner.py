import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class TextCleaner:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        nltk.download('stopwords')
        nltk.download('punkt')

        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    def remove_stopwords(self, text):
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text)
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(filtered_words)

    def clean_texts(self):
        for filename in os.listdir(self.input_folder):
            if filename.endswith('.txt'):
                with open(os.path.join(self.input_folder, filename), 'r', encoding='utf-8') as file:
                    text = file.read()
                    cleaned_text = self.remove_stopwords(text)

                    # Write cleaned text to new file in output folder
                    output_filename = os.path.join(self.output_folder, filename)
                    with open(output_filename, 'w', encoding='utf-8') as output_file:
                        output_file.write(cleaned_text)

                print(f'Processed {filename}.')

        print('All files processed.')

