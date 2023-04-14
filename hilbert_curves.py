import numpy as np
import matplotlib.pyplot as plt

class Hilbert:
    def __init__(self, figsize=(8, 8)):
        self.figsize = figsize

    def h0(self):
        '''First order Hilbert curve'''

        x = [-0.5, -0.5, 0.5, 0.5]
        y = [0.5, -0.5, -0.5, 0.5]
        x, y = np.array(x), np.array(y)

        return (x + 1j*y)*2

    def __call__(self, n):
        '''Finds (n+1)th order Hilbert curve

        Returns: complex array z whose real components are x-values, and
        imaginary components are y-values'''

        if n == 0:
            return self.h0()

        z = self(n-1)

        z0 = z.copy() * np.exp(1j*np.pi/2)
        z1 = z.copy()
        z2 = z.copy()
        z3 = z.copy() * np.exp(-1j*np.pi/2)

        width_last = 2**(n) - 1
        scaling = 1 + 1/width_last

        # shift:
        z0 += - scaling + 1j*scaling
        z1 += - scaling - 1j*scaling
        z2 += scaling - 1j * scaling
        z3 += scaling + 1j*scaling

        z0 = z0[::-1]
        z3 = z3[::-1]

        z = np.concatenate([z0, z1, z2, z3])*2

        # scale to [-1, 1]:
        z = z/np.max(np.real(z))

        return z

    def plot(self, n, show=True):
        '''Plot (n+1)th order Hilbert curve'''

        z = self(n)

        x = np.real(z)
        y = np.imag(z)

        fig, axs = plt.subplots(figsize=self.figsize)

        # axes limits:
        max_y = np.max(y)*1.1
        max_x = np.max(x)*1.1

        axs.set_ylim(-max_y, max_y)
        axs.set_xlim(-max_x, max_x)
        axs.plot(x, y, lw=1)

        if show:
            plt.show()

        return fig, axs


if __name__ == '__main__':

    H = Hilbert()
    H.plot(5)
