#!/usr/bin/env python3
"""
Setup configuration for ASCII Forge package
"""

from setuptools import setup, find_packages
import os

# Read long description from README
def read_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

setup(
    name='asciiforge',
    version='1.0.0',
    author='ASCII Forge Team',
    author_email='your.email@example.com',
    description='Professional ASCII art generation toolkit for images and text',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/asciiforge',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Artistic Software',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    keywords='ascii art generator image converter text art animation terminal',
    python_requires='>=3.8',
    install_requires=[
        'Pillow>=10.0.0',
        'pyfiglet>=0.8.0',
        'colorama>=0.4.6',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
            'mypy>=1.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'asciiforge-image=asciiforge.cli_image:main',
            'asciiforge-text=asciiforge.cli_text:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/asciiforge/issues',
        'Source': 'https://github.com/yourusername/asciiforge',
        'Documentation': 'https://github.com/yourusername/asciiforge#readme',
    },
)