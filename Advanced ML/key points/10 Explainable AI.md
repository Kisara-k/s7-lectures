## 10. Explainable AI

## Key Points

#### 1. 🤖 Importance of Explainable AI (XAI)
- AI systems make critical decisions in areas like disease diagnosis, loan approval, and agriculture.
- High accuracy in AI models does not guarantee trust without understanding how decisions are made.
- Explainability is needed to make AI decisions understandable and trustworthy.

#### 2. 🔍 Interpretability vs Explainability
- Interpretability is the inherent ability of a model to be understood without external tools.
- Explainability uses external techniques to translate complex model decisions into human-understandable explanations.
- Interpretability applies mostly to simple, transparent models (white-box), while explainability is for complex, opaque models (black-box).

#### 3. 🧩 Key Dimensions of Explainability
- Granularity: Explanations can be global (whole model behavior) or local (single prediction).
- Model Type: White-box models are inherently interpretable; black-box models require explainability methods.
- Model Dependence: Explanation methods can be model-specific (e.g., Grad-CAM for CNNs) or model-agnostic (e.g., LIME, SHAP).

#### 4. 🔧 Core Explainability Methods
- Feature Attribution: Assigns importance scores to input features or neurons influencing predictions (e.g., SHAP, Integrated Gradients, Grad-CAM).
- Surrogate Models: Train simple interpretable models to approximate complex models for explanation (e.g., LIME, decision tree surrogates).
- Example-Based Explanations: Explain predictions by showing similar examples from training data (e.g., kNN, prototypes).
- Counterfactual Explanations: Show minimal input changes needed to alter the model’s prediction (e.g., Wachter counterfactuals, DiCE).
- Model-Specific Intrinsic Explainability: Uses interpretable parts of models like decision tree paths, linear regression weights, CNN filter activations, or transformer attention maps.

#### 5. 🖼️ Presentation of Explanations
- Explanations must be clearly presented to be understood by humans.
- Presentation types include visual (heatmaps, plots), symbolic (rules, trees), textual (natural language, highlighted tokens), numerical (feature importance tables), and interactive/multimodal (dashboards).
- Different audiences require different presentation formats for effective understanding.

#### 6. 🛠️ Common Explainability Techniques
- Integrated Gradients: Measures feature importance relative to a baseline.
- SHAP: Uses game theory to assign fair importance values to features.
- Grad-CAM: Produces heatmaps for CNNs to visualize spatial attention on input data.



<br>

