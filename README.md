# fourier-epycicles-draw
This project visualizes how any 2D drawing can be reconstructed using **epicycles** derived from the **Fourier series**. By computing the coefficients of the complex Fourier Series, the program creates an animation that traces the original drawing with rotating vectors.

## ✨ Features
- Convert drawings (hand-drawn, functions, or .svg images) into point data
- Compute Fourier coefficients
- Animate epicycles that reconstruct the original figure
- Adjustable number of frequency components

## 🧮 Math Behind the Epicycles

A 2D drawing can be represented as a curve, that is a function of a time interval into the real plane $$ℝ^2$$, or alternatively the complex numbers ℂ. Let's restric ourselves to close curves, that is, 

$$f(t)=\(g(t),h(t)\) \equiv g(t) + ih(t),    t \in \[-\pi,\pi\]$$ and $$f(t)=f(t+2\pi)$$

We can break it into a sum of rotating vectors called **epicycles**.

The formula for reconstructing the curve is:

$$f(t) = g(t) + ih(t) = \sum_{k=-\infty}^{\infty} c_k \cdot e^{i k t} \approx \sum_{k=-K}^{K} c_k \cdot e^{i k t} =  \sum_{k=-K}^{K} |c_k| (\cos(kt+\theta_k) + i \cdot \sin(kt+\theta_k)) $$

Where:
- $$c_k = \frac{1}{2\pi}\int_{-\pi}^{\pi} f(t) e^{- i k t} \mathrm{d}t $$ are the complex **Fourier coefficients**. Given that $$c_k = |c_k| e^{i \theta_k +2n\pi i}$$, each one defines a circle :
  - Radius of the epicycle: $$|c_k|$$
  - Phase (initial angle): $$\theta_k$$
  - Frequency (rotation speed): $$k$$
-  t $$\in \[-\pi, \pi\] $$ represents time or progress through the drawing

Each term contributes a rotating circle (epicycle), and the sum of all vectors traces the original shape. More terms, i.e., greater $K$, give higher accuracy.

In practice:
1. Sample the drawing into a set of complex points.
2. Compute the $$|c_k|$$ and $$\theta_k$$ values (from $$c_k$$)
3. Animate the epicycles using these components to reconstruct the figure.
