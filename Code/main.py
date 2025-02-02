import pyttsx3 
import PyPDF2
from tkinter.filedialog import askopenfilename

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)  
player = pyttsx3.init()

for num in range(pages):
    page = pdfreader.pages[num]  
    text = page.extract_text() 
    player.say(text)
    
player.runAndWait()


