# Image Resizer

## Overview

A quick and efficient Python script to **resize multiple images** in a folder using **Pillow** library. Ideal for optimising images for web or mobile apps!

## Installation

Install Pillow if not already installed:
```sh
pip install pillow
```

## How to use

1. Clone the repository:
    ```sh
    git clone https://github.com/Aditya15267/image-resizer.git
2. Run the script:
    ```sh
    python image_resizer.py input_folder output_folder --width 300 --height 300
    ```
    - ```input_folder```: Folder containing original images
    - ```output_folder```: Folder to save resized images
    - ```--width```: Desired image width (default: 300)
    - ```--height```: Desired image height (default: 300)

## Supported Formats

- ```.jpg```
- ```.jpeg```
- ```.png```

## Example

```sh
    python image_resizer.py ./original ./resized --width 512 --height 512
```
