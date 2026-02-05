"""
ASCII Forge - Professional ASCII Art Generation Package
========================================================

A comprehensive toolkit for converting images to ASCII art and creating
styled text art with animations.

Main Classes:
-------------
- ImageConverter: Convert images and GIFs to ASCII art
- TextArtist: Create styled ASCII text art with animations
- BatchConverter: Batch process multiple images

Quick Start:
-----------
    # Image to ASCII
    from asciiforge import ImageConverter
    
    converter = ImageConverter(width=100, color_mode=True)
    ascii_art = converter.convert_image('photo.jpg')
    print(ascii_art)
    
    # Text Art
    from asciiforge import TextArtist
    
    artist = TextArtist('HELLO', font='slant', color='cyan')
    artist.display(style='neon')
    artist.animate_wave(loop_count=5)

Features:
---------
- High-quality image to ASCII conversion
- Multiple rendering modes (grayscale, color, emoji)
- Face detection mode with enhanced detail
- Animated GIF support
- Text art with 20+ fonts and multiple styles
- Various animations (wave, flow, glitch, decrypt, etc.)
- Batch processing capabilities
- File export functionality

Author: ASCII Forge Team
License: MIT
"""

__version__ = '1.0.0'
__author__ = 'ASCII Forge Team'
__all__ = [
    'ImageConverter',
    'CustomTextConverter', 
    'BatchConverter',
    'TextArtist',
    'TextArtGallery',
    'Color',
]

from .image_converter import (
    ImageConverter,
    CustomTextConverter,
    BatchConverter,
)

from .text_artist import (
    TextArtist,
    TextArtGallery,
    Color,
)