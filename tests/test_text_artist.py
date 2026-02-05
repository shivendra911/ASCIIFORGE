#!/usr/bin/env python3
"""
Unit tests for TextArtist class
"""

import pytest
import tempfile
import os
from asciiforge import TextArtist, TextArtGallery, Color


class TestColor:
    """Test Color class"""
    
    def test_get_color(self):
        """Test color retrieval"""
        from colorama import Fore
        assert Color.get('red') == Fore.RED
        assert Color.get('blue') == Fore.BLUE
    
    def test_default_color(self):
        """Test default color fallback"""
        from colorama import Fore
        result = Color.get('invalid_color')
        assert result == Fore.WHITE
    
    def test_list_colors(self):
        """Test color listing"""
        colors = Color.list_colors()
        assert isinstance(colors, list)
        assert 'red' in colors
        assert 'blue' in colors


class TestTextArtist:
    """Test TextArtist class"""
    
    def test_initialization(self):
        """Test artist initialization"""
        artist = TextArtist('TEST', font='slant', color='cyan')
        assert artist.text == 'TEST'
        assert artist.font == 'slant'
        assert artist.color == 'cyan'
    
    def test_generate_art(self):
        """Test art generation"""
        artist = TextArtist('A')
        art = artist._generate_art()
        assert isinstance(art, str)
        assert len(art) > 0
    
    def test_render_plain(self):
        """Test plain rendering"""
        artist = TextArtist('TEST')
        result = artist.render()
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_render_with_style(self):
        """Test rendering with style"""
        artist = TextArtist('TEST', color='red')
        styles = ['neon', 'metal', 'retro', 'shadow', 'galaxy', 'rainbow']
        
        for style in styles:
            result = artist.render(style=style)
            assert isinstance(result, str)
            assert len(result) > 0
    
    def test_list_fonts(self):
        """Test font listing"""
        fonts = TextArtist.list_fonts()
        assert isinstance(fonts, list)
        assert len(fonts) > 0
        assert 'slant' in fonts
    
    def test_list_styles(self):
        """Test style listing"""
        styles = TextArtist.list_styles()
        assert isinstance(styles, list)
        assert 'neon' in styles
        assert 'metal' in styles
        assert 'rainbow' in styles
    
    def test_list_colors(self):
        """Test color listing"""
        colors = TextArtist.list_colors()
        assert isinstance(colors, list)
        assert 'red' in colors
        assert 'blue' in colors
    
    def test_save_to_file(self):
        """Test saving to file"""
        artist = TextArtist('TEST', color='cyan')
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name
        
        try:
            artist.save(temp_path, style='neon')
            assert os.path.exists(temp_path)
            
            with open(temp_path, 'r') as f:
                content = f.read()
                assert len(content) > 0
                # Should not have ANSI codes
                assert '\033[' not in content
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


class TestStyles:
    """Test individual style classes"""
    
    def test_neon_style(self):
        """Test neon style"""
        from asciiforge.text_artist import NeonStyle
        style = NeonStyle()
        result = style.apply("TEST", "cyan")
        assert "+" in result  # Border character
        assert "|" in result  # Border character
    
    def test_metal_style(self):
        """Test metal style"""
        from asciiforge.text_artist import MetalStyle
        style = MetalStyle()
        result = style.apply("TEST\nTEST\nTEST", "cyan")
        assert len(result) > 0
    
    def test_retro_style(self):
        """Test retro style"""
        from asciiforge.text_artist import RetroStyle
        style = RetroStyle()
        result = style.apply("TEST\nTEST", "green")
        assert len(result) > 0
    
    def test_shadow_style(self):
        """Test shadow style"""
        from asciiforge.text_artist import ShadowStyle
        style = ShadowStyle()
        result = style.apply("TEST", "red")
        assert len(result) > 0
    
    def test_galaxy_style(self):
        """Test galaxy style"""
        from asciiforge.text_artist import GalaxyStyle
        style = GalaxyStyle()
        result = style.apply("TEST", "magenta")
        assert len(result) > 0
    
    def test_rainbow_style(self):
        """Test rainbow style"""
        from asciiforge.text_artist import RainbowStyle
        style = RainbowStyle()
        result = style.apply("TEST\nTEST", "white")
        assert len(result) > 0


class TestAnimations:
    """Test animation classes (non-interactive)"""
    
    def test_typewriter_animation_creation(self):
        """Test typewriter animation creation"""
        from asciiforge.text_artist import TypewriterAnimation
        anim = TypewriterAnimation('TEST', 'slant', 'green')
        assert anim.text == 'TEST'
        assert anim.font == 'slant'
        assert len(anim.art) > 0
    
    def test_decrypt_animation_creation(self):
        """Test decrypt animation creation"""
        from asciiforge.text_artist import DecryptAnimation
        anim = DecryptAnimation('TEST', 'slant', 'green')
        assert anim.text == 'TEST'
        assert len(anim.art) > 0
    
    def test_wave_animation_creation(self):
        """Test wave animation creation"""
        from asciiforge.text_artist import WaveAnimation
        anim = WaveAnimation('TEST', 'slant', 'blue')
        assert anim.text == 'TEST'
        assert len(anim.art) > 0
    
    def test_flow_animation_creation(self):
        """Test flow animation creation"""
        from asciiforge.text_artist import FlowAnimation
        anim = FlowAnimation('TEST', 'slant', 'white')
        assert anim.text == 'TEST'
        assert len(anim.art) > 0
    
    def test_glitch_animation_creation(self):
        """Test glitch animation creation"""
        from asciiforge.text_artist import GlitchAnimation
        anim = GlitchAnimation('TEST', 'slant', 'red')
        assert anim.text == 'TEST'
        assert len(anim.art) > 0
    
    def test_marquee_animation_creation(self):
        """Test marquee animation creation"""
        from asciiforge.text_artist import MarqueeAnimation
        anim = MarqueeAnimation('TEST', 'slant', 'cyan')
        assert anim.text == 'TEST'
        assert len(anim.art) > 0


class TestTextArtGallery:
    """Test TextArtGallery utility class"""
    
    def test_showcase_styles_exists(self):
        """Test showcase_styles method exists"""
        assert hasattr(TextArtGallery, 'showcase_styles')
    
    def test_showcase_fonts_exists(self):
        """Test showcase_fonts method exists"""
        assert hasattr(TextArtGallery, 'showcase_fonts')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])