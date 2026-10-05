## 8. Sequence to Sequence Learning

## Questions

#### 1. What are the key characteristics of sequence data that make sequence-to-sequence learning necessary?  
A) Data points are arranged in a meaningful order  
B) Data points are independent and identically distributed  
C) Temporal dependencies exist between elements  
D) Input and output sequences always have the same length  

#### 2. Which of the following are valid applications of sequence-to-sequence learning?  
A) Image Captioning  
B) Sentiment Classification  
C) Time-Series Forecasting  
D) Frame-level Video Action Recognition  

#### 3. In the context of sequence-to-sequence problems, which of the following correctly describe many-to-many (Type II) sequence modeling?  
A) Input and output sequences have variable lengths  
B) The input is a sequence of video frames and the output is a caption  
C) The input is a single image and the output is a sequence of words  
D) The input and output sequences are of fixed length and same modality  

#### 4. Why does a Multi-Layer Perceptron (MLP) perform poorly on the reverse sequence problem?  
A) It cannot process variable-length sequences  
B) It processes each time step independently without modeling temporal dependencies  
C) It uses shared weights across time steps  
D) It lacks the ability to capture the order of sequence elements  

#### 5. Which of the following statements about Recurrent Neural Networks (RNNs) are true?  
A) RNNs maintain a hidden state that propagates information across time steps  
B) RNNs share parameters across all time steps  
C) RNNs cannot process sequences of variable length  
D) RNNs always retain long-term dependencies perfectly  

#### 6. What are the main gating mechanisms in an LSTM cell and their functions?  
A) Forget Gate: decides what information to discard from the previous cell state  
B) Input Gate: controls what new information to add to the cell state  
C) Reset Gate: controls how much past information to use in the new state  
D) Output Gate: determines how much of the cell state to expose as hidden state  

#### 7. How do GRU cells differ from LSTM cells in terms of gating mechanisms?  
A) GRUs have a reset gate and an update gate  
B) GRUs have separate forget and input gates like LSTMs  
C) GRUs combine the forget and input gates into a single update gate  
D) GRUs maintain a separate cell state distinct from the hidden state  

#### 8. Which of the following are possible ways recurrent layers can share information between layers?  
A) Passing only the last hidden state  
B) Passing all hidden states  
C) Passing the last hidden state and last cell state  
D) Passing only the input sequence  

#### 9. What are the main advantages of the Encoder-Decoder architecture in sequence-to-sequence tasks?  
A) It allows input and output sequences to have different lengths  
B) It requires input and output sequences to be of the same modality  
C) It separates sequence encoding from sequence generation  
D) It transfers information through a context representation  

#### 10. Which of the following statements about sequence data encoding techniques are correct?  
A) One-Hot Encoding transforms categorical sequence data into numerical vectors  
B) Bag-of-Words preserves the order of words in a sequence  
C) Word2Vec and BERT provide contextual embeddings for text sequences  
D) Wav2Vec is used for encoding audio sequences into numerical representations



<br>

## Answers

#### 1. What are the key characteristics of sequence data that make sequence-to-sequence learning necessary?  
A) ✓ Data points are arranged in a meaningful order, which is essential for sequence modeling.  
B) ✗ Data points are not independent; temporal dependencies exist, so this is false.  
C) ✓ Temporal dependencies exist between elements, requiring models that capture order.  
D) ✗ Input and output sequences do not always have the same length in Seq2Seq tasks.  

**Correct:** A, C


#### 2. Which of the following are valid applications of sequence-to-sequence learning?  
A) ✓ Image Captioning is a classic Seq2Seq task converting images to text sequences.  
B) ✗ Sentiment Classification is many-to-one, not sequence-to-sequence.  
C) ✓ Time-Series Forecasting predicts future sequences from past sequences.  
D) ✗ Frame-level Video Action Recognition is many-to-many (Type I), classification, not Seq2Seq generation.  

**Correct:** A, C


#### 3. In the context of sequence-to-sequence problems, which of the following correctly describe many-to-many (Type II) sequence modeling?  
A) ✓ Many-to-many (Type II) often involves variable-length input and output sequences.  
B) ✓ Video Captioning (sequence of frames → caption) is many-to-many (Type II).  
C) ✗ Image Captioning is one-to-many, not many-to-many (Type II).  
D) ✗ Fixed length and same modality is not typical for many-to-many (Type II).  

**Correct:** A, B


#### 4. Why does a Multi-Layer Perceptron (MLP) perform poorly on the reverse sequence problem?  
A) ✗ MLPs can process fixed-length inputs but fail to model temporal order.  
B) ✓ MLP processes each time step independently, ignoring temporal dependencies.  
C) ✗ MLPs do not share weights across time steps; RNNs do.  
D) ✓ MLP cannot capture the order of sequence elements, which is critical here.  

**Correct:** B, D


#### 5. Which of the following statements about Recurrent Neural Networks (RNNs) are true?  
A) ✓ RNNs maintain a hidden state that carries information across time steps.  
B) ✓ RNNs share the same parameters (weights) across all time steps.  
C) ✗ RNNs can process variable-length sequences by design.  
D) ✗ RNNs struggle to retain long-term dependencies due to vanishing gradients.  

**Correct:** A, B


#### 6. What are the main gating mechanisms in an LSTM cell and their functions?  
A) ✓ Forget Gate decides what to discard from previous cell state.  
B) ✓ Input Gate controls what new information to add to the cell state.  
C) ✗ Reset Gate is part of GRU, not LSTM.  
D) ✓ Output Gate controls how much cell state info is exposed as hidden state.  

**Correct:** A, B, D


#### 7. How do GRU cells differ from LSTM cells in terms of gating mechanisms?  
A) ✓ GRUs have reset and update gates.  
B) ✗ GRUs do not have separate forget and input gates like LSTMs.  
C) ✓ GRUs combine forget and input gates into a single update gate.  
D) ✗ GRUs do not maintain a separate cell state; hidden state and cell state are merged.  

**Correct:** A, C


#### 8. Which of the following are possible ways recurrent layers can share information between layers?  
A) ✓ Passing only the last hidden state is a common method.  
B) ✓ Passing all hidden states is another valid method.  
C) ✓ Passing last hidden state and last cell state is used especially with LSTM.  
D) ✗ Passing only the input sequence is not a form of recurrent layer information sharing.  

**Correct:** A, B, C


#### 9. What are the main advantages of the Encoder-Decoder architecture in sequence-to-sequence tasks?  
A) ✓ It allows input and output sequences to have different lengths.  
B) ✗ It does not require input and output sequences to be of the same modality.  
C) ✓ It separates sequence encoding from sequence generation, improving flexibility.  
D) ✓ It transfers information through a context representation between encoder and decoder.  

**Correct:** A, C, D


#### 10. Which of the following statements about sequence data encoding techniques are correct?  
A) ✓ One-Hot Encoding converts categorical data into numerical vectors.  
B) ✗ Bag-of-Words does not preserve word order; it only counts word occurrences.  
C) ✓ Word2Vec and BERT provide contextual embeddings capturing semantic meaning.  
D) ✓ Wav2Vec is designed for encoding audio sequences into numerical representations.  

**Correct:** A, C, D