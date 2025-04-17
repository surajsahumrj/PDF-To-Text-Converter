# PDF to Text Conversion Script

This Python script converts the contents of a PDF file into a text file using the PyPDF2 library. It reads the PDF file, extracts the text from each page, and saves it to a specified text file.

## Features

- **PDF to Text Conversion**: Extracts all text from a PDF file.
- **Error Handling**: Handles errors for invalid file paths and PDF reading.
- **Directory Management**: Creates a `temp` directory if it doesn't already exist to store the output file.
- **Progress Feedback**: Displays feedback on the number of pages being processed.
- **Flexible File Paths**: You can specify your own file paths or use a default output path.

## Requirements

- Python 3.x
- PyPDF2 library

### Installation

1. **Install Python**: Ensure Python 3.x is installed on your machine. If not, download and install it from [python.org](https://www.python.org/downloads/).
   
2. **Install PyPDF2**: You can install the PyPDF2 library using pip:
   ```bash
   pip install PyPDF2
   ```

### Usage

1. **Clone or Download the Script**: Download or clone the repository containing the script.

2. **Run the Script**: Open a terminal or command prompt and run the script:
   ```bash
   python pdf_to_text.py
   ```

3. **Provide Input**:
   - **PDF file path**: Enter the path of the PDF file you want to convert to text.
   - **Text file path**: Enter the desired output file path for the extracted text. If left empty, the text will be saved in the `temp` directory with the same name as the PDF.

4. **The program will process the PDF**: The script will read the PDF, extract text from each page, and save it to the specified output text file. You will see progress updates as the pages are processed.

## Example

```bash
Enter the name of your pdf file - please use backslash when typing in directory path: C:\Documents\sample.pdf
Enter the name of your txt file - please use backslash when typing in directory path (Leave empty for default path): 
```

In this example, the text from `sample.pdf` will be saved as `temp\sample.txt`.

## File Structure

- `pdf_to_text.py`: The main script that performs the PDF-to-text conversion.
- `temp/`: A folder that will store the output text files if no custom path is provided.

## Code Overview

### Functions:

- **`create_directory(directory)`**: Ensures the `temp` directory exists for storing output files.
- **`get_file_path(prompt)`**: Prompts the user for a file path and validates if it exists.
- **`pdf_to_text(pdf_path, txt_path)`**: Reads the PDF, extracts text, and writes it to a text file.
- **`main()`**: The main function that orchestrates the flow of the program.

### Error Handling

- If the provided PDF path is invalid, the script will prompt the user to enter a valid path.
- If there are any issues with reading the PDF or extracting text, they will be caught and printed.

## License

This script is released under the MIT License.
