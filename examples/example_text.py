#!/usr/bin/env python3
"""
Example: Text Art and Animations
Demonstrates styled text art and animation features
"""

from asciiforge import TextArtist, TextArtGallery
import time


def example_basic():
    """Basic text art"""
    print("\n" + "=" * 60)
    print("Example 1: Basic Text Art")
    print("=" * 60 + "\n")
    
    artist = TextArtist('HELLO', font='slant', color='cyan')
    artist.display()


def example_styles():
    """All static styles"""
    print("\n" + "=" * 60)
    print("Example 2: Static Styles")
    print("=" * 60 + "\n")
    
    styles = ['neon', 'metal', 'retro', 'shadow', 'galaxy', 'rainbow']
    
    for style in styles:
        print(f"\nStyle: {style.upper()}")
        print("-" * 40)
        artist = TextArtist('STYLE', font='slant', color='cyan')
        artist.display(style=style)
        time.sleep(0.5)


def example_fonts():
    """Different fonts"""
    print("\n" + "=" * 60)
    print("Example 3: Different Fonts")
    print("=" * 60 + "\n")
    
    fonts = ['slant', 'block', 'banner', 'digital', 'bubble']
    
    for font in fonts:
        print(f"\nFont: {font}")
        print("-" * 40)
        artist = TextArtist('ABC', font=font, color='white')
        artist.display()
        time.sleep(0.3)


def example_colors():
    """Different colors"""
    print("\n" + "=" * 60)
    print("Example 4: Color Palette")
    print("=" * 60 + "\n")
    
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    
    for color in colors:
        artist = TextArtist(color.upper(), font='small', color=color)
        artist.display()


def example_typewriter():
    """Typewriter animation"""
    print("\n" + "=" * 60)
    print("Example 5: Typewriter Animation")
    print("=" * 60 + "\n")
    
    artist = TextArtist('TYPE', font='slant', color='green')
    artist.animate_typewriter(speed=0.005)


def example_decrypt():
    """Matrix decrypt animation"""
    print("\n" + "=" * 60)
    print("Example 6: Decrypt Animation")
    print("=" * 60 + "\n")
    
    artist = TextArtist('DECRYPT', font='slant', color='green')
    artist.animate_decrypt(duration=15)


def example_wave():
    """Wave motion animation (runs 3 times)"""
    print("\n" + "=" * 60)
    print("Example 7: Wave Animation (3 loops)")
    print("=" * 60 + "\n")
    print("Press Ctrl+C to stop early\n")
    
    try:
        artist = TextArtist('WAVE', font='banner', color='blue')
        artist.animate_wave(loop_count=3)
    except KeyboardInterrupt:
        print("\nStopped by user.")


def example_flow():
    """RGB flow animation (runs 3 times)"""
    print("\n" + "=" * 60)
    print("Example 8: RGB Flow Animation (3 loops)")
    print("=" * 60 + "\n")
    print("Press Ctrl+C to stop early\n")
    
    try:
        artist = TextArtist('FLOW', font='slant')
        artist.animate_flow(loop_count=3)
    except KeyboardInterrupt:
        print("\nStopped by user.")


def example_glitch():
    """Glitch animation (runs 3 times)"""
    print("\n" + "=" * 60)
    print("Example 9: Glitch Animation (3 loops)")
    print("=" * 60 + "\n")
    print("Press Ctrl+C to stop early\n")
    
    try:
        artist = TextArtist('GLITCH', font='slant', color='red')
        artist.animate_glitch(loop_count=3)
    except KeyboardInterrupt:
        print("\nStopped by user.")


def example_marquee():
    """Marquee scroll animation (runs 3 times)"""
    print("\n" + "=" * 60)
    print("Example 10: Marquee Animation (3 loops)")
    print("=" * 60 + "\n")
    print("Press Ctrl+C to stop early\n")
    
    try:
        artist = TextArtist('BREAKING NEWS', font='banner', color='red')
        artist.animate_marquee(speed=0.03, direction='left', loop_count=3)
    except KeyboardInterrupt:
        print("\nStopped by user.")


def example_save():
    """Save to file"""
    print("\n" + "=" * 60)
    print("Example 11: Save to File")
    print("=" * 60 + "\n")
    
    artist = TextArtist('TITLE', font='banner', color='cyan')
    # artist.save('output_text.txt', style='neon')
    print("Usage: artist.save('filename.txt', style='neon')")
    print("ANSI color codes are automatically stripped")


def example_showcase():
    """Showcase all styles"""
    print("\n" + "=" * 60)
    print("Example 12: Style Showcase")
    print("=" * 60 + "\n")
    
    print("Usage: TextArtGallery.showcase_styles('TEXT', 'slant')")
    print("Displays all available styles sequentially")


def interactive_menu():
    """Interactive menu for running examples"""
    print("\n" + "=" * 60)
    print("ASCII FORGE - TEXT ART EXAMPLES")
    print("=" * 60)
    
    examples = [
        ("Basic Text Art", example_basic),
        ("Static Styles", example_styles),
        ("Different Fonts", example_fonts),
        ("Color Palette", example_colors),
        ("Typewriter Animation", example_typewriter),
        ("Decrypt Animation", example_decrypt),
        ("Wave Animation (3 loops)", example_wave),
        ("RGB Flow Animation (3 loops)", example_flow),
        ("Glitch Animation (3 loops)", example_glitch),
        ("Marquee Animation (3 loops)", example_marquee),
        ("Save to File", example_save),
        ("Run All Examples", None),
    ]
    
    print("\nSelect an example to run:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i:2d}. {name}")
    print("   0. Exit")
    
    while True:
        try:
            choice = input("\nEnter choice (0-12): ").strip()
            
            if choice == '0':
                print("Goodbye!")
                break
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(examples):
                if choice_num == len(examples):
                    # Run all
                    for name, func in examples[:-1]:
                        if func:
                            func()
                            time.sleep(1)
                else:
                    _, func = examples[choice_num - 1]
                    if func:
                        func()
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break


if __name__ == '__main__':
    import sys
    
    # If run with --all flag, run all examples
    if len(sys.argv) > 1 and sys.argv[1] == '--all':
        print("\n" + "=" * 60)
        print("ASCII FORGE - RUNNING ALL TEXT ART EXAMPLES")
        print("=" * 60)
        
        example_basic()
        example_styles()
        example_fonts()
        example_colors()
        example_typewriter()
        example_decrypt()
        
        print("\n" + "=" * 60)
        print("Animated examples require user interaction")
        print("Run individual examples for animations")
        print("=" * 60)
    else:
        # Interactive menu
        interactive_menu()