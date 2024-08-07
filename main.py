# Generates bids in three different distributions


import numpy as np


def random_snorm(n, mean=0, sd=1, xi=1.5):
    def random_snorm_aux(n, xi):
        weight = xi / (xi + 1 / xi)
        z = np.random.uniform(-weight, 1 - weight, n)
        xi_ = xi ** np.sign(z)
        random = -np.absolute(np.random.normal(0, 1, n)) / xi_ * np.sign(z)
        m1 = 2 / np.sqrt(2 * np.pi)
        mu = m1 * (xi - 1 / xi)
        sigma = np.sqrt((1 - m1 ** 2) * (xi ** 2 + 1 / xi ** 2) + 2 * m1 ** 2 - 1)
        return (random - mu) / sigma

    return random_snorm_aux(n, xi) * sd + mean


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    normalBids = np.round(np.random.normal(50, 5, 10), 1)
    normalBids.sort()
    print("Normal bids ", normalBids)
    skewedBids = np.round(random_snorm(10, 50, 10, 1.5), 1)
    skewedBids.sort()
    print("Skewed bids ", skewedBids)
    uniformBids = np.round(np.random.uniform(0.0, 100.0, 10), 1)
    uniformBids.sort()
    print("Uniform bids ", uniformBids)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
