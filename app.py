#   88""Yb  dP"Yb  88   88 Yb  dP    db
#   88__dP dP   Yb 88   88  YbdP    dPYb
#   88"""  Yb   dP Y8   8P   8P    dP__Yb
#   88      YbodP  `YbodP'  dP    dP""""Yb


from PIL import Image
import os
from os import system
import colorama
from colorama import Fore, Style

colorama.init()

LOW_QUALITY = 50
MEDIUM_QUALITY = 75
HIGH_QUALITY = 90


def greeting():
    print("Welcome to REZI! To use me, all you need to do is copy me to your image folder, and I'll take care of the "
          "rest.  ")
    input('Press Enter to continue')


def reduce_image_quality(image_path, quality=75, overwrite=False):
    try:
        # Open the image
        image = Image.open(image_path)

        # Check for incompatible modes and convert accordingly
        # ... existing code for handling image modes ...

        # Save the image with reduced quality using its original format (if possible)
        new_folder = "REZI_Images"  # Customize this folder name if desired
        original_format = image.format

        if not os.path.exists(new_folder):
            os.makedirs(new_folder)  # Create the folder if needed

        new_image_path = f"{os.path.join(new_folder, os.path.basename(image_path))}_reduced.{original_format}"

        try:
            # Attempt to save using original format
            image.save(new_image_path, quality=quality)
        except Exception as e:
            # If saving with original format fails (e.g., unsupported format)
            print(f"Error saving '{image_path}' with original format: {e}")

            # Fallback: handle formats not supported by Pillow for quality reduction
            if original_format.lower() in ('png', 'gif', 'bmp'):
                print(f"Warning: Quality reduction not supported for '{original_format}'. "
                      f"Copying file to '{new_image_path}'.")
                os.copy(image_path, new_image_path)  # Copy the original file
            else:
                print(f"Error: Unsupported image format '{original_format}'.")
                return False  # Indicate error

        print(f"Image reduced and saved to: {new_image_path}")
        return True  # Indicate success

    except Exception as e:
        print(f"Error processing image '{image_path}': {e}")
        return False  # Indicate error


def handle_image_processing(folder_path, quality=80):
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and others
        os.system('clear')
    # Present options for quality level
    print("Choose a compression level:")
    print("1. Low Quality (Higher Compression)")
    print("2. Medium Quality")
    print("3. High Quality (Lower Compression)")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Use chosen quality level from predefined options
    quality = {
        1: LOW_QUALITY,
        2: MEDIUM_QUALITY,
        3: HIGH_QUALITY
    }[choice]
    # Process images with the chosen quality
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            if not reduce_image_quality(image_path, quality):
                print(f"Error processing image: {image_path}")


def find_and_reduce_images(folder_path, quality=80):
    image_formats = [".jpg", ".jpeg", ".png"]  # Add more formats as needed
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(tuple(image_formats)):
            image_path = os.path.join(folder_path, filename)
            reduce_image_quality(image_path, quality)


def colored_text(text, color):
    print(color + text + Style.RESET_ALL)


def main():
    # Get the current script's directory
    greeting()
    script_dir = os.path.dirname(os.path.realpath(__file__))
    handle_image_processing(script_dir)
    print(colored_text("Image processing complete.", Fore.GREEN))
    print(colored_text("**WARNING:** Some images might not have been compressed due to unsupported formats.",
                       Fore.YELLOW))
    input(colored_text("ATTENTION: If you enjoy using me or if you have any ideas to improve the app, please contact "
                       "me. Thank you! :)",
                       Fore.RED))


if __name__ == "__main__":
    main()
