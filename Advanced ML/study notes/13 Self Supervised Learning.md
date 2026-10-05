## 13. Self Supervised Learning

## Study Notes

### 1. 🤖 What is Self-Supervised Learning (SSL)?

Self-Supervised Learning (SSL) is a special type of machine learning that sits between supervised and unsupervised learning. Unlike supervised learning, which requires large amounts of labeled data (where humans provide the correct answers), SSL uses unlabeled data but still creates a learning signal by generating labels from the data itself. This means the model learns by predicting parts of the data that are hidden or withheld during training.

#### How SSL fits in the learning spectrum:
- **Supervised learning:** The model learns from input-output pairs where labels are provided by humans (e.g., images labeled as cats or dogs).
- **Unsupervised learning:** The model tries to find patterns or structure in unlabeled data (e.g., clustering similar data points).
- **Self-supervised learning:** The model creates its own labels from the data and learns to predict them, combining the advantages of both supervised and unsupervised learning.

#### Why SSL?
- Deep learning models need huge amounts of data to perform well.
- Labeling data is expensive, slow, and sometimes impossible (e.g., medical images requiring expert annotation).
- Unlabeled data (images, text) is abundant and cheap.
- SSL aims to learn useful, general-purpose representations from raw data without human labeling.

#### How SSL works in practice:
- The model is given a task (called a **pretext task**) where some part of the data is hidden or altered.
- The model tries to predict the missing or altered part.
- The accuracy of this pretext task itself is not the main goal; instead, the learned internal representation (the **encoder**) is what matters.
- This encoder can then be fine-tuned or used for other downstream tasks like classification, detection, or question answering.


### 2. 🖼️ SSL with Image Data: From Puzzles to Masked Modeling

Self-supervised learning for images has evolved over the last decade, moving from simple hand-crafted tasks to sophisticated large-scale models.

#### Early Pretext Tasks (Hand-Crafted Puzzles)
- **Context Prediction:** The model sees two patches from the same image and predicts the relative position of one patch to the other. To solve this, the model must understand object parts and their spatial relationships.
- **Context Encoders:** A large central part of the image is removed, and the model learns to fill in the missing pixels, forcing it to understand the surrounding scene.
- **Colorization:** The model receives only the grayscale (lightness) channel and predicts the color channels, which requires semantic understanding of objects.
- **Jigsaw Puzzles:** The image is split into tiles, shuffled, and the model predicts the correct arrangement.
- **Rotation Prediction (RotNet):** The model predicts the rotation angle applied to an image (0°, 90°, 180°, 270°).

**Limitations:** These tasks are hand-designed and models sometimes find shortcuts by exploiting low-level cues (like color distortions) rather than truly understanding the image.

#### Contrastive Learning: Learning by Comparison
- Instead of hand-crafted puzzles, contrastive learning trains the model to bring different augmented views of the same image closer in the feature space, while pushing apart views of different images.
- This approach uses a loss function called **InfoNCE**, which maximizes mutual information between views.
- Example: **SimCLR** framework applies strong augmentations (cropping, color distortion) and uses a nonlinear projection head to improve representation quality.
- Contrastive learning benefits from large batch sizes and longer training.

#### Masked Image Modeling: Inspired by Language Models
- Inspired by BERT in NLP, models like **BEiT** and **MAE** mask random patches of an image and train the model to predict the missing content.
- **BEiT** predicts discrete visual tokens from a pre-trained tokenizer.
- **MAE** reconstructs raw pixels directly and masks a large portion (up to 75%) of the image patches.
- This approach forces the model to learn semantic understanding of images and achieves state-of-the-art results.

#### Evaluating Image SSL Models
- **Linear probing:** Freeze the encoder and train a simple linear classifier on top to test how linearly separable the learned features are.
- **k-Nearest Neighbors (k-NN):** Classify test images based on nearest neighbors in feature space without additional training.
- **Fine-tuning:** Update all model weights on labeled data to see how well the representation adapts.
- **Transfer learning:** Apply the encoder to new tasks (e.g., object detection) to test generalizability.


### 3. 📚 SSL with Textual Data: Learning Language from Raw Text

Text data is naturally suited for SSL because it is a sequence of discrete tokens (words or subwords), and we can easily hide or mask tokens to create prediction tasks.

#### Why SSL works well for text:
- The **distributional hypothesis** states that words appearing in similar contexts tend to have similar meanings.
- Massive amounts of unlabelled text are available (books, Wikipedia, web).
- Labeling text data is expensive and limited.
- SSL enables models to learn rich language representations from raw text.

#### Early Word Embeddings: Static Vectors
- **word2vec:** Predicts surrounding words from a center word (CBOW) or vice versa (skip-gram). Produces fixed vectors for each word.
- **GloVe:** Uses global co-occurrence statistics to learn word vectors whose dot products approximate word co-occurrence counts.
- **Limitation:** Each word has a single vector, ignoring context (e.g., "bank" in "river bank" vs. "bank account").

#### Contextual Word Representations
- **ELMo:** Uses bidirectional LSTMs to produce word embeddings that depend on the entire sentence context, so the same word can have different vectors depending on usage.
- This was a major step forward, improving many NLP tasks.

#### Transformer and Masked Language Modeling (MLM)
- **BERT:** Uses a Transformer encoder to read the whole sentence bidirectionally.
- During training, 15% of tokens are masked, and the model predicts these masked tokens from context.
- Also uses a next sentence prediction task to understand sentence relationships.
- BERT significantly improved benchmarks like GLUE.

#### Autoregressive Models: Predicting Next Token
- **GPT:** A Transformer decoder trained to predict the next token given all previous tokens (left-to-right).
- This makes GPT naturally suited for text generation.
- Pre-training on large corpora followed by fine-tuning on specific tasks improved many NLP benchmarks.

#### Improvements Beyond BERT and GPT
- **RoBERTa:** Improved BERT by removing next sentence prediction, using dynamic masking, larger batches, and more data.
- **XLNet:** Uses permutation language modeling to capture bidirectional context without masking tokens.
- **ELECTRA:** Trains a discriminator to detect replaced tokens generated by a small generator, improving efficiency.

#### Text-to-Text Models
- **T5:** Uses a sequence-to-sequence Transformer trained to reconstruct corrupted spans of text.
- **BART:** A denoising autoencoder that corrupts text in various ways and trains a seq2seq model to reconstruct the original, excelling at generation tasks like summarization.


### 4. 🧪 Evaluating SSL Models: How Do We Know They Work?

Evaluating SSL models focuses on how well the learned representations transfer to real tasks, rather than the accuracy on the pretext task itself.

#### Common evaluation methods:
- **Linear probing:** Freeze the learned encoder and train a simple linear classifier on labeled data. If the features are good, the classifier will perform well.
- **k-Nearest Neighbors (k-NN):** Classify test samples based on nearest neighbors in the learned feature space without any additional training.
- **Fine-tuning:** Update all model parameters on a labeled dataset to see how well the pretrained model adapts.
- **Transfer learning:** Apply the pretrained encoder to different datasets and tasks (e.g., object detection, sentiment analysis) to test generalization.


### 5. 🔍 Summary: Why Self-Supervised Learning Matters

Self-Supervised Learning is a powerful approach that leverages the vast amounts of unlabeled data available today. By creating tasks where the model predicts parts of the data from other parts, SSL enables learning rich, general-purpose representations without costly human annotation.

- In **vision**, SSL evolved from hand-crafted puzzles to contrastive learning and masked image modeling, achieving performance close to or surpassing supervised learning.
- In **language**, SSL moved from static word embeddings to contextual models and large Transformer-based architectures, forming the backbone of modern NLP.
- SSL representations are evaluated by their usefulness on downstream tasks, not just by their performance on the pretext task.
- This approach reduces reliance on labeled data, making AI more scalable and adaptable across domains.