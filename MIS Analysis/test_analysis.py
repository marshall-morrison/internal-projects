#!/usr/bin/env python3
"""
Quick test script to analyze just 2 documents and show the expected output format
"""

import os
import json
from pdf_rule_extractor import PDFRuleExtractor

def main():
    # Load configuration
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    # Create extractor
    extractor = PDFRuleExtractor(config)
    
    # Test with just 2 documents
    pdf_directory = "/Users/marshallmorrison/Documents/Active MIS"
    output_directory = "test_output"
    
    # Get first 2 PDF files
    from pathlib import Path
    pdf_path = Path(pdf_directory)
    pdf_files = list(pdf_path.glob("*.pdf"))[:2]  # Just first 2 files
    
    print(f"Testing with {len(pdf_files)} documents:")
    for pdf_file in pdf_files:
        print(f"  - {pdf_file.name}")
    
    try:
        print("\nStarting analysis...")
        
        # Process just these 2 files
        for pdf_file in pdf_files:
            extractor.process_single_pdf(pdf_file)
        
        print("Generating reports...")
        extractor.generate_report(output_directory)
        
        print(f"\n✅ Analysis complete! Check the '{output_directory}' directory for results.")
        
        # Print summary
        print(f"\n📊 Summary:")
        print(f"- Documents processed: {len(set([chunk.document_id for chunk in extractor.chunks]))}")
        print(f"- Chunks analyzed: {len(extractor.chunks)}")
        print(f"- Analysis results: {len(extractor.analysis_results)}")
        print(f"- Rules synthesized: {len(extractor.synthesized_rules)}")
        
        # Show sample output
        if extractor.analysis_results:
            print(f"\n📋 Sample Analysis Result:")
            result = extractor.analysis_results[0]
            print(f"Document: {result.document_id}")
            print(f"Themes: {result.themes}")
            print(f"Rules: {result.rules}")
            print(f"Confidence: {result.confidence_score}")
        
    except Exception as e:
        print(f"❌ Error during analysis: {e}")

if __name__ == "__main__":
    main()
