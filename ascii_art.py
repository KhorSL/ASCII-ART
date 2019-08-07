'''
  * Credits:
    - https://github.com/RameshAditya/asciify
'''


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageOps, ImageDraw
import sys


''' Different sets of ASCII characters '''

ASCII_CHARS = ['@', '#', '8', '&', 'o', ':', '*', '+', ',', '.', ' ']
# ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

''' Inversion for dark background '''
# ASCII_CHARS = ASCII_CHARS[::-1]


IMAGE_PATH = 1


GRAYSCALE = 'L'


PIXEL_ON = 0  # PIL color to use for "on"
PIXEL_OFF = 255  # PIL color to use for "off"


DEFAULT_FONT_PATH = 'fonts/Courier New.ttf'


FIXED_NEW_WIDTH = 100

'''
  * Credits: 
     - https://stackoverflow.com/questions/29760402/converting-a-txt-file-to-an-image-in-python
     - https://github.com/kobejohn/polymaze/blob/master/polymaze/polygrid.py#L207-L261
'''
def string_image(string, font_path=None):
  """Convert string to a grayscale image with black characters on a white background.

  arguments:
  string - this string will be converted to an image
           if string has "\n" token in it, interpret it as a newline
  font_path - path to a font file (for example impact.ttf)
  """

  ''' For array parsing to lines
    # lines = tuple(l for l in array)
  '''

  lines = string.split('\n')

  # Choosing font
  large_font = 100  # get better resolution with larger size
  font_path = font_path or 'fonts/Courier.dfont'
  try:
    font = ImageFont.truetype(font_path, size=large_font)
  except IOError:
    font = ImageFont.load_default()
    printc('Chosen font could not bed used. Using default font.')

  # make the background image based on the combination of font and lines
  pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
  max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
  # max height is adjusted down because it's too large visually for spacing
  test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  max_height = pt2px(font.getsize(test_string)[1])
  max_width = pt2px(font.getsize(max_width_line)[0])
  height = max_height * len(lines)  # perfect or a little oversized
  width = int(round(max_width + 40))  # a little oversized
  image = Image.new(GRAYSCALE, (width, height), color=PIXEL_OFF)
  draw = ImageDraw.Draw(image)

  # draw each line of text
  vertical_position = 5
  horizontal_position = 5
  line_spacing = int(round(max_height * 0.65))  # reduced spacing seems better
  for line in lines:
    draw.text((horizontal_position, vertical_position), line, fill=PIXEL_ON, font=font)
    vertical_position += line_spacing

  # crop the text
  c_box = ImageOps.invert(image).getbbox()
  image = image.crop(c_box)
  return image


def pixels_to_image_array(ascii_pixels, width):
  ''' Unflattening the array

  * range(0, len(pixels), width)
      - Create a sequence of numbers from 0 to length of pixels
      - but increment by the width instead of 1.
  * pixels[i:i+width]
     - This creates the row of the matrix

  '''
  return [ascii_pixels[i : i + width] for i in range(0, len(ascii_pixels), width)]


def image_array_to_string(image):
  return '\n'.join(image)


def asciify_pixels(image, groups=25):
  pixels = list(image.getdata())
  ascii_pixels = [ASCII_CHARS[pixel_intensity//groups] for pixel_intensity in pixels]
  return ''.join(ascii_pixels)


def convert_to_grayscale(image):
  return image.convert(GRAYSCALE)


def resize(image, new_width=FIXED_NEW_WIDTH):
  initial_width, initial_height = image.size
  aspect_ratio = float(initial_height)/float(initial_width)
  new_height = int(aspect_ratio * new_width)
  return image.resize((new_width, new_height))


def apply_magic(image):
  resized_image = resize(image)
  grayscale_image = convert_to_grayscale(resized_image)
  ascii_pixels = asciify_pixels(grayscale_image)
  final_image = pixels_to_image_array(ascii_pixels, resized_image.width)
  return image_array_to_string(final_image)


def main():
  """ Main program """
  image_path = sys.argv[IMAGE_PATH]

  try:
    image = Image.open(image_path)
  except Exception:
    print("Unable to find image in", image_path)
    return

  final_image = apply_magic(image)
  
  print (final_image)

  ''' To write out as text file '''
  f = open('output/text/ascii_art.txt', 'w')
  f.write(final_image)
  f.close()

  ''' To save a .png file '''
  image = string_image(final_image, DEFAULT_FONT_PATH)
  image.save('output/images/ascii_art.png')


if __name__ == "__main__":
  main()
