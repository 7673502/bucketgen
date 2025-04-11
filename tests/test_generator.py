import bucketgen as bg
import numpy as np

def test_single_image():
    dl = bg.DataLoader('tests/data/dataset2', verbose=False)
    generator = bg.Generator(dl.images)

    # sampled image should equal dataset in single dataset
    assert (dl.images[0] == generator.sample()).all()

def test_single_image_grayscale():
    dl = bg.DataLoader('tests/data/dataset2', verbose=False)
    grayscale_images = dl.to_grayscale()
    generator = bg.Generator(grayscale_images)

    assert (grayscale_images[0] == generator.sample()).all()

