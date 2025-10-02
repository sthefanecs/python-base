"""
Esse é um programa Multi Línguas que exibe "Hello Word" conforme a 
configuração do seu sistema operacional.
"""

__version__ = "1.0.0"
__author__ = "Sthefane Costa"
__license__ = "Unlicense"

import os 

current_language = os.getenv("LANG")

msg = ("Hello, World!")

if current_language == "pt_BR":
    msg = ("Olá, Mundo!")

elif current_language == "fr_FR":
    msg = ("Bonjour, le monde!")


print(msg)