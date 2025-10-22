from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid argument: " + sys.argv[1])
    if sys.argv[2] not in font_list:
        sys.exit("Invalid argument: " + sys.argv[2])
    figlet.setFont(font=sys.argv[2])
else:
    figlet.setFont(font=random.choice(font_list))

text = input("Input: ")
print("Output:")
print(figlet.renderText(text))
