from PIL import Image
import os

def rotate_images_in_folder(folder_path, degrees):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    for file in files:
        # Check if the file is an image (you can adjust the list of valid image extensions)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(folder_path, file)

            # Open the image using PIL
            image = Image.open(file_path)

            # Rotate the image
            rotated_image = image.rotate(degrees, expand=True)

            # Save the rotated image back to the same file
            rotated_image.save(file_path)

            print(f"Rotated {file} by {degrees} degrees.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    rotation_degrees = int(input("Enter the rotation angle in degrees: "))

    rotate_images_in_folder(folder_path, rotation_degrees)
    