from googletrans import Translator
import time

translator = Translator()

input = input("Enter the text you want to convert to Hindi!\n")

out = translator.translate(input , dest="hi")

print(out.text)
time.sleep(10)