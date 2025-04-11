import pytest
import bucketgen as bg

def test_init():
    dl = bg.DataLoader('tests/data/dataset1', verbose=False)
    assert dl.images.shape == (10, 32, 32, 3)

def test_init_single():
    dl = bg.DataLoader('tests/data/dataset2', verbose=False)
    assert dl.images.shape == (1, 32, 32, 3)

def test_nonexistent():
    with pytest.raises(OSError):
        dl = bg.DataLoader('tests/data/foo', verbose=False) # non existent dataset

def test_grayscale():
    dl = bg.DataLoader('tests/data/dataset1', verbose=False)
    grayscale_images = dl.to_grayscale()
    assert grayscale_images.shape == (10, 32, 32, 1)
