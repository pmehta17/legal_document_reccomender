from TextCleaner import TextCleaner

input_folder = 'texts'
output_folder = 'cleaned_texts'

tc = TextCleaner(input_folder, output_folder)
tc.clean_texts()
