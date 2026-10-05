## 8. Sequence to Sequence Learning

## Questions

#### 1. What are the key characteristics of sequence data that make sequence-to-sequence learning necessary?  
A) Temporal dependencies exist between elements  
B) Input and output sequences always have the same length  
C) Data points are arranged in a meaningful order  
D) Data points are independent and identically distributed  

#### 2. Which of the following are valid applications of sequence-to-sequence learning?  
A) Image Captioning  
B) Time-Series Forecasting  
C) Sentiment Classification  
D) Frame-level Video Action Recognition  

#### 3. In the context of sequence-to-sequence problems, which of the following correctly describe many-to-many (Type II) sequence modeling?  
A) The input is a sequence of video frames and the output is a caption  
B) The input and output sequences are of fixed length and same modality  
C) Input and output sequences have variable lengths  
D) The input is a single image and the output is a sequence of words  

#### 4. Why does a Multi-Layer Perceptron (MLP) perform poorly on the reverse sequence problem?  
A) It processes each time step independently without modeling temporal dependencies  
B) It lacks the ability to capture the order of sequence elements  
C) It uses shared weights across time steps  
D) It cannot process variable-length sequences  

#### 5. Which of the following statements about Recurrent Neural Networks (RNNs) are true?  
A) RNNs always retain long-term dependencies perfectly  
B) RNNs maintain a hidden state that propagates information across time steps  
C) RNNs cannot process sequences of variable length  
D) RNNs share parameters across all time steps  

#### 6. What are the main gating mechanisms in an LSTM cell and their functions?  
A) Forget Gate: decides what information to discard from the previous cell state  
B) Output Gate: determines how much of the cell state to expose as hidden state  
C) Input Gate: controls what new information to add to the cell state  
D) Reset Gate: controls how much past information to use in the new state  

#### 7. How do GRU cells differ from LSTM cells in terms of gating mechanisms?  
A) GRUs combine the forget and input gates into a single update gate  
B) GRUs have separate forget and input gates like LSTMs  
C) GRUs maintain a separate cell state distinct from the hidden state  
D) GRUs have a reset gate and an update gate  

#### 8. Which of the following are possible ways recurrent layers can share information between layers?  
A) Passing all hidden states  
B) Passing only the last hidden state  
C) Passing the last hidden state and last cell state  
D) Passing only the input sequence  

#### 9. What are the main advantages of the Encoder-Decoder architecture in sequence-to-sequence tasks?  
A) It requires input and output sequences to be of the same modality  
B) It transfers information through a context representation  
C) It separates sequence encoding from sequence generation  
D) It allows input and output sequences to have different lengths  

#### 10. Which of the following statements about sequence data encoding techniques are correct?  
A) One-Hot Encoding transforms categorical sequence data into numerical vectors  
B) Wav2Vec is used for encoding audio sequences into numerical representations  
C) Bag-of-Words preserves the order of words in a sequence  
D) Word2Vec and BERT provide contextual embeddings for text sequences  



<br>

## Answers

#### 1. What are the key characteristics of sequence data that make sequence-to-sequence learning necessary?  
A) ✓ Temporal dependencies exist between elements, requiring models that capture order.  
B) ✗ Input and output sequences do not always have the same length in Seq2Seq tasks.  
C) ✓ Data points are arranged in a meaningful order, which is essential for sequence modeling.  
D) ✗ Data points are not independent; temporal dependencies exist, so this is false.  

**Correct:** A, C


#### 2. Which of the following are valid applications of sequence-to-sequence learning?  
A) ✓ Image Captioning is a classic Seq2Seq task converting images to text sequences.  
B) ✓ Time-Series Forecasting predicts future sequences from past sequences.  
C) ✗ Sentiment Classification is many-to-one, not sequence-to-sequence.  
D) ✗ Frame-level Video Action Recognition is many-to-many (Type I), classification, not Seq2Seq generation.  

**Correct:** A, B


#### 3. In the context of sequence-to-sequence problems, which of the following correctly describe many-to-many (Type II) sequence modeling?  
A) ✓ Video Captioning (sequence of frames → caption) is many-to-many (Type II).  
B) ✗ Fixed length and same modality is not typical for many-to-many (Type II).  
C) ✓ Many-to-many (Type II) often involves variable-length input and output sequences.  
D) ✗ Image Captioning is one-to-many, not many-to-many (Type II).  

**Correct:** A, C


#### 4. Why does a Multi-Layer Perceptron (MLP) perform poorly on the reverse sequence problem?  
A) ✓ MLP processes each time step independently, ignoring temporal dependencies.  
B) ✓ MLP cannot capture the order of sequence elements, which is critical here.  
C) ✗ MLPs do not share weights across time steps; RNNs do.  
D) ✗ MLPs can process fixed-length inputs but fail to model temporal order.  

**Correct:** A, B


#### 5. Which of the following statements about Recurrent Neural Networks (RNNs) are true?  
A) ✗ RNNs struggle to retain long-term dependencies due to vanishing gradients.  
B) ✓ RNNs maintain a hidden state that carries information across time steps.  
C) ✗ RNNs can process variable-length sequences by design.  
D) ✓ RNNs share the same parameters (weights) across all time steps.  

**Correct:** B, D


#### 6. What are the main gating mechanisms in an LSTM cell and their functions?  
A) ✓ Forget Gate decides what to discard from previous cell state.  
B) ✓ Output Gate controls how much cell state info is exposed as hidden state.  
C) ✓ Input Gate controls what new information to add to the cell state.  
D) ✗ Reset Gate is part of GRU, not LSTM.  

**Correct:** A, B, C


#### 7. How do GRU cells differ from LSTM cells in terms of gating mechanisms?  
A) ✓ GRUs combine forget and input gates into a single update gate.  
B) ✗ GRUs do not have separate forget and input gates like LSTMs.  
C) ✗ GRUs do not maintain a separate cell state; hidden state and cell state are merged.  
D) ✓ GRUs have reset and update gates.  

**Correct:** A, D


#### 8. Which of the following are possible ways recurrent layers can share information between layers?  
A) ✓ Passing all hidden states is another valid method.  
B) ✓ Passing only the last hidden state is a common method.  
C) ✓ Passing last hidden state and last cell state is used especially with LSTM.  
D) ✗ Passing only the input sequence is not a form of recurrent layer information sharing.  

**Correct:** A, B, C


#### 9. What are the main advantages of the Encoder-Decoder architecture in sequence-to-sequence tasks?  
A) ✗ It does not require input and output sequences to be of the same modality.  
B) ✓ It transfers information through a context representation between encoder and decoder.  
C) ✓ It separates sequence encoding from sequence generation, improving flexibility.  
D) ✓ It allows input and output sequences to have different lengths.  

**Correct:** B, C, D


#### 10. Which of the following statements about sequence data encoding techniques are correct?  
A) ✓ One-Hot Encoding converts categorical data into numerical vectors.  
B) ✓ Wav2Vec is designed for encoding audio sequences into numerical representations.  
C) ✗ Bag-of-Words does not preserve word order; it only counts word occurrences.  
D) ✓ Word2Vec and BERT provide contextual embeddings capturing semantic meaning.  

**Correct:** A, B, D