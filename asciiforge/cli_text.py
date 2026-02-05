#!/usr/bin/env python3
"""
ASCII Forge CLI - Text Artist
Command-line interface for styled text art and animations
"""

import argparse
import sys
from asciiforge import TextArtist, TextArtGallery


def main():
    parser = argparse.ArgumentParser(
        description='Create styled ASCII text art with animations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic styled text
  %(prog)s "HELLO" --font slant --color cyan
  %(prog)s "CYBER" --neon --color magenta
  %(prog)s "CHROME" --metal --font block
  
  # Animations (Ctrl+C to stop, or runs 5 loops by default)
  %(prog)s "WAVE" --wave --color blue --loops 3
  %(prog)s "HACKER" --decrypt --color green
  %(prog)s "NEWS" --marquee --speed 0.02
  
  # Save to file
  %(prog)s "TITLE" --neon -o title.txt
  
  # List available options
  %(prog)s --list-fonts
  %(prog)s --list-styles
        """
    )
    
    parser.add_argument('text', nargs='?', help='Text to convert')
    
    # Basic options
    parser.add_argument('-f', '--font', default='slant',
                       help='Font name (default: slant)')
    parser.add_argument('-c', '--color', default='white',
                       choices=TextArtist.list_colors(),
                       help='Text color')
    parser.add_argument('-o', '--output', help='Save to file')
    
    # Static styles
    style_group = parser.add_mutually_exclusive_group()
    style_group.add_argument('--neon', action='store_true',
                            help='Neon box border style')
    style_group.add_argument('--metal', action='store_true',
                            help='Chrome/metal gradient style')
    style_group.add_argument('--retro', action='store_true',
                            help='Retro CRT scanline style')
    style_group.add_argument('--shadow', action='store_true',
                            help='3D shadow/reflection style')
    style_group.add_argument('--galaxy', action='store_true',
                            help='Galaxy/starfield style')
    style_group.add_argument('--rainbow', action='store_true',
                            help='Rainbow color rows style')
    
    # Animations (mutually exclusive with styles)
    anim_group = parser.add_mutually_exclusive_group()
    anim_group.add_argument('--wave', action='store_true',
                           help='Sine wave motion animation')
    anim_group.add_argument('--flow', action='store_true',
                           help='RGB color flow animation')
    anim_group.add_argument('--glitch', action='store_true',
                           help='Cyberpunk glitch animation')
    anim_group.add_argument('--decrypt', action='store_true',
                           help='Matrix decrypt animation')
    anim_group.add_argument('--typewriter', action='store_true',
                           help='Typewriter print animation')
    anim_group.add_argument('--marquee', action='store_true',
                           help='Scrolling marquee animation')
    
    # Animation parameters
    parser.add_argument('--loops', type=int, default=5,
                       help='Animation loop count (default: 5)')
    parser.add_argument('--speed', type=float, default=0.04,
                       help='Animation speed (default: 0.04)')
    parser.add_argument('--direction', choices=['left', 'right'], default='left',
                       help='Marquee scroll direction')
    
    # Utility options
    parser.add_argument('--list-fonts', action='store_true',
                       help='List all available fonts')
    parser.add_argument('--list-styles', action='store_true',
                       help='List all available styles')
    parser.add_argument('--list-colors', action='store_true',
                       help='List all available colors')
    parser.add_argument('--showcase-styles', action='store_true',
                       help='Showcase all styles')
    parser.add_argument('--showcase-fonts', action='store_true',
                       help='Showcase sample fonts')
    
    args = parser.parse_args()
    
    # Handle list commands
    if args.list_fonts:
        fonts = TextArtist.list_fonts()
        print(f"Available fonts ({len(fonts)}):")
        for i, font in enumerate(fonts, 1):
            print(f"  {i:3d}. {font}")
        return
    
    if args.list_styles:
        styles = TextArtist.list_styles()
        print("Available styles:")
        for style in styles:
            print(f"  - {style}")
        return
    
    if args.list_colors:
        colors = TextArtist.list_colors()
        print("Available colors:")
        for color in colors:
            print(f"  - {color}")
        return
    
    if args.showcase_styles:
        text = args.text or "DEMO"
        TextArtGallery.showcase_styles(text, args.font)
        return
    
    if args.showcase_fonts:
        text = args.text or "ABC"
        TextArtGallery.showcase_fonts(text)
        return
    
    # Require text for actual conversion
    if not args.text:
        parser.error("text argument is required (unless using --list or --showcase)")
    
    try:
        # Create artist
        artist = TextArtist(args.text, font=args.font, color=args.color)
        
        # Determine style
        style = None
        if args.neon:
            style = 'neon'
        elif args.metal:
            style = 'metal'
        elif args.retro:
            style = 'retro'
        elif args.shadow:
            style = 'shadow'
        elif args.galaxy:
            style = 'galaxy'
        elif args.rainbow:
            style = 'rainbow'
        
        # Execute animations
        if args.wave:
            artist.animate_wave(loop_count=args.loops)
        elif args.flow:
            artist.animate_flow(loop_count=args.loops)
        elif args.glitch:
            artist.animate_glitch(loop_count=args.loops)
        elif args.decrypt:
            artist.animate_decrypt(duration=20)
        elif args.typewriter:
            artist.animate_typewriter(speed=0.005)
        elif args.marquee:
            artist.animate_marquee(
                speed=args.speed,
                direction=args.direction,
                loop_count=args.loops,
                style=style or 'normal'
            )
        else:
            # Static output
            if args.output:
                artist.save(args.output, style=style)
            else:
                artist.display(style=style)
    
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()