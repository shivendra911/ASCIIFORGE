# ASCII Forge 🔥

**Professional ASCII Art Generation Toolkit**

Convert images to stunning ASCII art and create animated text art with style. Built with clean OOP architecture, ready for PyPI distribution.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Features

### 🖼️ Image to ASCII Converter
- **High-detail grayscale** (default mode)
- **Colored output** with ANSI color codes
- **Emoji mode** with auto aspect correction
- **Face recognition mode** with enhanced detail
- **Custom character ramps**
- **Animated GIF support** with configurable loops
- **Batch processing** for multiple images
- **File export** to text files

### 🎨 Text Art Generator
- **20+ fonts** via pyfiglet
- **6 static styles**: Neon, Metal, Retro, Shadow, Galaxy, Rainbow
- **6 animations**: Wave, Flow, Glitch, Decrypt, Typewriter, Marquee
- **Custom colors** from terminal palette
- **Loop control** - animations run 5 times by default
- **File export** with ANSI code stripping

## Installation

### From Source (Development)

```bash
git clone https://github.com/yourusername/asciiforge.git
cd asciiforge
pip install -e .
```

### From PyPI (Once Published)

```bash
pip install asciiforge
```

### Requirements

```
Python >= 3.8
Pillow >= 10.0.0
pyfiglet >= 0.8.0
colorama >= 0.4.6
```

## Quick Start

### Python API

#### Image to ASCII

```python
from asciiforge import ImageConverter

# Basic conversion
converter = ImageConverter(width=100, color_mode=True)
ascii_art = converter.convert_image('photo.jpg')
print(ascii_art)

# Face mode (optimized for portraits)
converter = ImageConverter(width=150)
converter.set_mode_face()
ascii_art = converter.convert_image('face.jpg')

# Animated GIF (runs 5 times then stops)
converter = ImageConverter(width=80, color_mode=True)
converter.convert_gif('animation.gif', fps=30, loop_count=5)

# Save to file
converter.save_to_file(ascii_art, 'output.txt')
```

#### Custom Character Ramps

```python
from asciiforge import CustomTextConverter

# Use custom characters (dark to light)
converter = CustomTextConverter(
    custom_text="@#*+=-:. ",
    width=100,
    color_mode=True
)
ascii_art = converter.convert_image('photo.jpg')
```

#### Emoji Mode

```python
converter = ImageConverter(width=80)
converter.set_mode_emoji()
# Automatically adjusts aspect ratio for emojis
converter.ramp = "🟦🟩🟨🟧🟥"
ascii_art = converter.convert_image('photo.jpg')
```

#### Text Art

```python
from asciiforge import TextArtist

# Basic styled text
artist = TextArtist('HELLO', font='slant', color='cyan')
artist.display(style='neon')

# Animations (run 5 times by default)
artist.animate_wave(loop_count=5)
artist.animate_glitch(loop_count=3)
artist.animate_decrypt()

# Save to file
artist.save('title.txt', style='metal')
```

### Command Line Interface

#### Image Converter CLI

```bash
# Basic conversion
asciiforge-image photo.jpg -w 100 -c

# Face mode with high detail
asciiforge-image face.jpg --face -w 150 -o output.txt

# Animated GIF (runs 5 times)
asciiforge-image animation.gif --fps 30 --loops 5

# Custom character ramp
asciiforge-image photo.jpg --custom "@#*+. " -c

# Emoji mode
asciiforge-image emoji.png --emoji

# Batch process directory
asciiforge-image input_dir/ --batch output_dir/
```

#### Text Art CLI

```bash
# Basic text
asciiforge-text "HELLO WORLD" --font slant --color cyan

# Static styles
asciiforge-text "CYBER" --neon --color magenta
asciiforge-text "CHROME" --metal --font block
asciiforge-text "RETRO" --retro --color green

# Animations (Ctrl+C to stop, or runs 5 times)
asciiforge-text "WAVE" --wave --color blue --loops 3
asciiforge-text "HACKER" --decrypt --color green
asciiforge-text "NEWS" --marquee --speed 0.02 --loops 5

# Save to file
asciiforge-text "TITLE" --neon -o title.txt

# List available options
asciiforge-text --list-fonts
asciiforge-text --list-styles
asciiforge-text --list-colors
```

## Advanced Usage

### Batch Processing

```python
from asciiforge import ImageConverter, BatchConverter

converter = ImageConverter(width=100, color_mode=True)
batch = BatchConverter(converter)
batch.process_directory('input_images/', 'output_ascii/')
```

### Custom Styles

```python
from asciiforge.text_artist import Style_Base, TextArtist

class CustomStyle(Style_Base):
    def apply(self, art: str, color: str) -> str:
        # Your custom styling logic
        return styled_art

# Use it
TextArtist.STYLES['custom'] = CustomStyle()
artist = TextArtist('TEXT')
artist.display(style='custom')
```

### Animation Customization

```python
# Control animation parameters
artist = TextArtist('CUSTOM', color='magenta')

# Wave with custom loops
artist.animate_wave(loop_count=10)

# Marquee with custom speed and direction
artist.animate_marquee(
    speed=0.02,
    direction='right',
    loop_count=5,
    style='neon'
)

# Typewriter with custom speed
artist.animate_typewriter(speed=0.01)
```

## Configuration Options

### ImageConverter Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `width` | int | 100 | Character width of output |
| `color_mode` | bool | False | Enable colored output |
| `gamma` | float | 1.0 | Brightness adjustment (>1 brightens) |
| `ramp` | str | Standard | Character ramp (dark to light) |
| `aspect_ratio` | float | 0.55 | Height/width ratio compensation |
| `enhance` | bool | True | Apply preprocessing filters |

### TextArtist Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | str | - | Text to convert |
| `font` | str | 'slant' | Font name (pyfiglet fonts) |
| `color` | str | 'white' | Color name from palette |

### Animation Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `loop_count` | int | 5 | Number of animation loops (0=infinite) |
| `speed` | float | 0.04 | Animation speed multiplier |
| `direction` | str | 'left' | Scroll direction for marquee |
| `fps` | int | 30 | Frames per second for GIF playback |

## Available Styles & Fonts

### Text Art Styles
- **neon** - Glowing box border
- **metal** - Chrome gradient
- **retro** - CRT scanlines
- **shadow** - 3D reflection
- **galaxy** - Starfield background
- **rainbow** - Color rows

### Text Art Animations
- **wave** - Sine wave motion
- **flow** - RGB color flow
- **glitch** - Cyberpunk corruption
- **decrypt** - Matrix reveal
- **typewriter** - Character by character
- **marquee** - Horizontal scroll

### Colors
red, green, yellow, blue, magenta, cyan, white, black

### Sample Fonts
slant, block, banner, digital, script, bubble, shadow, doom, starwars, etc.

List all fonts: `asciiforge-text --list-fonts`

## Architecture

```
asciiforge/
├── asciiforge/
│   ├── __init__.py              # Package initialization
│   ├── image_converter.py       # Image to ASCII classes
│   ├── text_artist.py           # Text art classes
│   ├── cli_image.py            # Image CLI tool
│   └── cli_text.py             # Text CLI tool
├── tests/                      # Unit tests
├── examples/                   # Example scripts
├── setup.py                    # Package configuration
├── README.md                   # This file
├── LICENSE                     # MIT License
└── requirements.txt            # Dependencies
```

## Testing

```bash
# Run tests
pytest tests/

# With coverage
pytest --cov=asciiforge tests/
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built on [Pillow](https://python-pillow.org/) for image processing
- Text art powered by [pyfiglet](https://github.com/pwaller/pyfiglet)
- Terminal colors via [colorama](https://github.com/tartley/colorama)

## Examples Gallery

### Image Conversion

```
Original Image → ASCII Art

    @@@@@@@@@@@@@@@@
  @@##############@@
 @#******************#@
@#********************#@
#****     ****     ****#
#***  @@  ****  @@  ***#
#****     ****     ****#
 #**********************#
  #********************#
   @@################@@
```

### Text Art Styles

**Neon:**
```
+------------------------+
| ██  ██ ████ ██   ██    |
| ██  ██ ██   ██   ██    |
| ██████ ████ ██   ██    |
| ██  ██ ██   ██   ██    |
| ██  ██ ████ ████ ████  |
+------------------------+
```

**Galaxy:**
```
   * .  ██  ██  . ° ██ *
.  ° ██ . ██  °  ██  * ██
 * ██ ° ██████  . ██ ° ██
```

## Support

- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/asciiforge/issues)
- 📖 Docs: [Full Documentation](https://github.com/yourusername/asciiforge#readme)

## Roadmap

- [ ] Video to ASCII support
- [ ] Web interface
- [ ] Real-time webcam ASCII
- [ ] 3D ASCII rendering
- [ ] ASCII font designer
- [ ] More animation effects

---

**Made with ❤️ by Shivendra Pratap**