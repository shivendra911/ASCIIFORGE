#!/usr/bin/env python3
"""
Example: Image to ASCII Conversion
Demonstrates various image conversion features
"""

from asciiforge import ImageConverter, CustomTextConverter

def example_basic():
    """Basic image to ASCII conversion"""
    print("=" * 60)
    print("Example 1: Basic Grayscale Conversion")
    print("=" * 60)
    
    converter = ImageConverter(width=80)
    # ascii_art = converter.convert_image('sample.jpg')
    # print(ascii_art)
    print("Usage: converter.convert_image('your_image.jpg')\n")


def example_colored():
    """Colored ASCII art"""
    print("=" * 60)
    print("Example 2: Colored Output")
    print("=" * 60)
    
    converter = ImageConverter(width=100, color_mode=True, gamma=1.2)
    # ascii_art = converter.convert_image('sample.jpg')
    # print(ascii_art)
    print("Usage: ImageConverter(width=100, color_mode=True)\n")


def example_face_mode():
    """High-detail face mode"""
    print("=" * 60)
    print("Example 3: Face Recognition Mode")
    print("=" * 60)
    
    converter = ImageConverter(width=150)
    converter.set_mode_face()
    print("Face mode enabled with optimal settings:")
    print("- Width: 150+ characters")
    print("- Gamma: 1.5 (brightened)")
    print("- Ramp: Detailed character set")
    print("- Enhancement: Maximum\n")


def example_custom_ramp():
    """Custom character ramp"""
    print("=" * 60)
    print("Example 4: Custom Character Ramp")
    print("=" * 60)
    
    # Custom ramp from darkest to lightest
    custom_ramp = "█▓▒░ "
    converter = ImageConverter(width=80, ramp=custom_ramp)
    print(f"Using custom ramp: '{custom_ramp}'")
    print("Characters ordered from dark to light\n")


def example_emoji_mode():
    """Emoji mode with auto aspect correction"""
    print("=" * 60)
    print("Example 5: Emoji Mode")
    print("=" * 60)
    
    converter = CustomTextConverter(
        custom_text="🟦🟩🟨🟧🟥",
        width=60
    )
    print("Emoji mode automatically adjusts aspect ratio")
    print("Prevents emojis from looking squashed\n")


def example_gif_animation():
    """Animated GIF conversion"""
    print("=" * 60)
    print("Example 6: GIF Animation (Runs 5 Times)")
    print("=" * 60)
    
    converter = ImageConverter(width=80, color_mode=True)
    print("Usage: converter.convert_gif('animation.gif', fps=30, loop_count=5)")
    print("Animation will run 5 times then stop automatically")
    print("Press Ctrl+C to stop early\n")


def example_save_file():
    """Save ASCII art to file"""
    print("=" * 60)
    print("Example 7: Save to File")
    print("=" * 60)
    
    converter = ImageConverter(width=100)
    # ascii_art = converter.convert_image('sample.jpg')
    # converter.save_to_file(ascii_art, 'output.txt')
    print("Saves ASCII art to text file")
    print("ANSI color codes are automatically stripped\n")


def example_batch_processing():
    """Batch process multiple images"""
    print("=" * 60)
    print("Example 8: Batch Processing")
    print("=" * 60)
    
    from asciiforge import BatchConverter
    
    converter = ImageConverter(width=80, color_mode=True)
    batch = BatchConverter(converter)
    # batch.process_directory('input_dir/', 'output_dir/')
    print("Process entire directories of images")
    print("Supports: .jpg, .jpeg, .png, .gif, .bmp\n")


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("ASCII FORGE - IMAGE CONVERSION EXAMPLES")
    print("=" * 60 + "\n")
    
    example_basic()
    example_colored()
    example_face_mode()
    example_custom_ramp()
    example_emoji_mode()
    example_gif_animation()
    example_save_file()
    example_batch_processing()
    
    print("=" * 60)
    print("To run these examples with real images:")
    print("1. Uncomment the conversion lines")
    print("2. Provide your own image files")
    print("3. Run: python examples/example_image.py")
    print("=" * 60)