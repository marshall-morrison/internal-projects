#!/bin/bash

# PDF Rule Extractor - Run Script
# This script sets up the environment and runs the PDF analysis

echo "Setting up PDF Rule Extractor..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Create directories
mkdir -p pdfs
mkdir -p output
mkdir -p logs

echo "Setup complete!"
echo ""
echo "To run the analysis:"
echo "1. Place your PDF files in the 'pdfs' directory"
echo "2. Set your API keys:"
echo "   export OPENAI_API_KEY='your-openai-key'"
echo "   export ANTHROPIC_API_KEY='your-anthropic-key'"
echo "3. Run: python pdf_rule_extractor.py --pdf-dir pdfs --output-dir output"
echo ""
echo "Or run with API keys directly:"
echo "python pdf_rule_extractor.py --pdf-dir pdfs --output-dir output --openai-key YOUR_KEY --anthropic-key YOUR_KEY"
