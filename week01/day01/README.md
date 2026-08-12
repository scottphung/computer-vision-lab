# Week 1 — Day 1: Image as Data

## What I learned

- An image can be represented as a NumPy array.
- Grayscale images have shape `(height, width)`.
- Color images have shape `(height, width, 3)`.
- OpenCV uses BGR channel order by default.
- `image[y, x]` accesses a pixel.
- `image[y, x, channel]` accesses a specific color channel.
- `uint8` is an unsigned 8-bit integer with values from 0 to 255.
- `image.shape` describes the structure of the image.
- `image.dtype` describes the data type of the values.

## Key mental model

```text
Image
  ↓
NumPy array
  ↓
Rows × Columns × Channels
  ↓
Numerical pixel values