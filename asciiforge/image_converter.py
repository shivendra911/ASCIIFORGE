#!/usr/bin/env python3
"""
ASCII Forge - Image to ASCII Converter Module
Professional OOP implementation with advanced features
"""

import sys
import time
import os
from typing import Optional, List, Tuple
from PIL import Image, ImageOps, ImageFilter, ImageSequence
import unicodedata


class ImageConverter:
    """
    Converts images and GIFs to ASCII art with multiple rendering modes.
    
    Features:
    - High detail grayscale (default)
    - Colored output
    - Emoji mode with auto aspect correction
    - Face recognition mode (high detail)
    - Custom character ramps
    - Animation support with configurable loops
    - File saving
    """
    
    # Character ramps from darkest to lightest
    RAMP_STANDARD = "@%#*+=-:. "
    RAMP_DETAILED = "@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    RAMP_SIMPLE = "@#*+=-:. "
    RAMP_BLOCKS = "█▓▒░ "
    
    def __init__(
        self,
        width: int = 100,
        color_mode: bool = False,
        gamma: float = 1.0,
        ramp: Optional[str] = None,
        aspect_ratio: float = 0.55,
        enhance: bool = True
    ):
        """
        Initialize the ASCII converter.
        
        Args:
            width: Character width of output (higher = more detail)
            color_mode: Enable colored output
            gamma: Brightness adjustment (>1.0 brightens, <1.0 darkens)
            ramp: Custom character ramp (darkest to lightest)
            aspect_ratio: Height/width ratio compensation for text
            enhance: Apply preprocessing filters
        """
        self.width = width
        self.color_mode = color_mode
        self.gamma = gamma
        self.ramp = ramp or self.RAMP_STANDARD
        self.aspect_ratio = aspect_ratio
        self.enhance = enhance
        self._is_emoji_mode = False
        
    def _rgb_to_ansi(self, r: int, g: int, b: int, char: str) -> str:
        """Convert RGB values to ANSI colored character."""
        return f"\033[38;2;{r};{g};{b}m{char}\033[0m"
    
    def _detect_emoji(self, text: str) -> bool:
        """Detect if input contains emoji characters."""
        for char in text:
            if unicodedata.category(char) == 'So':  # Symbol, other
                return True
        return False
    
    def _preprocess_image(self, img: Image.Image) -> Image.Image:
        """
        Apply preprocessing to enhance ASCII quality.
        
        Args:
            img: Input PIL Image
            
        Returns:
            Preprocessed grayscale image
        """
        img = img.convert("L")
        
        if self.enhance:
            # Auto-contrast to enhance features
            img = ImageOps.autocontrast(img, cutoff=2)
            
            # Gamma correction for brightness control
            if self.gamma != 1.0:
                img = img.point(lambda p: ((p / 255.0) ** (1.0 / self.gamma)) * 255)
            
            # Sharpen for better definition
            img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150))
        
        return img
    
    def _resize_image(self, img: Image.Image) -> Image.Image:
        """Resize image maintaining aspect ratio for text display."""
        orig_w, orig_h = img.size
        aspect = self.aspect_ratio
        
        # Emoji mode needs different aspect ratio
        if self._is_emoji_mode:
            aspect = 0.5  # Taller to prevent squashing
            
        new_h = int((orig_h / orig_w) * self.width * aspect)
        return img.resize((self.width, new_h), Image.Resampling.LANCZOS)
    
    def _map_pixel_to_char(self, brightness: int) -> str:
        """Map brightness value to character from ramp."""
        ramp_max = len(self.ramp) - 1
        idx = int((brightness / 255) * ramp_max)
        return self.ramp[idx]
    
    def generate_frame(self, img: Image.Image) -> str:
        """
        Generate ASCII art from a single image frame.
        
        Args:
            img: PIL Image object
            
        Returns:
            ASCII art string
        """
        # Process grayscale version for character mapping
        img_gray = self._preprocess_image(img)
        img_gray = self._resize_image(img_gray)
        pixels_gray = list(img_gray.getdata())
        
        # Get color data if needed
        pixels_color = None
        if self.color_mode:
            img_color = img.convert("RGB")
            img_color = self._resize_image(img_color)
            pixels_color = list(img_color.getdata())
        
        # Build ASCII string
        ascii_lines = []
        w, h = img_gray.size
        
        for i, brightness in enumerate(pixels_gray):
            char = self._map_pixel_to_char(brightness)
            
            if self.color_mode and pixels_color:
                r, g, b = pixels_color[i]
                char = self._rgb_to_ansi(r, g, b, char)
            
            ascii_lines.append(char)
            
            if (i + 1) % w == 0:
                ascii_lines.append("\n")
        
        return "".join(ascii_lines)
    
    def convert_image(self, image_path: str) -> str:
        """
        Convert a static image to ASCII art.
        
        Args:
            image_path: Path to image file
            
        Returns:
            ASCII art string
        """
        try:
            img = Image.open(image_path)
            return self.generate_frame(img)
        except Exception as e:
            raise RuntimeError(f"Failed to convert image: {e}")
    
    def convert_gif(
        self,
        gif_path: str,
        fps: int = 30,
        loop_count: int = 5,
        display: bool = True
    ) -> List[str]:
        """
        Convert animated GIF to ASCII animation.
        
        Args:
            gif_path: Path to GIF file
            fps: Frames per second for playback
            loop_count: Number of times to loop (0 = infinite)
            display: If True, display animation in terminal
            
        Returns:
            List of ASCII frame strings
        """
        try:
            img = Image.open(gif_path)
            
            if not img.is_animated:
                return [self.generate_frame(img)]
            
            # Pre-render all frames
            print("Pre-rendering frames...")
            frames = []
            for frame in ImageSequence.Iterator(img):
                frames.append(self.generate_frame(frame))
            
            if display:
                self._play_animation(frames, fps, loop_count)
            
            return frames
            
        except Exception as e:
            raise RuntimeError(f"Failed to convert GIF: {e}")
    
    def _play_animation(self, frames: List[str], fps: int, loop_count: int):
        """Play ASCII animation in terminal."""
        print(f"\nPlaying {len(frames)} frames at {fps} FPS")
        print(f"Loops: {'infinite' if loop_count == 0 else loop_count}")
        print("(Press Ctrl+C to stop)\n")
        
        # Hide cursor
        sys.stdout.write("\033[?25l")
        
        loops_played = 0
        try:
            while loop_count == 0 or loops_played < loop_count:
                for frame in frames:
                    sys.stdout.write("\033[H")  # Move cursor home
                    sys.stdout.write(frame)
                    sys.stdout.flush()
                    time.sleep(1.0 / fps)
                
                loops_played += 1
                
        except KeyboardInterrupt:
            pass
        finally:
            # Show cursor
            sys.stdout.write("\033[?25h")
            print("\nAnimation stopped.")
    
    def save_to_file(self, content: str, output_path: str):
        """
        Save ASCII art to text file.
        
        Args:
            content: ASCII art string
            output_path: Output file path
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                # Strip ANSI codes if saving colored output
                if self.color_mode:
                    import re
                    content = re.sub(r'\033\[[0-9;]+m', '', content)
                f.write(content)
            print(f"Saved to: {output_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to save file: {e}")
    
    def set_mode_emoji(self):
        """Enable emoji mode with adjusted aspect ratio."""
        self._is_emoji_mode = True
        self.aspect_ratio = 0.5
        self.ramp = "🟦🟩🟨🟧🟥"  # Can be customized
        
    def set_mode_face(self):
        """Enable face/detail mode with optimal settings."""
        self.width = max(self.width, 150)
        self.gamma = 1.5
        self.ramp = self.RAMP_DETAILED
        self.enhance = True
        
    def set_mode_simple(self):
        """Enable simple/minimal mode."""
        self.ramp = self.RAMP_SIMPLE
        self.enhance = False


class CustomTextConverter(ImageConverter):
    """
    Extended converter supporting custom text input as character source.
    """
    
    def __init__(self, custom_text: str, **kwargs):
        """
        Initialize with custom text as the character ramp.
        
        Args:
            custom_text: Text to use as character source (dark to light order)
            **kwargs: Additional ImageConverter arguments
        """
        if not custom_text or len(custom_text) < 2:
            raise ValueError("Custom text must have at least 2 characters")
        
        # Detect if text contains emojis
        is_emoji = self._detect_emoji(custom_text)
        
        super().__init__(ramp=custom_text, **kwargs)
        
        if is_emoji:
            self.set_mode_emoji()


class BatchConverter:
    """
    Batch process multiple images with the same settings.
    """
    
    def __init__(self, converter: ImageConverter):
        """
        Initialize batch processor.
        
        Args:
            converter: Configured ImageConverter instance
        """
        self.converter = converter
        
    def process_directory(
        self,
        input_dir: str,
        output_dir: str,
        extensions: Tuple[str, ...] = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    ):
        """
        Process all images in a directory.
        
        Args:
            input_dir: Input directory path
            output_dir: Output directory path
            extensions: Tuple of valid file extensions
        """
        os.makedirs(output_dir, exist_ok=True)
        
        files = [f for f in os.listdir(input_dir) 
                if f.lower().endswith(extensions)]
        
        print(f"Processing {len(files)} files...")
        
        for filename in files:
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{filename}.txt")
            
            try:
                ascii_art = self.converter.convert_image(input_path)
                self.converter.save_to_file(ascii_art, output_path)
                print(f"✓ {filename}")
            except Exception as e:
                print(f"✗ {filename}: {e}")