# Python Streamlit Applications

This repository contains three separate Streamlit applications designed to perform different tasks:

## AI Image Generator

This application uses an API to generate images based on a user-provided prompt. It showcases the image and provides a download button for the user to save the generated image.

### How to Run

1. Replace `'YOUR_API_KEY'` with your actual API key.
2. Run `streamlit run image_generator.py`.
3. Enter a prompt in the text area.
4. Click "Generate Image" to view and download the image.

## QR Code Generator

Generates a QR code based on the input URL and allows the user to download the generated QR code image.

### How to Run

1. Run `streamlit run qr_generator.py`.
2. Enter the URL in the text input.
3. Click "Generate QR Code" to view and download the QR code.

## URL Shortener

Shortens a given URL using the `pyshorteners` library and displays the shortened URL.

### How to Run

1. Run `streamlit run url_shortener.py`.
2. Enter the URL in the text input.
3. Click "Generate new URL" to get the shortened URL.

## Installation

To install the required libraries, run:

```bash
pip install streamlit requests qrcode pyshorteners
