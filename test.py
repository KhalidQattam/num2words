from bidi.algorithm import get_display
import arabic_reshaper
from bidi.algorithm import get_display
from num2words import num2words

print get_display(arabic_reshaper.reshape(num2words(550,lang='ar')))