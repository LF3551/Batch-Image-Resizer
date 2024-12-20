"""
Copyright (c) 2024 Aleksei Aleinikov

Licensed under the Universal Permissive License (UPL), Version 1.0.
You may obtain a copy of the License at https://opensource.org/licenses/UPL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software, associated documentation and/or data (collectively the
"Software"), to deal in the Software without restriction, including without
limitation the rights to copy, create derivative works of, display, perform,
and distribute the Software and make, use, sell, offer for sale, import,
export, have made, and have sold the Software and the Larger Work(s), and to
sublicense the foregoing rights on either these or other terms.

This license is subject to the following condition:
The above copyright notice and this permission notice must be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import argparse
import os
from PIL import Image

def resize_image(input_file, output_file, width, height):
    try:
        with Image.open(input_file) as img:
            if img.mode == "RGBA":  
                img = img.convert("RGB")  
            img_resized = img.resize((width, height))
            img_resized.save(output_file)
            print(f"Resized {input_file} to {output_file} with size {width}x{height}")
    except Exception as e:
        print(f"Error resizing image {input_file}: {e}")


def batch_resize(input_folder, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'webp')):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_folder, file)
                resize_image(input_file, output_file, width, height)

def convert_format(input_file, output_file, format):
    try:
        with Image.open(input_file) as img:
            img.save(output_file, format=format)
            print(f"Converted {input_file} to {output_file} as {format}")
    except Exception as e:
        print(f"Error converting image {input_file}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Batch Image Resizer - Resize and Convert Images in Bulk")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")


    resize_parser = subparsers.add_parser('resize', help="Resize a single image")
    resize_parser.add_argument('--input', '-i', required=True, help="Input image file")
    resize_parser.add_argument('--output', '-o', required=True, help="Output image file")
    resize_parser.add_argument('--width', '-w', type=int, required=True, help="Width of the resized image")
    resize_parser.add_argument('--height', '-H', type=int, required=True, help="Height of the resized image")  


    batch_resize_parser = subparsers.add_parser('batch-resize', help="Resize all images in a folder")
    batch_resize_parser.add_argument('--input', '-i', required=True, help="Input folder containing images")
    batch_resize_parser.add_argument('--output', '-o', required=True, help="Output folder for resized images")
    batch_resize_parser.add_argument('--width', '-w', type=int, required=True, help="Width of the resized images")
    batch_resize_parser.add_argument('--height', '-H', type=int, required=True, help="Height of the resized images")  


    convert_parser = subparsers.add_parser('convert', help="Convert image format")
    convert_parser.add_argument('--input', '-i', required=True, help="Input image file")
    convert_parser.add_argument('--output', '-o', required=True, help="Output image file")
    convert_parser.add_argument('--format', '-f', required=True, help="Output image format (JPEG, PNG, WEBP)")

    args = parser.parse_args()

    if args.command == 'resize':
        resize_image(args.input, args.output, args.width, args.height)
    elif args.command == 'batch-resize':
        batch_resize(args.input, args.output, args.width, args.height)
    elif args.command == 'convert':
        convert_format(args.input, args.output, args.format.upper())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
