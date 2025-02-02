# 📄 to 🎧 Book Converter

This project converts 📄 files into 🎧 books using text-to-speech (TTS) technology. It extracts text from 📄 documents and reads it aloud 🔊.

## 📁 Code Overview

```python
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
```

### Features
- **Select PDF:** Choose your PDF file using a GUI dialog.
- **Extract Text:** Reads all pages from the selected PDF.
- **Convert to Audio:** Converts extracted text into speech using `pyttsx3`.
- **Listen Aloud:** Plays the audio immediately after conversion.

## 📦 How to Install Libraries

Use `pip` to install the required libraries:

```bash
pip install PyPDF2 pyttsx3
```

- **`PyPDF2`:** For reading and extracting text from PDFs.
- **`pyttsx3`:** Converts text to speech and plays it aloud.
- **`tkinter`:** (Comes pre-installed with Python) Used for GUI-based file selection.

## 🔄 Running the Code in VS Code

1. **Open VS Code:** Launch Visual Studio Code.
2. **Create/Open File:** Create a new `.py` file or open an existing one.
3. **Copy & Paste Code:** Paste the provided Python code into your file.
4. **Open Terminal:**
   - Go to **View** > **Terminal** in the top menu.
5. **Run the Script:**
   ```bash
   python filename.py
   ```
6. **Select PDF:** A file dialog will appear; select your PDF.
7. **Listen to Audio:** The PDF content will be read aloud automatically.

## 💡 Features Recap

- **Easy File Selection:** GUI for picking PDF files.
- **Full Document Reading:** Reads all pages of your PDF.
- **Instant Playback:** Text is converted to audio and played immediately.
- **Offline Functionality:** Works without internet access.

## ❓ Troubleshooting

- **Missing Modules:** If you get an import error, run `pip install PyPDF2 pyttsx3`.
- **Audio Issues:** Ensure your device's sound is working, and `pyttsx3` is properly installed.
- **Non-readable PDFs:** Some PDFs may contain images or non-extractable text. Use OCR tools like `pytesseract` if needed.

## 📅 License

This project is licensed under the MIT License.

## 📂 Contributing

Feel free to fork this repository and contribute by submitting pull requests.

#Thanks
Coding With Evan

## 📧 Contact

For any questions or suggestions, contact Shadab Firoz at shdbfrz@gmail.com.


