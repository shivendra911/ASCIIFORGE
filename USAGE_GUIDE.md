# ASCII Forge Usage Guide 📚

This comprehensive guide covers all features of **ASCII Forge**, from command-line tools to advanced Python API usage.

## Table of Contents
1. [Installation](#installation)
2. [Command Line Interface (CLI)](#command-line-interface)
   - [Image Converter (`asciiforge-image`)](#image-converter-cli)
   - [Text Artist (`asciiforge-text`)](#text-artist-cli)
3. [Python Library Usage](#python-library-usage)
   - [Converting Images](#converting-images)
   - [Creating Text Art](#creating-text-art)
   - [Batch Processing](#batch-processing)
4. [Advanced Customization](#advanced-customization)

---

## Installation

Ensure you have Python 3.8+ installed.

### Standard Installation
```bash
pip install asciiforge
```

### Development Installation
```bash
git clone https://github.com/yourusername/asciiforge.git
cd asciiforge
pip install -e .
```

---

## Command Line Interface

ASCII Forge provides two powerful CLI tools once installed.

### Image Converter CLI
**Command:** `asciiforge-image`

Reference for converting images and GIFs to ASCII art.

#### Syntax
```bash
asciiforge-image [IMAGE_PATH] [OPTIONS]
```

#### Common Examples
```bash
# Basic conversion (printed to console)
asciiforge-image photo.jpg

# Colored output with width of 120 chars
asciiforge-image photo.jpg --width 120 --color

# Save to file
asciiforge-image photo.jpg --output art.txt

# Face Mode (Optimized for portraits)
asciiforge-image portrait.jpg --face --width 160

# Emoji Mode
asciiforge-image icon.png --emoji

# Convert GIF (animate in terminal)
asciiforge-image loop.gif --loops 10 --fps 20
```

#### Full Options Reference
| Option | Short | Description |
|--------|-------|-------------|
| `--width` | `-w` | Character width of output (default: 100) |
| `--color` | `-c` | Enable ANSI colored output |
| `--output` | `-o` | Save output to a text file |
| `--gamma` | `-g` | Gamma correction (>1 brightens, <1 darkens) |
| `--face` | | Enable Face Mode (high detail, contrast boost) |
| `--emoji` | | Enable Emoji Mode (1:1 aspect ratio) |
| `--simple`| | Enable Simple Mode (fewer characters) |
| `--custom`| | Provide a custom character string (e.g. "@#.") |
| `--loops` | | Number of loops for GIF animation |
| `--fps` | | Frames Per Second for GIF playback |
| `--batch` | | Batch process a directory (see below) |

---

### Text Artist CLI
**Command:** `asciiforge-text`

Generate stylish text art and animations.

#### Syntax
```bash
asciiforge-text [TEXT] [OPTIONS]
```

#### Common Examples
```bash
# Basic Text
asciiforge-text "HELLO" --color cyan

# Neon Style
asciiforge-text "OPEN" --neon --color red

# Metal Style
asciiforge-text "ROCK" --metal --font block

# Animations
asciiforge-text "LOADING" --wave --loops 5
asciiforge-text "MATRIX" --decrypt --color green
asciiforge-text "NEWS" --marquee --speed 0.03
```

#### Full Options Reference
| Option | Short | Description |
|--------|-------|-------------|
| `--font` | `-f` | Font name (e.g., slant, block, shadow) |
| `--color` | `-c` | Color name (red, blue, cyan, etc.) |
| `--neon` | | Apply Neon Box style |
| `--metal` | | Apply Chrome/Metal style |
| `--retro` | | Apply CRT Retro style |
| `--shadow`| | Apply 3D Shadow style |
| `--wave` | | Animate with Sine Wave effect |
| `--glitch`| | Animate with Glitch effect |
| `--decrypt`| | Animate with Matrix Decrypt effect |
| `--list-fonts`| | List all available fonts |
| `--list-styles` | | List all available styles |

---

## Python Library Usage

### Converting Images

The `ImageConverter` class is the core of image processing.

```python
from asciiforge import ImageConverter

# 1. Initialize
converter = ImageConverter(
    width=100,          # Output width in characters
    color_mode=True,    # Enable color
    gamma=1.2           # Slight brightness boost
)

# 2. Convert standard image
ascii_art = converter.convert_image("path/to/image.jpg")
print(ascii_art)

# 3. specialized Modes
# Face Mode: Best for portraits
converter.set_mode_face() 
print(converter.convert_image("face.jpg"))

# Emoji Mode: Best for emojis/icons
converter.set_mode_emoji()
print(converter.convert_image("emoji.png"))
```

### Creating Text Art

Use `TextArtist` to generate styled text programmatically.

```python
from asciiforge import TextArtist

# 1. Initialize
artist = TextArtist("Hello World", font="slant", color="cyan")

# 2. Render Static Styles
# Returns string, does not print
neon_art = artist.render(style="neon")
print(neon_art)

# 3. Direct Display
artist.display(style="metal")

# 4. Animations (Blocking)
# These methods run the animation loop in the terminal
artist.animate_wave(loop_count=3)
artist.animate_glitch(loop_count=5)
# Infinite loop
# artist.animate_marquee(loop_count=0) 
```

### Batch Processing

Convert entire directories of images at once.

```python
from asciiforge import ImageConverter, BatchConverter

# Configure the base converter
converter = ImageConverter(width=80, color_mode=False)

# Initialize batch processor
batch = BatchConverter(converter)

# Process
# Input: folder of images
# Output: folder where .txt files will be saved
batch.process_directory(
    input_dir="assets/raw_images", 
    output_dir="assets/ascii_output"
)
```

---

## Advanced Customization

### Custom Character Ramps
You can define exactly which characters are used for shading, from darkest to lightest.

```python
from asciiforge import CustomTextConverter

# Define a custom ramp (Dark -> Light)
# Example: Matrix style binary
binary_ramp = "01 " 

converter = CustomTextConverter(
    custom_text=binary_ramp,
    width=120
)

print(converter.convert_image("matrix_code.jpg"))
```

### Defining New Text Styles
You can extend `Style_Base` to create your own text effects.

```python
from asciiforge.text_artist import Style_Base, TextArtist

class MyCustomStyle(Style_Base):
    def apply(self, art: str, color: str) -> str:
        # Manipulate the ASCII string here
        lines = art.split('\n')
        # ... logic ...
        return "\n".join(lines)

# Register the style
TextArtist.STYLES['my_style'] = MyCustomStyle()

# Use it
artist = TextArtist("TEST")
artist.display(style='my_style')
```

---
**Happy Forging!** 🔥
