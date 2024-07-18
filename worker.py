import TextCleaner

input_folder = 'texts'
output_folder = 'cleaned_texts'

cleaner = TextCleaner(input_folder, output_folder)
cleaner.clean_texts()
