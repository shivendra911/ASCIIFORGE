#!/usr/bin/env python3
"""
ASCII Forge - Text Art Generator Module
Professional OOP implementation with styles and animations
"""

import sys
import time
import math
import random
import shutil
from typing import Optional, List, Callable
from abc import ABC, abstractmethod

try:
    import pyfiglet
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError as e:
    print("Error: Missing required libraries.")
    print("Run: pip install pyfiglet colorama")
    sys.exit(1)


class Color:
    """Color palette manager."""
    
    PALETTE = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        'black': Fore.BLACK,
    }
    
    @classmethod
    def get(cls, name: str, default=Fore.WHITE):
        """Get color by name."""
        return cls.PALETTE.get(name.lower(), default)
    
    @classmethod
    def list_colors(cls) -> List[str]:
        """Get list of available color names."""
        return list(cls.PALETTE.keys())


class Style_Base(ABC):
    """Abstract base class for text styles."""
    
    @abstractmethod
    def apply(self, art: str, color: str) -> str:
        """Apply style to ASCII art."""
        pass


class NeonStyle(Style_Base):
    """Neon box border style."""
    
    def apply(self, art: str, color: str) -> str:
        lines = art.split('\n')
        width = max(len(line) for line in lines) if lines else 0
        c = Color.get(color)
        
        border_top = c + "+" + "-" * (width + 2) + "+"
        border_bot = c + "+" + "-" * (width + 2) + "+"
        
        out = [border_top]
        for line in lines:
            padding = " " * (width - len(line))
            out.append(f"{c}| {Fore.WHITE}{line}{padding} {c}|")
        out.append(border_bot)
        
        return "\n".join(out)


class MetalStyle(Style_Base):
    """Chrome/metal gradient style."""
    
    def apply(self, art: str, color: str) -> str:
        lines = art.split('\n')
        out = []
        mid = len(lines) // 2
        
        for i, line in enumerate(lines):
            if i == 0 or i == len(lines) - 1:
                col = Fore.WHITE + Style.BRIGHT
            elif i == mid:
                col = Fore.LIGHTBLACK_EX
            else:
                col = Fore.CYAN
            out.append(col + line)
        
        return "\n".join(out)


class RetroStyle(Style_Base):
    """Retro CRT scanline style."""
    
    def apply(self, art: str, color: str) -> str:
        lines = art.split('\n')
        out = []
        
        for i, line in enumerate(lines):
            if i % 2 == 0:
                out.append(Fore.GREEN + Style.BRIGHT + line)
            else:
                out.append(Fore.GREEN + Style.DIM + line)
        
        return "\n".join(out)


class ShadowStyle(Style_Base):
    """3D shadow/reflection style."""
    
    def apply(self, art: str, color: str) -> str:
        lines = art.split('\n')
        out = []
        c = Color.get(color)
        
        # Main text
        out.append(c + Style.BRIGHT + art.rstrip())
        
        # Shadow layer
        for line in lines:
            shadow_line = line.replace('#', '/').replace('@', '%')
            out.append(Fore.LIGHTBLACK_EX + shadow_line)
        
        return "\n".join(out)


class GalaxyStyle(Style_Base):
    """Galaxy/starfield background style."""
    
    def apply(self, art: str, color: str) -> str:
        lines = art.split('\n')
        out = []
        stars = [".", ",", "*", "°", "+"]
        
        for line in lines:
            new_line = ""
            for char in line:
                if char == " ":
                    if random.random() < 0.1:
                        new_line += Fore.LIGHTBLACK_EX + random.choice(stars)
                    else:
                        new_line += " "
                else:
                    new_line += Fore.MAGENTA + Style.BRIGHT + char
            out.append(new_line)
        
        return "\n".join(out)


class RainbowStyle(Style_Base):
    """Rainbow color rows style."""
    
    def apply(self, art: str, color: str) -> str:
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, 
                 Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        lines = art.split('\n')
        out = []
        
        for i, line in enumerate(lines):
            c = colors[i % len(colors)]
            out.append(c + line)
        
        return "\n".join(out)


class Animation_Base(ABC):
    """Abstract base class for animations."""
    
    def __init__(self, text: str, font: str, color: str):
        self.text = text
        self.font = font
        self.color = Color.get(color)
        self.art = self._generate_art()
        
    def _generate_art(self) -> str:
        """Generate base ASCII art."""
        try:
            return pyfiglet.figlet_format(self.text, font=self.font)
        except:
            return pyfiglet.figlet_format(self.text)
    
    @abstractmethod
    def play(self, **kwargs):
        """Play the animation."""
        pass


class TypewriterAnimation(Animation_Base):
    """Typewriter effect animation."""
    
    def play(self, speed: float = 0.005):
        """Print text character by character."""
        print(self.color + Style.BRIGHT, end="")
        for char in self.art:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed + random.uniform(0, 0.005))
        print(Style.RESET_ALL)


class DecryptAnimation(Animation_Base):
    """Matrix-style decrypt animation."""
    
    def play(self, duration: int = 20):
        """Decode random characters into final text."""
        lines = self.art.split('\n')
        height = len(lines)
        garbage_chars = "10@#$%&*"
        
        print("\n" * height)  # Reserve space
        
        # Garbage phase
        for _ in range(duration):
            sys.stdout.write(f"\033[{height}A")  # Move up
            for line in lines:
                g_line = ""
                for c in line:
                    if c == " ":
                        g_line += " "
                    else:
                        g_line += random.choice(garbage_chars)
                print(Fore.GREEN + g_line)
            time.sleep(0.05)
        
        # Reveal
        sys.stdout.write(f"\033[{height}A")
        print(self.color + self.art + Style.RESET_ALL)


class WaveAnimation(Animation_Base):
    """Sine wave motion animation."""
    
    def play(self, loop_count: int = 5):
        """Animate text with wave motion."""
        lines = self.art.split('\n')
        t = 0.0
        loops = 0
        
        try:
            while loops < loop_count:
                buffer = "\033[H"  # Home position
                for i, line in enumerate(lines):
                    offset = int(10 * math.sin(i * 0.5 + t)) + 15
                    space = " " * max(0, offset)
                    buffer += self.color + space + line + "\n"
                
                sys.stdout.write(buffer)
                sys.stdout.flush()
                
                t += 0.2
                time.sleep(0.05)
                
                # Count loops (rough estimate)
                if t > 2 * math.pi:
                    loops += 1
                    t = 0.0
                    
        except KeyboardInterrupt:
            print("\nStopped.")


class FlowAnimation(Animation_Base):
    """RGB color flow animation."""
    
    def play(self, loop_count: int = 5):
        """Animate rainbow colors flowing through text."""
        lines = self.art.split('\n')
        palette = [Fore.RED, Fore.YELLOW, Fore.GREEN, 
                  Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        offset = 0
        frames = 0
        max_frames = loop_count * 60  # Approximate
        
        try:
            while frames < max_frames:
                buffer = "\033[H"
                for line in lines:
                    row = ""
                    for i, char in enumerate(line):
                        c = palette[(i + offset) % len(palette)]
                        row += c + char
                    buffer += row + "\n"
                
                sys.stdout.write(buffer)
                sys.stdout.flush()
                
                offset += 1
                frames += 1
                time.sleep(0.05)
                
        except KeyboardInterrupt:
            print("\nStopped.")


class GlitchAnimation(Animation_Base):
    """Cyberpunk glitch animation."""
    
    def play(self, loop_count: int = 5):
        """Animate glitchy corrupted text."""
        lines = self.art.split('\n')
        noise = ["@", "#", "$", "%", "&"]
        frames = 0
        max_frames = loop_count * 30
        
        try:
            while frames < max_frames:
                buffer = "\033[H"
                shake = random.choice([0, 2])
                indent = " " * (5 + shake)
                
                for line in lines:
                    new_line = ""
                    for char in line:
                        if char != " " and random.random() < 0.05:
                            new_line += Fore.WHITE + random.choice(noise)
                        else:
                            new_line += self.color + char
                    buffer += indent + new_line + "\n"
                
                sys.stdout.write(buffer)
                sys.stdout.flush()
                
                frames += 1
                time.sleep(0.08)
                
        except KeyboardInterrupt:
            print("\nStopped.")


class MarqueeAnimation(Animation_Base):
    """Scrolling marquee animation."""
    
    def play(self, speed: float = 0.04, direction: str = 'left', 
             loop_count: int = 5, style_name: str = 'normal'):
        """Scroll text across screen."""
        lines = self.art.split('\n')
        max_w = max(len(l) for l in lines)
        fixed_lines = [line.ljust(max_w) for line in lines]
        
        term_w = shutil.get_terminal_size().columns
        padding = " " * term_w
        
        scroll_buffer = [(padding + line + padding) for line in fixed_lines]
        total_len = len(scroll_buffer[0])
        
        offset = 0
        loops = 0
        sys.stdout.write("\033[?25l")  # Hide cursor
        
        try:
            while loops < loop_count:
                frame = "\033[H"
                
                if offset >= total_len - term_w:
                    offset = 0
                    loops += 1
                
                for line in scroll_buffer:
                    slice_txt = line[offset: offset + term_w]
                    
                    # Apply style
                    if style_name == 'retro':
                        frame += Fore.GREEN + Style.DIM + slice_txt + "\n"
                    elif style_name == 'metal':
                        frame += Fore.CYAN + slice_txt + "\n"
                    elif style_name == 'neon':
                        frame += Fore.MAGENTA + slice_txt + "\n"
                    else:
                        frame += self.color + slice_txt + "\n"
                
                sys.stdout.write(frame)
                sys.stdout.flush()
                
                if direction == 'left':
                    offset += 1
                else:
                    offset -= 1
                    if offset < 0:
                        offset = total_len - term_w - 1
                
                time.sleep(speed)
                
        except KeyboardInterrupt:
            pass
        finally:
            sys.stdout.write("\033[?25h")  # Show cursor
            print("\nStopped.")


class TextArtist:
    """
    Main class for creating styled ASCII text art.
    
    Features:
    - Multiple fonts via pyfiglet
    - Static styles (neon, metal, retro, shadow, galaxy, rainbow)
    - Animations (wave, flow, glitch, decrypt, typewriter, marquee)
    - Custom colors
    - Loop control for animations
    """
    
    STYLES = {
        'neon': NeonStyle(),
        'metal': MetalStyle(),
        'retro': RetroStyle(),
        'shadow': ShadowStyle(),
        'galaxy': GalaxyStyle(),
        'rainbow': RainbowStyle(),
    }
    
    def __init__(self, text: str, font: str = 'slant', color: str = 'white'):
        """
        Initialize TextArtist.
        
        Args:
            text: Text to convert
            font: Font name (e.g., 'slant', 'block', 'banner')
            color: Color name
        """
        self.text = text
        self.font = font
        self.color = color
        self._art = None
        
    def _generate_art(self) -> str:
        """Generate base ASCII art."""
        if self._art is None:
            try:
                self._art = pyfiglet.figlet_format(self.text, font=self.font)
            except:
                self._art = pyfiglet.figlet_format(self.text)
        return self._art
    
    def render(self, style: Optional[str] = None) -> str:
        """
        Render text with optional style.
        
        Args:
            style: Style name ('neon', 'metal', 'retro', etc.)
            
        Returns:
            Styled ASCII art string
        """
        art = self._generate_art()
        
        if style and style in self.STYLES:
            return self.STYLES[style].apply(art, self.color)
        else:
            # Default: just apply color
            return Color.get(self.color) + art
    
    def display(self, style: Optional[str] = None):
        """Display ASCII art in terminal."""
        print(self.render(style))
    
    def save(self, filepath: str, style: Optional[str] = None):
        """Save ASCII art to file."""
        import re
        content = self.render(style)
        # Strip ANSI codes
        content = re.sub(r'\033\[[0-9;]+m', '', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved to: {filepath}")
    
    def animate_typewriter(self, speed: float = 0.005):
        """Play typewriter animation."""
        anim = TypewriterAnimation(self.text, self.font, self.color)
        anim.play(speed=speed)
    
    def animate_decrypt(self, duration: int = 20):
        """Play decrypt animation."""
        anim = DecryptAnimation(self.text, self.font, self.color)
        anim.play(duration=duration)
    
    def animate_wave(self, loop_count: int = 5):
        """Play wave animation."""
        sys.stdout.write("\033[2J\033[H")  # Clear screen
        anim = WaveAnimation(self.text, self.font, self.color)
        anim.play(loop_count=loop_count)
    
    def animate_flow(self, loop_count: int = 5):
        """Play RGB flow animation."""
        sys.stdout.write("\033[2J\033[H")  # Clear screen
        anim = FlowAnimation(self.text, self.font, self.color)
        anim.play(loop_count=loop_count)
    
    def animate_glitch(self, loop_count: int = 5):
        """Play glitch animation."""
        sys.stdout.write("\033[2J\033[H")  # Clear screen
        anim = GlitchAnimation(self.text, self.font, self.color)
        anim.play(loop_count=loop_count)
    
    def animate_marquee(self, speed: float = 0.04, direction: str = 'left',
                       loop_count: int = 5, style: str = 'normal'):
        """Play marquee scrolling animation."""
        sys.stdout.write("\033[2J\033[H")  # Clear screen
        anim = MarqueeAnimation(self.text, self.font, self.color)
        anim.play(speed=speed, direction=direction, 
                 loop_count=loop_count, style_name=style)
    
    @staticmethod
    def list_fonts() -> List[str]:
        """Get list of available fonts."""
        return pyfiglet.FigletFont.getFonts()
    
    @staticmethod
    def list_colors() -> List[str]:
        """Get list of available colors."""
        return Color.list_colors()
    
    @staticmethod
    def list_styles() -> List[str]:
        """Get list of available styles."""
        return list(TextArtist.STYLES.keys())


class TextArtGallery:
    """
    Utility class for showcasing different styles/fonts.
    """
    
    @staticmethod
    def showcase_styles(text: str = "DEMO", font: str = 'slant'):
        """Display all available styles."""
        artist = TextArtist(text, font)
        styles = TextArtist.list_styles()
        
        for style_name in styles:
            print(f"\n{'=' * 60}")
            print(f"Style: {style_name.upper()}")
            print('=' * 60)
            artist.display(style=style_name)
            time.sleep(0.5)
    
    @staticmethod
    def showcase_fonts(text: str = "ABC", max_fonts: int = 10):
        """Display sample of available fonts."""
        fonts = TextArtist.list_fonts()[:max_fonts]
        artist = TextArtist(text)
        
        for font_name in fonts:
            print(f"\n{'=' * 60}")
            print(f"Font: {font_name}")
            print('=' * 60)
            artist.font = font_name
            artist._art = None  # Reset cache
            artist.display()
            time.sleep(0.3)