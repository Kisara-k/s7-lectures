## 13. Self Supervised Learning

## Questions

#### 1. Which of the following statements correctly describe self-supervised learning (SSL)?  
A) SSL uses labeled data provided by human annotators to train models.  
B) SSL requires explicit external supervision signals to guide training.  
C) SSL combines aspects of supervised and unsupervised learning by using a prediction task with a standard loss on unlabeled data.  
D) SSL creates labels automatically from the data itself without manual annotation.  

#### 2. In the context of early self-supervised learning pretext tasks for images, which challenges or limitations were identified?  
A) Context prediction tasks always required pixel-perfect reconstruction to be effective.  
B) Hand-designed tasks often forced networks to learn deep semantic features without shortcuts.  
C) Tasks such as rotation prediction significantly closed the gap to supervised pre-training despite their simplicity.  
D) Networks could solve tasks by exploiting low-level cues like chromatic aberration rather than semantic understanding.  

#### 3. Contrastive learning in vision SSL involves which of the following principles?  
A) Pushing embeddings of different images apart in the feature space.  
B) Predicting masked patches of an image directly from visible patches.  
C) Pulling embeddings of two augmented views of the same image closer together.  
D) Using a memory bank to store negative samples for instance discrimination.  

#### 4. Regarding Masked Image Modelling methods like BEiT and MAE, which statements are true?  
A) MAE masks a smaller percentage of patches than BEiT to simplify the task.  
B) BEiT predicts discrete visual tokens from a pre-trained tokenizer for masked patches.  
C) MAE uses an asymmetric design with a large encoder for visible patches and a lightweight decoder for reconstruction.  
D) Both BEiT and MAE rely on pixel-wise reconstruction of masked patches.  

#### 5. Which evaluation methods are commonly used to assess the quality of representations learned via self-supervised learning?  
A) Fine-tuning the entire pre-trained model on a labeled downstream task.  
B) Linear probing, where the encoder is frozen and only a linear classifier is trained.  
C) Using k-nearest neighbors in feature space without additional training.  
D) Measuring the accuracy of the pretext task during SSL training.  

#### 6. Why is text particularly well-suited for self-supervised learning approaches?  
A) Text data is always labeled with semantic tags, making supervision easy.  
B) Large volumes of unlabeled text are readily available, unlike labeled datasets.  
C) The distributional hypothesis supports learning word meanings from context.  
D) The discrete token nature of text allows masking any word and using the original as a free label.  

#### 7. Which of the following correctly describe differences between static and contextual word embeddings?  
A) Contextual embeddings generate different vectors for the same word depending on its sentence context.  
B) ELMo uses bidirectional LSTMs to produce contextualized word representations.  
C) Static embeddings assign a single fixed vector to each word regardless of context.  
D) Word2Vec and GloVe produce contextual embeddings.  

#### 8. In Masked Language Modelling (MLM) as used in BERT, which of the following are true?  
A) Next sentence prediction is a secondary task used to improve sentence-level understanding.  
B) The model predicts the original token using context from both left and right sides.  
C) Of the selected tokens, 80% are replaced with [MASK], 10% with random tokens, and 10% remain unchanged.  
D) 15% of tokens are selected for prediction, and all are replaced with a [MASK] token during training.  

#### 9. How do autoregressive language models like GPT differ from masked language models like BERT?  
A) GPT predicts the next token using only tokens to the left, making it unidirectional.  
B) BERT predicts masked tokens using context from both directions.  
C) GPT uses a bidirectional Transformer encoder to read the entire sentence.  
D) GPT is naturally suited for text generation, while BERT is better for classification and tagging.  

#### 10. Which statements about advanced SSL text models such as RoBERTa, XLNet, and ELECTRA are correct?  
A) XLNet uses permutation language modeling to incorporate bidirectional context while maintaining autoregressive training.  
B) RoBERTa removes next sentence prediction and uses dynamic masking with larger batches and more data.  
C) All three models rely exclusively on the original BERT training objective without modifications.  
D) ELECTRA trains a generator to replace tokens and a discriminator to detect replaced tokens, considering all tokens in the sequence.  



<br>

## Answers

#### 1. Which of the following statements correctly describe self-supervised learning (SSL)?  
A) ✗ SSL does not use human-provided labels; it uses labels generated from the data itself.  
B) ✗ SSL does not require external supervision signals; supervision comes from the data itself.  
C) ✓ SSL combines unlabeled data (like unsupervised) with a supervised-style prediction task.  
D) ✓ SSL automatically creates labels from the data, requiring no manual annotation.  

**Correct:** C, D


#### 2. In the context of early self-supervised learning pretext tasks for images, which challenges or limitations were identified?  
A) ✗ Pixel-perfect reconstruction was not always necessary; some tasks focused on relative position or context.  
B) ✗ Hand-designed tasks often allowed shortcuts, so they did not always force semantic learning.  
C) ✓ Rotation prediction, despite simplicity, significantly improved performance toward supervised levels.  
D) ✓ Networks exploited low-level cues like chromatic aberration instead of learning semantics.  

**Correct:** C, D


#### 3. Contrastive learning in vision SSL involves which of the following principles?  
A) ✓ Pushing embeddings of different images apart is essential to contrastive learning.  
B) ✗ Predicting masked patches is a masked modelling approach, not contrastive learning.  
C) ✓ Pulling embeddings of two augmented views of the same image closer is fundamental.  
D) ✓ Instance discrimination uses a memory bank to store negative samples.  

**Correct:** A, C, D


#### 4. Regarding Masked Image Modelling methods like BEiT and MAE, which statements are true?  
A) ✗ MAE masks a larger percentage (~75%) of patches, not smaller, to encourage semantic learning.  
B) ✓ BEiT predicts discrete visual tokens from a pre-trained tokenizer for masked patches.  
C) ✓ MAE uses an asymmetric design with a large encoder for visible patches and a lightweight decoder.  
D) ✗ BEiT predicts discrete tokens, while MAE reconstructs raw pixels; both do not rely solely on pixel-wise reconstruction.  

**Correct:** B, C


#### 5. Which evaluation methods are commonly used to assess the quality of representations learned via self-supervised learning?  
A) ✓ Fine-tuning updates all weights to measure representation usefulness on labeled tasks.  
B) ✓ Linear probing tests how linearly separable the learned features are.  
C) ✓ k-nearest neighbors uses feature similarity without additional training.  
D) ✗ Pretext task accuracy is not a reliable measure of representation quality.  

**Correct:** A, B, C


#### 6. Why is text particularly well-suited for self-supervised learning approaches?  
A) ✗ Text data is mostly unlabeled; labels are not provided explicitly.  
B) ✓ Large volumes of unlabeled text are widely available, unlike labeled datasets.  
C) ✓ The distributional hypothesis supports learning word meaning from context.  
D) ✓ Discrete tokens allow masking any word and using the original as a free label.  

**Correct:** B, C, D


#### 7. Which of the following correctly describe differences between static and contextual word embeddings?  
A) ✓ Contextual embeddings produce different vectors for the same word depending on sentence context.  
B) ✓ ELMo uses bidirectional LSTMs to create contextualized word representations.  
C) ✓ Static embeddings assign one fixed vector per word regardless of context.  
D) ✗ Word2Vec and GloVe produce static embeddings, not contextual ones.  

**Correct:** A, B, C


#### 8. In Masked Language Modelling (MLM) as used in BERT, which of the following are true?  
A) ✓ Next sentence prediction is a secondary task to improve sentence-level understanding.  
B) ✓ The model predicts masked tokens using context from both left and right sides.  
C) ✓ 80% of selected tokens become [MASK], 10% random tokens, and 10% unchanged.  
D) ✗ Not all selected tokens are replaced with [MASK]; only 80% are masked.  

**Correct:** A, B, C


#### 9. How do autoregressive language models like GPT differ from masked language models like BERT?  
A) ✓ GPT predicts the next token using only left-side tokens, making it unidirectional.  
B) ✓ BERT predicts masked tokens using context from both directions (bidirectional).  
C) ✗ GPT uses a Transformer decoder, not a bidirectional encoder like BERT.  
D) ✓ GPT is naturally suited for generation; BERT excels at classification and tagging.  

**Correct:** A, B, D


#### 10. Which statements about advanced SSL text models such as RoBERTa, XLNet, and ELECTRA are correct?  
A) ✓ XLNet uses permutation language modeling to incorporate bidirectional context while maintaining autoregressive training.  
B) ✓ RoBERTa removes next sentence prediction and uses dynamic masking with larger batches and more data.  
C) ✗ All three models modify BERT’s original training objective; none rely exclusively on it.  
D) ✓ ELECTRA trains a generator to replace tokens and a discriminator to detect replaced tokens, considering all tokens.  

**Correct:** A, B, D