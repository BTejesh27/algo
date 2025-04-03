import numpy as np
from PIL import Image, ImageOps
import cv2

def load_image(image_path):
    """Load an image, remove background, and enhance contrast."""
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img_array = np.array(img)

    # Apply Gaussian Blur to reduce noise
    img_blur = cv2.GaussianBlur(img_array, (5, 5), 0)

    # Adaptive thresholding to highlight human figures
    img_thresh = cv2.adaptiveThreshold(
        img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )

    # Edge detection (Canny)
    edges = cv2.Canny(img_thresh, 100, 200)

    # Morphological operations to enhance edges
    kernel = np.ones((3, 3), np.uint8)
    img_processed = cv2.dilate(edges, kernel, iterations=1)

    # Convert back to PIL image
    return Image.fromarray(img_processed)

def resize_image(img, width):
    """Resize the image to the specified width while maintaining aspect ratio."""
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio / 2)  # Adjust height for Braille mapping
    return img.resize((width, height), Image.LANCZOS)

def apply_threshold(img_array, threshold=0.5):
    """Apply threshold to the image array."""
    return (img_array > threshold * 255).astype(np.int8)  # Inverted to match Braille style

def array_to_braille(binary_array):
    """Convert a binary array to Braille Unicode characters."""
    height, width = binary_array.shape
    height_pad = (4 - height % 4) % 4
    width_pad = (2 - width % 2) % 2
    
    if height_pad > 0 or width_pad > 0:
        binary_array = np.pad(binary_array, ((0, height_pad), (0, width_pad)), 'constant')
    
    height, width = binary_array.shape
    result = []
    
    for i in range(0, height, 4):
        line = []
        for j in range(0, width, 2):
            block = binary_array[i:i+4, j:j+2]
            
            code = 0
            if block[0, 0]: code |= 0x01  # Dot 1
            if block[1, 0]: code |= 0x02  # Dot 2
            if block[2, 0]: code |= 0x04  # Dot 3
            if block[0, 1]: code |= 0x08  # Dot 4
            if block[1, 1]: code |= 0x10  # Dot 5
            if block[2, 1]: code |= 0x20  # Dot 6
            if block[3, 0]: code |= 0x40  # Dot 7
            if block[3, 1]: code |= 0x80  # Dot 8
            
            char = chr(0x2800 + code)
            line.append(char)
        result.append(''.join(line))
    
    return '\n'.join(result)

def generate_braille_art(image_path, width=50, threshold=0.5):
    """Generate Braille dot art from an image."""
    img = load_image(image_path)
    img = resize_image(img, width)
    img_array = np.array(img)
    binary_array = apply_threshold(img_array, threshold)
    braille_art = array_to_braille(binary_array)
    return braille_art

def main():
    image_path = input("Enter the path to the image file: ")
    width = int(input("Enter the width (default 50): ") or 50)
    threshold = float(input("Enter the threshold (0.0-1.0, default 0.5): ") or 0.5)
    
    braille_art = generate_braille_art(image_path, width, threshold)
    print("\nGenerated Braille Art:\n")
    print(braille_art)
    
    save_option = input("Do you want to save the Braille art? (yes/no): ").strip().lower()
    if save_option == 'yes':
        output_path = input("Enter the output file name (e.g., output.txt): ").strip()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(braille_art)
        print(f"Braille art saved to {output_path}")

if __name__ == "__main__":
    main()
