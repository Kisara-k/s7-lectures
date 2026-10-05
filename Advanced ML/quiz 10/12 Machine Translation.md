## 12. Machine Translation

## Questions

#### 1. Which of the following are challenges specific to machine translation between English and morphologically rich languages like Sinhala or Tamil?  
A) Word order differences such as SVO vs SOV  
B) Morphological richness causing one English word to map to many inflected forms  
C) The presence of lexical gaps and ambiguity in vocabulary  
D) The inability to use parallel corpora for training  

#### 2. In Rule-Based Machine Translation (RBMT), which components are typically involved in the pipeline?  
A) Morphological analysis and POS tagging  
B) Bilingual dictionary and structural transfer rules  
C) Neural network encoder-decoder architecture  
D) Target syntax realization and morphological inflection  

#### 3. What are the main limitations of phrase-based Statistical Machine Translation (SMT)?  
A) It only allows local reordering and penalizes long-distance reordering  
B) It generalizes well across morphological variants of words  
C) It relies on independently trained components leading to error accumulation  
D) It uses continuous vector representations for end-to-end training  

#### 4. Why does the plain encoder-decoder architecture in Neural Machine Translation suffer from degraded performance on long sentences?  
A) Because it uses a fixed-length context vector that acts as a bottleneck  
B) Because it cannot generate embeddings for rare words  
C) Because it cannot attend back to earlier encoder states once decoding starts  
D) Because it relies on phrase tables that grow exponentially with sentence length  

#### 5. How does the Transformer architecture improve over recurrent models in machine translation?  
A) By removing recurrence and allowing every position to attend directly to every other position  
B) By using multi-head attention to capture multiple types of relationships simultaneously  
C) By encoding word order through positional encodings added to input embeddings  
D) By relying solely on phrase-based translation probabilities  

#### 6. Which of the following statements about Byte-Pair Encoding (BPE) tokenization are true?  
A) It starts with a character vocabulary and merges frequent adjacent symbol pairs  
B) It results in a fixed vocabulary that excludes rare words  
C) Frequent words tend to remain as single tokens, while rare words are split into subwords  
D) It completely eliminates the out-of-vocabulary problem  

#### 7. In beam search decoding for Neural Machine Translation, why is length normalization applied to scores?  
A) To prevent longer hypotheses from being unfairly penalized due to accumulated negative log-probabilities  
B) To ensure that the highest probability token is always selected at each step  
C) To make the search space exponential in size  
D) To guarantee that larger beams always improve BLEU scores  

#### 8. What are the advantages of multilingual pre-trained models like mBART and mT5 for machine translation?  
A) They allow low-resource languages to benefit from data in related high-resource languages  
B) They require training from scratch for each language pair to achieve good performance  
C) They use a shared vocabulary and language tokens to mark the target language  
D) They completely avoid the curse of multilinguality regardless of the number of languages  

#### 9. Why is direct many-to-many translation preferred over pivoting through English in massively multilingual models?  
A) Pivoting compounds errors and discards language-specific information absent in English  
B) Pivoting reduces the number of translation steps, improving accuracy  
C) Direct translation keeps the process to a single step, preserving more information  
D) Pivoting is necessary because many languages lack parallel data with each other  

#### 10. Which of the following are known weaknesses or failure modes of large language models (LLMs) when used for machine translation?  
A) Hallucination, where fluent output diverges from the source meaning  
B) Off-target translation producing output in the wrong language  
C) Superior performance on low-resource languages compared to dedicated NMT systems  
D) Higher cost, latency, and reproducibility challenges compared to smaller specialized models



<br>

## Answers

#### 1. Which of the following are challenges specific to machine translation between English and morphologically rich languages like Sinhala or Tamil?  
A) ✓ Word order differences such as SVO vs SOV require reordering of constituents.  
B) ✓ Morphological richness means one English word may correspond to many inflected forms in the target language.  
C) ✓ Lexical gaps and ambiguity are common, e.g., words with multiple meanings or no direct equivalent.  
D) ✗ Parallel corpora can be used; the challenge is not their absence but linguistic complexity.  

**Correct:** A, B, C


#### 2. In Rule-Based Machine Translation (RBMT), which components are typically involved in the pipeline?  
A) ✓ Morphological analysis and POS tagging are part of the analysis stage.  
B) ✓ Bilingual dictionary and structural transfer rules are used in the transfer stage.  
C) ✗ Neural encoder-decoder architectures are not part of classical RBMT.  
D) ✓ Target syntax realization and morphological inflection are part of generation.  

**Correct:** A, B, D


#### 3. What are the main limitations of phrase-based Statistical Machine Translation (SMT)?  
A) ✓ Local reordering only; long-distance reordering is penalized, problematic for SOV-SVO pairs.  
B) ✗ It does not generalize well across morphological variants; treats forms like walk, walks, walked as unrelated.  
C) ✓ Independently trained components cause error accumulation and lack end-to-end optimization.  
D) ✗ Continuous vector representations and end-to-end training are features of neural MT, not phrase-based SMT.  

**Correct:** A, C


#### 4. Why does the plain encoder-decoder architecture in Neural Machine Translation suffer from degraded performance on long sentences?  
A) ✓ The fixed-length context vector acts as a bottleneck limiting capacity.  
B) ✗ Embeddings for rare words are handled by subword tokenization, not the bottleneck issue.  
C) ✓ The model cannot revisit encoder states once decoding starts, losing early information.  
D) ✗ Phrase tables are not used in encoder-decoder NMT; this is an SMT issue.  

**Correct:** A, C


#### 5. How does the Transformer architecture improve over recurrent models in machine translation?  
A) ✓ Removes recurrence, allowing direct attention between all positions, enabling parallel computation.  
B) ✓ Multi-head attention captures multiple relationship types simultaneously.  
C) ✓ Positional encodings inject order information since self-attention is permutation-invariant.  
D) ✗ Transformers do not rely on phrase-based translation probabilities.  

**Correct:** A, B, C


#### 6. Which of the following statements about Byte-Pair Encoding (BPE) tokenization are true?  
A) ✓ BPE starts with characters and merges frequent adjacent pairs iteratively.  
B) ✗ BPE creates an open vocabulary that includes rare words as subword units, not excluding them.  
C) ✓ Frequent words remain single tokens; rare words are split into meaningful subwords.  
D) ✓ BPE effectively eliminates out-of-vocabulary words by decomposing unknown words into subwords.  

**Correct:** A, C, D


#### 7. In beam search decoding for Neural Machine Translation, why is length normalization applied to scores?  
A) ✓ Without normalization, longer hypotheses accumulate more negative log-probabilities and are unfairly penalized.  
B) ✗ Greedy decoding selects highest probability tokens; beam search keeps multiple hypotheses.  
C) ✗ Length normalization does not increase search space size; it adjusts scoring.  
D) ✗ Larger beams often degrade BLEU scores due to search anomalies, so bigger beams do not guarantee improvement.  

**Correct:** A


#### 8. What are the advantages of multilingual pre-trained models like mBART and mT5 for machine translation?  
A) ✓ Low-resource languages benefit from shared representations with related high-resource languages.  
B) ✗ They do not require training from scratch for each language pair; fine-tuning suffices.  
C) ✓ Use of shared vocabulary and language tokens enables multilingual support.  
D) ✗ Adding many languages eventually reduces accuracy per language due to fixed model capacity (curse of multilinguality).  

**Correct:** A, C


#### 9. Why is direct many-to-many translation preferred over pivoting through English in massively multilingual models?  
A) ✓ Pivoting compounds errors and loses language-specific information absent in English.  
B) ✗ Pivoting adds steps and error accumulation; it does not reduce steps.  
C) ✓ Direct translation keeps the process to one step, preserving more information.  
D) ✗ Pivoting is used because many language pairs lack direct parallel data, but direct models aim to avoid this.  

**Correct:** A, C


#### 10. Which of the following are known weaknesses or failure modes of large language models (LLMs) when used for machine translation?  
A) ✓ Hallucination causes fluent but inaccurate output diverging from the source.  
B) ✓ Off-target translation produces output in the wrong language, common in zero-shot and multilingual settings.  
C) ✗ LLMs generally perform worse on low-resource languages compared to dedicated NMT trained on parallel data.  
D) ✓ LLMs have higher cost, latency, and reproducibility challenges than smaller specialized models.  

**Correct:** A, B, D