#!/usr/bin/env python3
"""
Unit tests for ImageConverter class
"""

import pytest
from PIL import Image
import tempfile
import os
from asciiforge import ImageConverter, CustomTextConverter, BatchConverter


class TestImageConverter:
    """Test ImageConverter class"""
    
    def test_initialization(self):
        """Test converter initialization"""
        converter = ImageConverter(width=100, color_mode=True, gamma=1.5)
        assert converter.width == 100
        assert converter.color_mode == True
        assert converter.gamma == 1.5
        assert converter.ramp == ImageConverter.RAMP_STANDARD
    
    def test_ramp_types(self):
        """Test different character ramps"""
        ramps = [
            ImageConverter.RAMP_STANDARD,
            ImageConverter.RAMP_DETAILED,
            ImageConverter.RAMP_SIMPLE,
            ImageConverter.RAMP_BLOCKS,
        ]
        for ramp in ramps:
            converter = ImageConverter(ramp=ramp)
            assert converter.ramp == ramp
    
    def test_mode_face(self):
        """Test face mode preset"""
        converter = ImageConverter(width=50)
        converter.set_mode_face()
        assert converter.width >= 150
        assert converter.gamma == 1.5
        assert converter.ramp == ImageConverter.RAMP_DETAILED
        assert converter.enhance == True
    
    def test_mode_emoji(self):
        """Test emoji mode"""
        converter = ImageConverter()
        converter.set_mode_emoji()
        assert converter._is_emoji_mode == True
        assert converter.aspect_ratio == 0.5
    
    def test_mode_simple(self):
        """Test simple mode"""
        converter = ImageConverter()
        converter.set_mode_simple()
        assert converter.ramp == ImageConverter.RAMP_SIMPLE
        assert converter.enhance == False
    
    def test_generate_frame(self):
        """Test ASCII frame generation"""
        # Create test image
        img = Image.new('RGB', (10, 10), color='white')
        converter = ImageConverter(width=10)
        result = converter.generate_frame(img)
        
        assert isinstance(result, str)
        assert len(result) > 0
        assert '\n' in result  # Should have newlines
    
    def test_pixel_mapping(self):
        """Test pixel to character mapping"""
        converter = ImageConverter()
        
        # Test brightness extremes
        dark_char = converter._map_pixel_to_char(0)
        light_char = converter._map_pixel_to_char(255)
        
        assert dark_char == converter.ramp[0]
        assert light_char == converter.ramp[-1]
    
    def test_save_to_file(self):
        """Test file saving"""
        converter = ImageConverter()
        test_content = "Test ASCII Art\n###\n***"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name
        
        try:
            converter.save_to_file(test_content, temp_path)
            assert os.path.exists(temp_path)
            
            with open(temp_path, 'r') as f:
                content = f.read()
                assert content == test_content
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


class TestCustomTextConverter:
    """Test CustomTextConverter class"""
    
    def test_custom_text(self):
        """Test custom character ramp"""
        custom = "@#*. "
        converter = CustomTextConverter(custom_text=custom)
        assert converter.ramp == custom
    
    def test_empty_text_error(self):
        """Test error on empty custom text"""
        with pytest.raises(ValueError):
            CustomTextConverter(custom_text="")
    
    def test_short_text_error(self):
        """Test error on too short custom text"""
        with pytest.raises(ValueError):
            CustomTextConverter(custom_text="A")
    
    def test_emoji_detection(self):
        """Test emoji auto-detection"""
        emoji_text = "🟦🟩🟨🟧🟥"
        converter = CustomTextConverter(custom_text=emoji_text)
        assert converter._is_emoji_mode == True


class TestBatchConverter:
    """Test BatchConverter class"""
    
    def test_initialization(self):
        """Test batch converter initialization"""
        converter = ImageConverter()
        batch = BatchConverter(converter)
        assert batch.converter == converter


def test_integration():
    """Integration test with real image"""
    # Create a simple test image
    img = Image.new('RGB', (50, 50), color='blue')
    
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        img_path = f.name
        img.save(img_path)
    
    try:
        converter = ImageConverter(width=20)
        result = converter.convert_image(img_path)
        
        assert isinstance(result, str)
        assert len(result) > 0
    finally:
        if os.path.exists(img_path):
            os.remove(img_path)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])