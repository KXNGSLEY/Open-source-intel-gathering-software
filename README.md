# OSINT Toolkit

OSINT Toolkit is a Python-based Open Source Intelligence (OSINT) tool with a graphical user interface (GUI) built using Tkinter. It provides various functionalities such as username lookup, email breach checks, IP address lookups, document and image metadata extraction, facial similarity search, and reverse image search.

## Features

✅ **Username Lookup** – Search for usernames across multiple platforms.\
✅ **Email Breach Check** – Check if an email has been compromised in known data breaches.\
✅ **IP Address Lookup** – Retrieve information about an IP address.\
✅ **Document Metadata Extraction** – Extract metadata from PDF and DOCX files.\
✅ **Image Metadata Extraction** – Extract EXIF data from images.\
✅ **Face Similarity Search** – Identify similar faces in an image dataset.\
✅ **Reverse Image Search** – Perform an online reverse image search.

## Installation

### Prerequisites

Ensure you have Python installed (Python 3.8+ recommended). Install required dependencies using:

```bash
pip install -r requirements.txt
```

### Running the Application

Run the script using:

```bash
python main.py
```

### Creating a Standalone Executable

To generate a standalone `.exe` file, use **PyInstaller**:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --icon=app.ico main.py
```

The executable will be located in the `dist/` folder.

## Usage

1. **Username Lookup**: Enter a username and click "Search Username".
2. **Email Check**: Enter an email and click "Check Email".
3. **IP Lookup**: Enter an IP address and click "Check IP".
4. **File Analysis**:
   - Click "Browse" to select a file.
   - Click "Extract Metadata" for document/image analysis.
   - Click "Find Similar Faces" for facial matching.
   - Click "Reverse Image Search" to find similar images online.

## Screenshots



## Contributing

There mighe be bugs....a lot of em so feel free to submit issues and pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.

## Disclaimer

This tool is for ethical OSINT research only. I (Kxngsley) am not responsible for any misuse.


