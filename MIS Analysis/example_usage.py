#!/usr/bin/env python3
"""
Example usage of the PDF Rule Extractor
"""

import os
import json
from pdf_rule_extractor import PDFRuleExtractor

def main():
    # Example configuration
    config = {
        'batch_size': 5,  # Process 5 PDFs at a time
        'max_workers': 3,  # Use 3 parallel workers for LLM calls
        'max_sentences_per_chunk': 8,  # Smaller chunks for better analysis
        'openai_model': 'gpt-4',
        'anthropic_model': 'claude-3-sonnet-20240229',
        'similarity_threshold': 0.6,
        'min_rule_frequency': 2,
        'confidence_threshold': 0.7
    }
    
    # Set API keys (replace with your actual keys)
    config['openai_api_key'] = os.getenv('OPENAI_API_KEY')
    config['anthropic_api_key'] = os.getenv('ANTHROPIC_API_KEY')
    
    if not config['openai_api_key'] and not config['anthropic_api_key']:
        print("Error: Please set either OPENAI_API_KEY or ANTHROPIC_API_KEY environment variable")
        return
    
    # Create extractor
    extractor = PDFRuleExtractor(config)
    
    # Process PDFs
    pdf_directory = "pdfs"  # Directory containing your PDF files
    output_directory = "output"
    
    try:
        print("Starting PDF analysis...")
        extractor.process_pdfs(pdf_directory)
        
        print("Generating reports...")
        extractor.generate_report(output_directory)
        
        print(f"Analysis complete! Check the '{output_directory}' directory for results.")
        
        # Print summary
        print(f"\nSummary:")
        print(f"- Documents processed: {len(set([chunk.document_id for chunk in extractor.chunks]))}")
        print(f"- Chunks analyzed: {len(extractor.chunks)}")
        print(f"- Rules synthesized: {len(extractor.synthesized_rules)}")
        
    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    main()

