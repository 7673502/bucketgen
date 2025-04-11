from PIL import Image
import numpy as np
import os

class DataLoader:
    def __init__(self, images_directory: str, verbose: bool = True) -> None:
        if not os.path.exists(images_directory):
            raise OSError
        
        image_list = []
        failed_loads = 0

        for root, _, files in os.walk(images_directory):
            for file in files:
                try:
                    image_path = os.path.join(root, file)
                    image = Image.open(image_path)
                    image_list.append(np.asarray(image))
                except OSError as e:
                    failed_loads += 1

        if verbose:
            print(f'Successfully loaded {len(image_list) - failed_loads} / {len(image_list)} images.')

        self.images = np.stack(image_list)

    def to_grayscale(self) -> np.array:
        grayscale_images = (
            0.3086 * self.images[:, :, :, 0] + 
            0.6094 * self.images[:, :, :, 1] + 
            0.0820 * self.images[:, :, :, 2]
        )
        return np.expand_dims(grayscale_images, axis=-1)
    

