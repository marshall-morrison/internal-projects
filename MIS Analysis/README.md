# PDF Rule Extractor

A comprehensive system for analyzing 150+ PDF documents to extract generalizable rules and patterns for merchant instructions.

## Features

- **Batch PDF Processing**: Efficiently processes large numbers of PDFs
- **Intelligent Text Extraction**: Uses multiple PDF extraction methods for robustness
- **Smart Chunking**: Breaks documents into logical sections for analysis
- **LLM Integration**: Uses Anthropic Claude for intelligent analysis
- **Rule Synthesis**: Automatically groups similar rules and identifies patterns
- **Merchant Customization**: Identifies elements that need per-merchant customization
- **Comprehensive Reporting**: Generates JSON, Markdown, and CSV reports

## Quick Start

1. **Setup Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure API Key**:
   ```bash
   cp config.json.template config.json
   # Edit config.json and add your Anthropic API key
   ```

3. **Prepare Your PDFs**:
   - Place all PDF files in your desired directory
   - Ensure PDFs contain readable text (not just images)

4. **Run Analysis**:
   ```bash
   python3 pdf_rule_extractor.py --pdf-dir "/path/to/your/pdfs" --output-dir output --config config.json
   ```

## Configuration

Edit `config.json` to customize:
- Batch processing size
- Chunk size limits
- LLM models
- Similarity thresholds
- Confidence requirements

## Output Files

The analysis generates several output files in the `output/` directory:

- **`analysis_report.json`**: Complete structured data
- **`analysis_report.md`**: Human-readable markdown report
- **`synthesized_rules.csv`**: Rules for spreadsheet analysis
- **`analysis_results.csv`**: Detailed chunk analysis results

## How It Works

1. **PDF Extraction**: Uses multiple libraries (pdfplumber, PyPDF2, pdfminer) for robust text extraction
2. **Preprocessing**: Cleans text, removes artifacts, standardizes formatting
3. **Chunking**: Intelligently splits documents into logical sections
4. **LLM Analysis**: Processes chunks in parallel using Claude
5. **Rule Synthesis**: Groups similar rules and identifies patterns
6. **Report Generation**: Creates comprehensive reports in multiple formats

## Cost Estimation

For 100 documents (~8 pages each):
- **Text Extraction**: ~$0 (local processing)
- **LLM Analysis**: ~$15-25 depending on document complexity
- **Total Processing Time**: 1.5-2.5 hours depending on API rate limits

## Security

- Never commit `config.json` (contains API keys)
- Use `config.json.template` as a starting point
- The `.gitignore` file protects sensitive information

## Support

For issues or questions:
1. Check the logs in `pdf_analysis.log`
2. Review the configuration in `config.json`
3. Ensure all dependencies are installed correctly
4. Verify API keys are valid and have sufficient credits