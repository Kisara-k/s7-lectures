## 8. Sequence to Sequence Learning

## Key Points

#### 1. 🔄 Sequence-to-Sequence Learning  
- Seq2Seq learning maps an input sequence to an output sequence.  
- Input and output sequences can have different lengths and modalities.  
- Common applications include machine translation, image captioning, video captioning, text summarization, question answering, speech recognition, and time-series forecasting.

#### 2. 📊 Types of Sequence-to-Sequence Problems  
- Many-to-One: Sequence input maps to a single output (e.g., sentiment classification).  
- One-to-Many: Single input maps to a sequence output (e.g., image captioning).  
- Many-to-Many (Type I): Sequence input maps to sequence output with aligned lengths (e.g., video action recognition).  
- Many-to-Many (Type II): Sequence input maps to sequence output with different lengths (e.g., video captioning).

#### 3. 🧮 Sequence Data Encoding  
- Neural networks require numerical representations of sequence data.  
- Common encoding methods: One-Hot Encoding, Bag-of-Words (BoW), Word2Vec, BERT, Wav2Vec.

#### 4. ❌ Limitations of Multi-Layer Perceptron (MLP) for Seq2Seq  
- MLP processes each time step independently, ignoring temporal dependencies.  
- MLP performs poorly on sequence reversal tasks (~10% accuracy).

#### 5. 🔁 Recurrent Neural Networks (RNNs)  
- RNNs maintain a hidden state that propagates information across time steps.  
- RNNs share the same parameters across all time steps.  
- Simple RNNs improve over MLPs by modeling temporal dependencies but struggle with long-term dependencies (~55% accuracy on sequence reversal).

#### 6. 🔑 Advanced Recurrent Cells: LSTM and GRU  
- LSTM uses forget, input, and output gates to control information flow and retain long-term dependencies.  
- GRU uses reset and update gates to manage memory with a simpler structure than LSTM.  
- Both LSTM and GRU improve memory retention compared to simple RNNs.

#### 7. 🏗️ Information Sharing in Stacked Recurrent Networks  
- Recurrent layers can share information via:  
  - Last hidden state  
  - All hidden states  
  - Last hidden state and last cell state  
  - All hidden states and last cell state

#### 8. 🏗️ Encoder-Decoder Architecture  
- Encoder converts input sequence into a context representation.  
- Decoder generates output sequence from the context representation.  
- Enables handling of input and output sequences with different lengths and modalities.



<br>

