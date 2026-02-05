from asciiforge import ImageConverter, TextArtist

# Image to ASCII
converter = ImageConverter(width=100, color_mode=True)
ascii_art = converter.convert_image('photo.jpg')

# Face mode
converter.set_mode_face()

# Animated GIF (runs 5 times)
converter.convert_gif('animation.gif', loop_count=5)

# Text art
artist = TextArtist('HELLO', font='slant', color='cyan')
artist.display(style='neon')
artist.animate_wave(loop_count=5)

# Command Line Usage
asciiforge-image photo.jpg -w 100 -c
asciiforge-text "HELLO" --neon --color cyan --loops 5