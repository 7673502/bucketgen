# BucketGen
BucketGen is a basic image generation algorithm that works by sampling from the pixels intensities in a dataset. 

## Basic Usage
BucketGen consists of two main components: the `DataLoader` and `Generator` classes. The `DataLoader` class converts a given directory of images to a NumPy array, and the `Generator` class creates images by sampling pixel values from a given NumPy array. 

The basic usage, including examples showing how to create images similar to the ones shown in the ["Example Outputs"](#-example-outputs) section, is explained in the [demo jupyter notebook](demonstration.ipynb).

## Example Outputs
Examples of BucketGen output on some famous datasets:

**MNIST Handwritten Digits**
![image](examples/mnist.png)

**CIFAR-10**
![image](examples/cifar10.png)


## References
*This project uses the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) and [MNIST Handwritten Digits](http://yann.lecun.com/exdb/mnist/) datasets for testing.*
