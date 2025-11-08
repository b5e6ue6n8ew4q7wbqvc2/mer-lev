import streamlit as st
import jiwer
import Levenshtein  # Note the capitalization
import pandas as pd

def calculate_levenshtein_ratio(word1, word2):
    """Calculate Levenshtein similarity ratio between two words"""
    max_len = max(len(word1), len(word2))
    if max_len == 0:
        return 1.0
    edit_dist = Levenshtein.distance(word1.lower(), word2.lower())  # Correct import
    return (max_len - edit_dist) / max_len

def analyze_transcription_errors(reference, hypothesis, levenshtein_threshold):
    """Analyze transcription errors and identify potential pronunciation issues"""
    
    # Calculate overall MER
    measures = jiwer.compute_measures(reference, hypothesis)
    mer = measures['wer']  # WER is essentially MER at word level
    
    # Get word-level alignment
    alignment = jiwer.process_words(reference, hypothesis)
    
    # Extract substitutions
    substitutions = []
    for ref_word, hyp_word in zip(alignment.references[0], alignment.hypotheses[0]):
        if ref_word != hyp_word and ref_word != "" and hyp_word != "":
            ratio = calculate_levenshtein_ratio(ref_word, hyp_word)
            # Flag as potential pronunciation issue if ratio is HIGH (similar words)
            is_pronunciation_issue = ratio >= levenshtein_threshold
            substitutions.append({
                'reference': ref_word,
                'hypothesis': hyp_word,
                'levenshtein_ratio': round(ratio, 3),
                'potential_pronunciation_issue': is_pronunciation_issue
            })
    
    return {
        'mer': mer,
        'accuracy': 1 - mer,
        'substitutions': substitutions,
        'total_words': len(alignment.references[0]),
        'correct_words': len([r for r, h in zip(alignment.references[0], alignment.hypotheses[0]) if r == h])
    }

# Streamlit app
st.title("MER-Lev: Transcription Error Analyzer")
st.write("Analyze transcription mistakes using Match Error Rate and Levenshtein distance to identify potential pronunciation issues")

# Input fields
reference_text = st.text_area("Reference Text (Ground Truth)", 
                             height=100,
                             placeholder="Enter the correct reference text here...")

hypothesis_text = st.text_area("Hypothesis Text (Transcription)", 
                              height=100,
                              placeholder="Enter the transcribed text here...")

# Parameters - now defaulting to 0.5 as the minimum similarity threshold
levenshtein_threshold = st.slider("Minimum Levenshtein Similarity Threshold", 
                                 min_value=0.0, max_value=1.0, value=0.5, step=0.05,
                                 help="Words with similarity ratio ABOVE this threshold will be flagged as potential pronunciation issues")

# Analyze button
if st.button("Analyze Transcription Errors") or (reference_text and hypothesis_text):
    if not reference_text.strip() or not hypothesis_text.strip():
        st.warning("Please enter both reference and hypothesis texts.")
    else:
        try:
            results = analyze_transcription_errors(reference_text, hypothesis_text, levenshtein_threshold)
            
            # Display summary metrics
            st.subheader("Summary Metrics")
            col1, col2, col3 = st.columns(3)
            col1.metric("Match Error Rate (MER)", f"{results['mer']:.3f}")
            col2.metric("Accuracy", f"{results['accuracy']:.3f}")
            col3.metric("Correct Words", f"{results['correct_words']}/{results['total_words']}")
            
            # Display substitutions
            if results['substitutions']:
                st.subheader("Word Substitutions Analysis")
                
                # Create DataFrame for better display
                df = pd.DataFrame(results['substitutions'])
                df_display = df.copy()
                df_display['levenshtein_ratio'] = df_display['levenshtein_ratio'].apply(lambda x: f"{x:.3f}")
                df_display.rename(columns={
                    'reference': 'Reference Word',
                    'hypothesis': 'Hypothesis Word', 
                    'levenshtein_ratio': 'Similarity Ratio',
                    'potential_pronunciation_issue': 'Pronunciation Issue?'
                }, inplace=True)
                
                # Style the dataframe to highlight pronunciation issues
                def highlight_pronunciation_issues(row):
                    if row['Pronunciation Issue?']:
                        return ['background-color: #ffcccc'] * len(row)
                    return [''] * len(row)
                
                styled_df = df_display.style.apply(highlight_pronunciation_issues, axis=1)
                st.dataframe(styled_df, use_container_width=True)
                
                # Summary of pronunciation issues
                pronunciation_issues = [sub for sub in results['substitutions'] if sub['potential_pronunciation_issue']]
                if pronunciation_issues:
                    st.subheader("Potential Pronunciation Issues")
                    st.write(f"Found {len(pronunciation_issues)} potential pronunciation issues:")
                    for issue in pronunciation_issues:
                        st.write(f"- '{issue['reference']}' → '{issue['hypothesis']}' (similarity: {issue['levenshtein_ratio']:.3f})")
                else:
                    st.success("No potential pronunciation issues found!")
                    
            else:
                st.info("No substitutions found between the texts.")
                
        except Exception as e:
            st.error(f"Error analyzing texts: {str(e)}")

# Example usage
with st.expander("Example Usage"):
    st.write("**Reference:** I like to play baseball")
    st.write("**Hypothesis:** I like to pray hockey")
    st.write("This will identify two substitutions:")
    st.write("- 'play' → 'pray' (similarity: ~0.75) - Likely pronunciation issue")
    st.write("- 'baseball' → 'hockey' (similarity: 0.0) - Likely semantic/transcription error")
