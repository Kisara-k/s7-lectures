## 12. Machine Translation

## Key Points

#### 1. 🌍 Machine Translation Basics  
- Machine Translation (MT) automatically converts text from a source language to a target language while preserving meaning.  
- Translation is not word-by-word due to structural, morphological, and lexical differences between languages.

#### 2. 🤔 Challenges in Translation  
- English uses SVO word order; Sinhala, Tamil, and Japanese use SOV, requiring reordering in translation.  
- Morphologically rich languages encode grammatical information in word forms that may not have direct English equivalents.  
- Lexical ambiguity (e.g., "bank" as river or financial institution) complicates translation.  
- Pro-drop languages omit subjects, requiring context to infer missing information.

#### 3. ⚙️ Rule-Based Machine Translation (RBMT)  
- RBMT uses hand-written rules and resources: morphological analysis, POS tagging, parsing, bilingual dictionaries, and transfer rules.  
- RBMT is limited by the difficulty of covering all language complexities with rules.

#### 4. 📊 Statistical Machine Translation (SMT)  
- SMT finds the target sentence maximizing conditional probability using Bayes’ theorem and the noisy channel model.  
- Phrase-based SMT estimates phrase translation probabilities and uses a distortion model to penalize phrase reordering.  
- Language models (n-gram) estimate fluency; smoothing techniques like Kneser-Ney prevent zero probabilities.  
- Decoding uses search with pruning (stack grouping, histogram, threshold) to manage exponential search space.  
- SMT limitations include poor handling of long-range reordering, no generalization across word forms, sparse data issues, and pipeline error accumulation.

#### 5. 🤖 Neural Machine Translation (NMT)  
- NMT uses an encoder-decoder architecture with recurrent neural networks trained end-to-end.  
- Encoder compresses source sentence into a fixed-length context vector; decoder generates target sentence conditioned on this vector.  
- Word embeddings allow generalization across related words.  
- Fixed-length context vector causes performance degradation on long sentences (bottleneck problem).  
- Attention mechanism allows decoder to focus on all encoder states, improving translation quality.

#### 6. ⚡ Transformer Architecture  
- Transformers remove recurrence, enabling parallel computation and direct attention between all words.  
- Self-attention computes relationships within the same sequence; cross-attention connects decoder to encoder outputs.  
- Masked self-attention prevents decoder from seeing future tokens during generation.  
- Multi-head attention runs multiple attention mechanisms in parallel to capture diverse relationships.  
- Positional encoding adds order information to embeddings.  
- Transformers are the basis of modern MT and large language models.

#### 7. 🧩 Tokenization and Decoding  
- Byte-Pair Encoding (BPE) builds subword vocabularies by merging frequent character pairs, handling rare words and morphology.  
- Greedy decoding selects the highest-probability token at each step but can get stuck in errors.  
- Beam search keeps multiple hypotheses, scoring them with length-normalized log-probabilities; typical beam sizes are 4-10.

#### 8. 🌐 Multilingual and Pre-trained Models  
- mBART and mT5 are multilingual pre-trained models trained on many languages with shared vocabularies and language tokens.  
- Multilingual pre-training helps low-resource languages by sharing representations with related high-resource languages.  
- Curse of multilinguality: adding languages reduces per-language accuracy due to fixed model capacity.  
- M2M-100 and NLLB-200 are massively multilingual models translating directly between many languages without pivoting through English.  
- Direct translation avoids compounded errors and information loss from pivoting.

#### 9. 🧠 Large Language Models (LLMs) in Translation  
- Zero-shot translation uses instructions only; few-shot adds example translations in the prompt.  
- LLMs provide document-level context, controllability (style, dialect), and related tasks (post-editing, quality estimation).  
- LLMs require no parallel data but struggle with low-resource languages, off-target translation, hallucination, and higher cost/latency.

#### 10. ✅ Translation Evaluation  
- Good translation preserves adequacy (meaning) and fluency (naturalness).  
- Human evaluation is gold standard but costly and variable.  
- BLEU measures n-gram overlap with clipping to prevent inflated scores but penalizes synonyms and reordering.  
- BLEU correlates poorly with human judgment at sentence level and is unreliable for morphologically rich languages.  
- chrF uses character n-grams, better for morphologically rich languages.  
- Neural metrics (COMET, BLEURT) score translations with trained models, correlating better with humans but may be unreliable for low-resource languages.



<br>

