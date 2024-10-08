﻿# table_extraction
Here’s a sample **README** file for your table extraction project using Python and OCR.

---

# Table Extraction from Images using Python

## Project Overview

This project focuses on extracting table data from images using Python. The extracted data is structured and saved in an Excel format. The project uses OCR (Optical Character Recognition) to detect and extract text, and various pre-processing techniques to improve the accuracy of table extraction, especially when dealing with complex layouts, multiple boxes, or colored text (like red text).

## Features

- **Table Detection**: Identifies tables and cells within images.
- **Text Extraction**: Extracts text from individual cells, including colored text (e.g., red text).
- **Excel Export**: Exports extracted data into structured Excel sheets.
- **Handling Complex Tables**: Supports nested tables, variable cell sizes, and tables with missing borders.
  
## Technologies Used

- **Python**: Core programming language for implementing the solution.
- **PaddleOCR**: OCR engine used for text recognition.
- **Tesseract (Optional)**: Another open-source OCR engine for text extraction.
- **OpenCV**: Used for image pre-processing, such as color filtering and edge detection.
- **Pandas**: For data manipulation and exporting the extracted tables to Excel.
- **OCR Space API**: An API to perform OCR on images with advanced table extraction features.
- **NumPy**: For numerical computations during image processing.

## Installation

### Prerequisites

Ensure that the following are installed:

- **Python 3.x**
- **pip** (Python package installer)

### Required Libraries

Install the required Python libraries by running the following command:

```bash
pip install opencv-python paddleocr requests pandas numpy
```

Alternatively, you can install the dependencies from the `requirements.txt` file (if included):

```bash
pip install -r requirements.txt
```

### Configuration

You need an API key for **OCR Space API** to extract tables. Get an API key by signing up at [OCR Space](https://ocr.space/ocrapi).

Once you have the API key, update your code where needed:

```python
API_KEY = 'your_api_key_here'
```

## How to Use

### Input Image

1. Prepare your input image containing the table.
2. Ensure the table and text are clear and readable, especially if working with colored text or complex layouts.

### Running the Script

To run the table extraction script, execute:

```bash
python table_extraction.py
```

### Output

The extracted table data will be exported into an Excel file (`extracted_data.xlsx`), following the desired format.

### Key Parameters

- **IMAGE_PATH**: Path to the input image.
- **API_KEY**: API key for OCR Space.
- **CROP_COORDINATES**: Tuple of coordinates `(x1, y1, x2, y2)` for cropping the input image (if needed).

Example:

```python
IMAGE_PATH = 'path/to/your/image.jpg'
CROP_COORDINATES = (33, 317, 306, 551)
```

### Customization

- **Table Extraction**: If the tables in your images are highly complex or contain nested structures, you may need to adjust the pre-processing steps (e.g., cropping, filtering).
- **Red Text Handling**: The project can detect red text by using color filtering. You can modify the `preprocess_red_text` function to handle different shades of red.

## Project Structure

```
├── table_extraction.py    # Main script to run the table extraction
├── requirements.txt       # List of required packages
├── extracted_data.xlsx    # Output file (generated after running the script)
└── README.md              # This file
```

## Known Limitations

- **Low-Resolution Images**: The accuracy of text extraction drops significantly when working with low-quality or pixelated images.
- **Complex Layouts**: Nested tables or tables with inconsistent borders may require additional fine-tuning.
- **Handwritten Text**: This project focuses on printed text and may not perform well on handwritten tables.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License.

---

This is a basic README for your project that can be expanded based on specific implementation details or additional features you may add later.
