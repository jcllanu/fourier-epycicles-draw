# fourier-epycicles-draw
This project visualizes how any 2D drawing can be reconstructed using **epicycles** derived from the **Fourier series**. By computing the coefficients of the complex Fourier Series, the program creates an animation that traces the original drawing with rotating vectors.

## ✨ Features
- Convert drawings (hand-drawn, functions, or points paths) into point data
- Compute Fourier coefficients
- Animate epicycles that reconstruct the original figure
- Adjustable number of frequency components
- ## 🧮 Math Behind the Epicycles

A 2D drawing can be represented as a curve, that is a function of a time interval into the plane or alternatively the complex numbers. That is, 
\[
f(t)=(g(t),h(t)) \equiv g(t) + ih(t)
\]
We can break it into a sum of rotating vectors called **epicycles**.

The formula for reconstructing the signal is:

\[
f(t) = \sum_{k=-N}^{N} c_k \cdot e^{2\pi i k t}
\]

Where:
- \( c_k \) are the **Fourier coefficients** (complex numbers) obtained from the DFT. Each one defines a circle:
  - Magnitude = radius of the epicycle
  - Phase = initial angle
  - Frequency = rotation speed
- \( k \) is the frequency index (positive and negative)
- \( t \in [0, 1] \) represents time or progress through the drawing

Each term contributes a rotating circle (epicycle), and the sum of all vectors traces the original shape. More terms give higher accuracy.

In practice:
1. Sample the drawing into N complex points.
2. Apply DFT to get \( c_k \) values.
3. Animate the epicycles using these components to reconstruct the figure.
