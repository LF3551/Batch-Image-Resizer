# Batch Image Resizer

**Batch Image Resizer** is a Python-based CLI tool for resizing and converting images in bulk. Supports multiple formats like JPEG, PNG, and WebP, with options for resizing, changing resolution, and batch format conversion. Ideal for developers, designers, and photographers.

## Features
- Resize a single image or all images in a folder.
- Convert images between formats (JPEG, PNG, WEBP).
- Simple and fast command-line interface.

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/LF3551/Batch-Image-Resizer.git
   cd BatchImageResizer
```
2. Install required packages:
```bash
pip install -r requirements.txt
```


## Usage

### Commands

#### Resize a Single Image
```bash
python3 main.py resize --input=input.jpg --output=output.jpg --width=800 --height=600
```

#### Batch Resize
```bash
python3 main.py batch-resize --input=./input_images --output=./output_images --width=800 --height=600
```

#### Convert Image Format
```bash
python main.py convert --input=input.jpg --output=output.webp --format=WEBP
```
