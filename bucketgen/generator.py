import numpy as np
import matplotlib.pyplot as plt

class Generator:
    def __init__(self, images: np.ndarray) -> None:
        self.images = images
        N, H, W, C = self.images.shape
        self.buckets = np.zeros((H, W, C, 256), dtype=float)

        for n in range(N):
            for h in range(H):
                for w in range(W):
                    for c in range(C):
                        intensity = self.images[n, h, w, c]
                        self.buckets[h, w, c, intensity] += 1
    
        # technically the below conversion means self.buckets should be interpreted as probabilities and not buckets
        for h in range(H):
            for w in range(W):
                for c in range(C):
                    total_count = np.sum(self.buckets[h, w, c])
                    if total_count > 0:
                        self.buckets[h, w, c] /= total_count

    def sample(self, show_result=False) -> np.ndarray:
        _, H, W, C = self.images.shape
        sampled_image = np.zeros_like(self.images[0])

        for h in range(H):
            for w in range(W):
                for c in range(C):
                    sampled_image[h, w, c] = np.random.choice(np.arange(256), p=self.buckets[h, w, c])
        
        if show_result:
            plt.imshow(sampled_image)
            plt.show()

        return sampled_image


        
