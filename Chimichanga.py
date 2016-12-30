import Chimichanga
import tkinter as tk
from tkinter.filedialog import askopenfilename
import sys

# Test it out
root = tk.Tk()
root.withdraw()
sig = "1"
while sig == "1":
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

    if(filename != ""):
        archivo = open(filename)
        datosArch = archivo.read()
        Chimichanga.execute(datosArch, filename, True)
    
    sig = input("\n\nPresione 1 y ENTER para cargar otro archivo...")
    print("")
    print("")
