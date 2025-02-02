# 📄 to 🎧 Book Converter

This 🐉 project converts 📄 files into 🎧 books using 🔤-to-🎧 (TTS) technology. It extracts 📖 from 📄 documents and reads it aloud 🔊, providing an accessible way to consume written content.

## ✨ Features

- Extracts 📖 from 📄 files
- Converts 📖 to 🎧 using TTS
- Supports 🌍 languages (🌐 if specified)
- Saves 🎧 output as an 🎵 file

## 🔧 Prerequisites

Make sure you have 🐉 3.x installed on your 🖥️.

## 📦 Installation

1. **🔄 Clone the Repository:**  
   ```bash
   git clone https://github.com/yourusername/pdf-to-audiobook.git
   cd pdf-to-audiobook
   ```

2. **Create a 🌱 Virtual Environment (✨ Optional but recommended):**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On 💻 Windows use: venv\Scripts\activate
   ```

3. **Install 📁 Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

## 🔍 Required Libraries

- `PyPDF2`: For extracting 📖 from 📄 files
- `gTTS`: 🔍 Text-to-🎧 for converting 📖 to 🎧
- `playsound`: For playing the generated 🎧 file

Install them manually if needed:
```bash
pip install PyPDF2 gTTS playsound
```

## 🔄 Usage

1. **Place your 📄 file** in the project directory.

2. **Run the 🔮 script:**  
   ```bash
   python pdf_to_audio.py
   ```

3. **Follow the 🔔 prompts:**
   - 📅 Enter the name of the 📄 file.
   - The script will extract 📖 and convert it to an 🎧 file (`output.mp3`).

4. **🎵 Listen to your 🎧 book:**  
   The generated 🎵 file will be saved in the project directory.

## 📜 Example

```bash
$ python pdf_to_audio.py
Enter the name of the PDF file (with extension): sample.pdf
Converting PDF to audio...
Audio book saved as output.mp3
```

## 🔧 Customization

- **🌍 Change Language:** You can modify the 🌍 in the script by adjusting the `lang` parameter in `gTTS`. For example, to convert to Hindi:
  ```python
  tts = gTTS(text, lang='hi')
  ```

- **🔢 Select Specific Pages:** Update the script to specify 📄 numbers to convert only certain sections.

## ❓ Troubleshooting

- **📂 Missing Modules:** If you get an ⛔️ import error, ensure all required libraries are installed.
- **🎧 Not Playing:** Check if `playsound` is correctly installed and supported on your 🖥️ OS.
- **📖 Extraction Issues:** Some 📄s may have non-selectable 📖. Consider using 🔮 OCR tools like `pytesseract` for such cases.



## 📂 Contributing

Feel free to 🔄 fork this repository and contribute by submitting 📅 pull requests.

## 📧 Contact

For any 📢 questions or suggestions, contact Shadab Firoz at Shdbfrz@gmail.com.

