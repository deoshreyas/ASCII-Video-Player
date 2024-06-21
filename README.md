# ASCII-Video-Player

## :zap: About
This is a very simple project I made to play around with OpenCV. It first captures frames from your webcamera, which it resizes for optimization purposes (keeping aspect ratio as it is). Finally, it converts each pixel in the frame to ASCII characters based on a simple 'density sorted string'. Basically, the higher the average of the RGB values in the pixel, the 'denser' the ASCII character for it.

**NOTE:** Currently, the resolution of the video is very poor (the size of each ASCII character is around 7 pixels). This is done as higher resolutions will put a lot of stress on the CPU and/or GPU. If you think your machine can handle that, please change `PIXEL_SIZE` in the source code.

## :desktop_computer: How to run locally
Just clone the repository on your machine, and run `pip install -r requirements.txt` to install all the packages. Then run `main.py` and you are good to go! 