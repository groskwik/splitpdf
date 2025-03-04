# PDF Page Splitter Script

This Python script splits each page of a PDF document vertically into two separate pages. It utilizes the [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) library (imported as `fitz`) to handle PDF operations.

## Features

- **Vertical Splitting**: Divides each page of a PDF into two equal halves vertically.
- **High-Resolution Rendering**: Allows specification of the DPI (dots per inch) to control the quality of the split pages.

## Requirements

- **Python 3.x**
- **PyMuPDF**: Install using `pip install pymupdf`.

## Installation

1. **Install Python**: Ensure Python 3 is installed on your system. Download it from the [official Python website](https://www.python.org/).

2. **Install PyMuPDF**: Install the PyMuPDF library using `pip`:

   ```bash
   pip install pymupdf
   ```

## Usage

1. **Prepare the Script**: Save the provided script to a `.py` file.

2. **Specify Input and Output Paths**: Modify the `input_pdf_path` and `output_pdf_path` variables in the script to point to your input and desired output PDF file paths:

   ```python
   input_pdf_path = "input.pdf"       # Path to your input PDF file
   output_pdf_path = "output.pdf"     # Path to save the output PDF file
   ```

3. **Set DPI (Optional)**: Adjust the `dpi` parameter to control the resolution of the split pages. The default is 200 DPI:

   ```python
   split_pdf_pages(input_pdf_path, output_pdf_path, dpi=200)
   ```

4. **Run the Script**: Execute the script using a terminal or command prompt:

   ```bash
   python script_name.py
   ```

5. **Output**: The script will process each page of the input PDF, split it vertically into two pages, and save the modified pages to the specified output PDF file.

## Functions

- `split_pdf_pages(input_pdf_path, output_pdf_path, dpi=200)`: Splits each page of the input PDF vertically into two pages and saves the result to the output PDF.

## Notes

- **Page Dimensions**: The script automatically calculates the midpoint of each page to ensure an accurate vertical split.

- **Resolution**: Higher DPI values result in better image quality but may increase processing time and output file size.

- **Dependencies**: Ensure that the PyMuPDF library is installed and up to date to avoid compatibility issues.

## License

This project is licensed under the MIT License.

## References

- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/en/latest/)
- [Stack Overflow: How to split a PDF with PyMuPDF](https://stackoverflow.com/questions/64637180/how-to-split-a-pdf-with-pymupdf-with-a-loop)
- [GitHub Issue: How to split a page in PDF using PyMuPDF](https://github.com/rk700/PyMuPDF/issues/219)

For further information on manipulating PDFs with Python, consider exploring the [PyMuPDF Tutorial](https://pymupdf.readthedocs.io/en/latest/tutorial.html). 
