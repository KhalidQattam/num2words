from num2words import num2words
from bidi.algorithm import get_display
import arabic_reshaper

# Replace '12345' with the number you want to convert
number_to_convert = 77777777456200126

# Convert the number to words in Arabic
words_in_arabic = num2words(number_to_convert, lang='ar')

# Reshape the Arabic words to display correctly
reshaped_text = arabic_reshaper.reshape(words_in_arabic)

# Get the display text with correct RTL (Right-To-Left) orientation
display_text = get_display(reshaped_text)

# Print the result
print(display_text)
