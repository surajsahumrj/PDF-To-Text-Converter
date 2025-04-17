import PyPDF2
import os


def create_directory(directory):
    """Creates a directory if it doesn't already exist."""
    if not os.path.isdir(directory):
        os.mkdir(directory)


def get_file_path(prompt):
    """Prompts the user to enter a file path and validates it."""
    while True:
        file_path = input(prompt)
        if os.path.exists(file_path):
            return file_path
        else:
            print(f"Error: '{file_path}' does not exist. Please enter a valid file path.")


def pdf_to_text(pdf_path, txt_path):
    """Converts a PDF file to a text file."""
    try:
        with open(pdf_path, 'rb') as pdf_obj:
            pdf_reader = PyPDF2.PdfFileReader(pdf_obj)
            num_pages = pdf_reader.numPages

            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                for page_num in range(num_pages):
                    page_obj = pdf_reader.getPage(page_num)
                    page_text = page_obj.extractText()
                    txt_file.write(page_text)

                    # Feedback on processing
                    print(f"Processing page {page_num + 1} of {num_pages}...")

        print(f"Text extraction completed. The text has been saved to {txt_path}")
    except Exception as e:
        print(f"Error during PDF processing: {e}")


def main():
    create_directory("temp")  # Ensure temp directory exists

    # Get PDF and text file paths from the user
    pdf_path = get_file_path("Enter the name of your pdf file - please use backslash when typing in directory path: ")
    txt_path = input("Enter the name of your txt file - please use backslash when typing in directory path (Leave empty for default path): ")

    if not txt_path:
        # Generate default txt path based on PDF filename
        base_dir = os.path.realpath("temp")
        txt_path = os.path.join(base_dir, os.path.basename(pdf_path).replace(".pdf", ".txt"))

    # Convert PDF to text
    pdf_to_text(pdf_path, txt_path)


if __name__ == "__main__":
    main()
