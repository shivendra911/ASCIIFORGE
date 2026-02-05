#!/usr/bin/env python3
"""
ASCII Forge CLI - Image Converter
Command-line interface for image to ASCII conversion
"""

import argparse
import sys
from asciiforge import ImageConverter, CustomTextConverter, BatchConverter


def main():
    parser = argparse.ArgumentParser(
        description='Convert images to ASCII art',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s photo.jpg -w 100 -c
  %(prog)s animation.gif --fps 30 --loops 5
  %(prog)s face.jpg --face -w 150 -o output.txt
  %(prog)s emoji.png --emoji
  %(prog)s image.jpg --custom "@#*+. " -c
        """
    )
    
    parser.add_argument('image', help='Image or GIF path')
    
    # Basic options
    parser.add_argument('-w', '--width', type=int, default=100,
                       help='Character width (default: 100, face mode: 150+)')
    parser.add_argument('-c', '--color', action='store_true',
                       help='Enable colored output')
    parser.add_argument('-o', '--output', help='Save to file')
    
    # Image processing
    parser.add_argument('-g', '--gamma', type=float, default=1.0,
                       help='Gamma correction (>1.0 brightens, <1.0 darkens)')
    parser.add_argument('--no-enhance', action='store_true',
                       help='Disable image enhancement')
    
    # Modes
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('--face', action='store_true',
                           help='Face/high-detail mode (optimal settings)')
    mode_group.add_argument('--emoji', action='store_true',
                           help='Emoji mode (auto aspect correction)')
    mode_group.add_argument('--simple', action='store_true',
                           help='Simple/minimal mode')
    
    # Character ramp
    parser.add_argument('--custom', help='Custom character ramp (dark to light)')
    parser.add_argument('--ramp', choices=['standard', 'detailed', 'simple', 'blocks'],
                       default='standard', help='Pre-defined character ramp')
    
    # GIF options
    parser.add_argument('--fps', type=int, default=30,
                       help='GIF playback FPS (default: 30)')
    parser.add_argument('--loops', type=int, default=5,
                       help='Animation loop count (0 = infinite, default: 5)')
    parser.add_argument('--no-display', action='store_true',
                       help='Pre-render GIF frames but do not display')
    
    # Batch processing
    parser.add_argument('--batch', metavar='OUTPUT_DIR',
                       help='Batch process directory (use with image as input dir)')
    
    args = parser.parse_args()
    
    try:
        # Create converter
        if args.custom:
            converter = CustomTextConverter(
                custom_text=args.custom,
                width=args.width,
                color_mode=args.color,
                gamma=args.gamma,
                enhance=not args.no_enhance
            )
        else:
            converter = ImageConverter(
                width=args.width,
                color_mode=args.color,
                gamma=args.gamma,
                enhance=not args.no_enhance
            )
            
            # Set ramp
            if args.ramp == 'detailed':
                converter.ramp = ImageConverter.RAMP_DETAILED
            elif args.ramp == 'simple':
                converter.ramp = ImageConverter.RAMP_SIMPLE
            elif args.ramp == 'blocks':
                converter.ramp = ImageConverter.RAMP_BLOCKS
        
        # Apply mode presets
        if args.face:
            converter.set_mode_face()
            print("Face mode enabled: width=150+, gamma=1.5, detailed ramp")
        elif args.emoji:
            converter.set_mode_emoji()
            print("Emoji mode enabled: aspect ratio adjusted")
        elif args.simple:
            converter.set_mode_simple()
            print("Simple mode enabled")
        
        # Batch processing
        if args.batch:
            batch = BatchConverter(converter)
            batch.process_directory(args.image, args.batch)
            return
        
        # Check if GIF
        is_gif = args.image.lower().endswith('.gif')
        
        if is_gif:
            frames = converter.convert_gif(
                args.image,
                fps=args.fps,
                loop_count=args.loops,
                display=not args.no_display
            )
            
            if args.output:
                # Save all frames to separate files
                import os
                base, ext = os.path.splitext(args.output)
                for i, frame in enumerate(frames):
                    output_path = f"{base}_frame{i:04d}.txt"
                    converter.save_to_file(frame, output_path)
                print(f"Saved {len(frames)} frames")
        else:
            # Static image
            ascii_art = converter.convert_image(args.image)
            
            if args.output:
                converter.save_to_file(ascii_art, args.output)
            else:
                print(ascii_art)
    
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()