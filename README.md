## File 3: `README.md`
```markdown
# MER-Lev: Transcription Error Analyzer

A Streamlit application for analyzing transcription errors using Match Error Rate (MER) and Levenshtein distance to identify potential pronunciation issues.

## Overview

This tool helps identify when transcription errors might be due to pronunciation similarities rather than semantic misunderstandings. It works by:

1. Computing Match Error Rate (MER) using the jiwer library
2. Identifying word-level substitutions  
3. Calculating Levenshtein similarity ratios for each substitution pair
4. Flagging high-similarity substitutions (≥ threshold) as potential pronunciation issues

## Features

- **Word-level error analysis**: Identifies specific word substitutions
- **Levenshtein similarity scoring**: Quantifies how similar mistaken words are
- **Pronunciation issue detection**: Flags similar-sounding word pairs
- **Interactive threshold adjustment**: Customize sensitivity for pronunciation issue detection
- **Visual highlighting**: Clearly shows potential pronunciation issues
- **Performance metrics**: Displays MER, accuracy, and word counts

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd mer-lev-analyzer
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run mer-lev.py
```

### How to Use

1. Enter your **Reference Text** (ground truth/correct transcription)
2. Enter your **Hypothesis Text** (transcribed text to analyze)
3. Adjust the **Levenshtein Similarity Threshold** if needed (default: 0.5)
4. Click "Analyze Transcription Errors"

### Interpreting Results

- **High similarity ratio** (≥ threshold): Potential pronunciation issue
  - Example: "play" vs "pray" (similarity ~0.75)
- **Low similarity ratio** (< threshold): Likely semantic/different word error
  - Example: "baseball" vs "hockey" (similarity 0.0)

## Example

**Reference:** "I like to play baseball"
**Hypothesis:** "I like to pray hockey"

Results:
- "play" → "pray" (similarity: 0.75) - Flagged as pronunciation issue
- "baseball" → "hockey" (similarity: 0.0) - Not flagged

## Requirements

- Python 3.8+
- Streamlit (latest compatible version)
- JiWER (latest compatible version)
- Levenshtein (latest compatible version)
- Pandas (latest compatible version)

See `requirements.txt` for package specifications.

## License

MIT License

Copyright (c) 2024 MER-Lev Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File 5: `LICENSE`
```
MIT License

Copyright (c) 2024 MER-Lev Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
