import fitz  # PyMuPDF

def split_pdf_pages(input_pdf_path, output_pdf_path, dpi=200):
    # Open the input PDF
    pdf_document = fitz.open(input_pdf_path)
    new_pdf = fitz.open()  # New PDF document for the split pages
    
    # Loop over each page in the original PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        rect = page.rect  # Page dimensions

        # Calculate the midpoint to split the page in half horizontally
        midpoint_x = rect.width / 2

        # Define the two rectangles for left and right pages
        left_rect = fitz.Rect(0, 0, midpoint_x, rect.height)
        right_rect = fitz.Rect(midpoint_x, 0, rect.width, rect.height)

        # Render each half as an image with higher DPI
        left_pix = page.get_pixmap(clip=left_rect, dpi=dpi)
        right_pix = page.get_pixmap(clip=right_rect, dpi=dpi)

        # Create new pages for each half and add the images
        left_page = new_pdf.new_page(width=midpoint_x, height=rect.height)
        left_page.insert_image(left_page.rect, pixmap=left_pix)

        right_page = new_pdf.new_page(width=midpoint_x, height=rect.height)
        right_page.insert_image(right_page.rect, pixmap=right_pix)

    # Save the new PDF with split pages
    new_pdf.save(output_pdf_path)
    new_pdf.close()
    pdf_document.close()
    print(f"New PDF saved as {output_pdf_path}")

# Usage
input_pdf_path = "split.pdf"  # Path to your input PDF file
output_pdf_path = "output_vertical_split.pdf"  # Path to save the output PDF file
split_pdf_pages(input_pdf_path, output_pdf_path, dpi=300)  # You can adjust DPI as needed
