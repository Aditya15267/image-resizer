from PIL import Image
import os
import argparse

def resize_images(input_folder, output_folder, width, height):
    """
    Resize all images in the input folder and save them to the output folder.
    """
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if not os.path.exists(input_folder):
        print(f'Input folder {input_folder} does not exist.')
   
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                img_path = os.path.join(input_folder, filename)
                img = Image.open(img_path)
                resize_img = img.resize((width, height))
                output_path = os.path.join(output_folder, filename)
                resize_img.save(output_path)
                print(f'Resized {filename} saved to {output_path}')
            except Exception as e:
                print(f'Error processing {filename}: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Resize all images in a folder')
    parser.add_argument('input', type=str, help='Path to the input folder')
    parser.add_argument('output', type=str, help='Path to the output folder')
    parser.add_argument('--width', type=int, default=300, help='Width of resized images')
    parser.add_argument('--height', type=int, default=300, help='Height of resized images')

    args = parser.parse_args()
    resize_images(args.input, args.output, args.width, args.height)
