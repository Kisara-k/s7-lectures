## 10. Explainable AI

## Questions

#### 1. What distinguishes interpretability from explainability in AI models?  
A) Interpretability is inherent to simple models, while explainability uses external methods for complex models.  
B) Interpretability requires high human effort, whereas explainability is automatic and requires no tools.  
C) Interpretability focuses on clarity of the model’s inner workings, explainability focuses on translating model decisions for humans.  
D) Explainability applies only to white-box models, interpretability applies only to black-box models.  

#### 2. Which of the following statements about the black box problem are true?  
A) High accuracy of a model guarantees high trustworthiness.  
B) Complex models like CNNs and Transformers have millions of parameters making them hard to interpret directly.  
C) Black box models provide predictions without revealing internal decision logic.  
D) The black box problem only occurs in models with fewer than 100 parameters.  

#### 3. Which dimensions are essential to consider when choosing an explainability method?  
A) Granularity – whether explanation is global or local.  
B) Model Type – whether the model is white-box or black-box.  
C) Model Dependence – whether the method is model-specific or model-agnostic.  
D) Training dataset size – whether the dataset is large or small.  

#### 4. Feature attribution methods:  
A) Identify which input features or neurons most influenced a model’s prediction.  
B) Are only applicable to tabular data models, not vision or NLP.  
C) Include techniques like SHAP, Integrated Gradients, and Grad-CAM.  
D) Work by training a simpler surrogate model to approximate the complex model.  

#### 5. Surrogate model methods:  
A) Train a simple interpretable model to mimic the behavior of a complex black-box model.  
B) Are always global explanations and cannot provide local explanations.  
C) Examples include LIME and decision tree surrogates.  
D) Require access to the internal weights of the original complex model.  

#### 6. Counterfactual explanations are particularly useful when:  
A) Users want actionable guidance on how to change inputs to alter predictions.  
B) The model is inherently interpretable and simple.  
C) Explaining why a specific prediction was made by showing similar examples.  
D) Fairness and transparency in decision-making are critical.  

#### 7. Which of the following presentation techniques are best suited for non-technical audiences?  
A) Textual explanations with natural language summaries and highlighted tokens.  
B) Numerical tables of SHAP or LIME scores without any visualization.  
C) Visual heatmaps like Grad-CAM for image models.  
D) Symbolic rules and decision trees with complex branching logic.  

#### 8. Regarding model-specific intrinsic explainability:  
A) It leverages internal structures like attention maps or filter activations to explain predictions.  
B) It requires post-hoc external tools to interpret the model.  
C) Examples include decision trees, linear regression, CNNs with Grad-CAM, and Transformers with attention visualization.  
D) It is applicable only to black-box models with millions of parameters.  

#### 9. Which of the following statements about explainability dimensions is correct?  
A) Global explanations focus on understanding individual predictions only.  
B) Local explanations help understand the overall behavior of the model across the dataset.  
C) Model-agnostic methods can be applied to any model type, regardless of complexity.  
D) Model-specific methods are designed to work with any model without modification.  

#### 10. Why is the presentation of explanations critical in Explainable AI?  
A) Because explanations alone guarantee human understanding without further effort.  
B) Because even white-box models require visualization to improve human comprehension.  
C) Because post-hoc explanation outputs like SHAP values need to be converted into human-readable formats.  
D) Because different stakeholders (e.g., doctors, policymakers) require tailored explanation formats to interpret results effectively.



<br>

## Answers

#### 1. What distinguishes interpretability from explainability in AI models?  
A) ✓ Interpretability is inherent to simple models, while explainability uses external methods for complex models.  
B) ✗ Explainability requires human effort and tools; it is not automatic or effortless.  
C) ✓ Interpretability focuses on clarity of inner workings; explainability translates decisions for humans.  
D) ✗ Explainability applies mainly to complex (black-box) models, not only white-box; interpretability applies to simple models.  

**Correct:** A, C


#### 2. Which of the following statements about the black box problem are true?  
A) ✗ High accuracy does not guarantee trust if the model is not interpretable.  
B) ✓ Complex models like CNNs and Transformers have millions of parameters making them hard to interpret.  
C) ✓ Black box models provide predictions without revealing internal decision logic.  
D) ✗ The black box problem occurs in complex models, not those with very few parameters.  

**Correct:** B, C


#### 3. Which dimensions are essential to consider when choosing an explainability method?  
A) ✓ Granularity (global vs local) is a key dimension.  
B) ✓ Model Type (white-box vs black-box) is essential.  
C) ✓ Model Dependence (model-specific vs agnostic) is important.  
D) ✗ Training dataset size is not a core dimension of explainability methods.  

**Correct:** A, B, C


#### 4. Feature attribution methods:  
A) ✓ They identify which input features or neurons influenced the prediction.  
B) ✗ They apply to tabular, vision, audio, and NLP data, not just tabular.  
C) ✓ SHAP, Integrated Gradients, and Grad-CAM are typical feature attribution methods.  
D) ✗ Surrogate models are a different explainability approach, not feature attribution.  

**Correct:** A, C


#### 5. Surrogate model methods:  
A) ✓ They train a simple interpretable model to mimic a complex model’s behavior.  
B) ✗ Surrogates can be local (e.g., LIME) or global (e.g., decision tree surrogates).  
C) ✓ LIME and decision tree surrogates are common examples.  
D) ✗ They do not require access to internal weights, only inputs and outputs.  

**Correct:** A, C


#### 6. Counterfactual explanations are particularly useful when:  
A) ✓ Users want actionable guidance on how to change inputs to alter predictions.  
B) ✗ They are mainly for complex, non-interpretable models, not inherently simple ones.  
C) ✗ Explaining by similar examples is example-based explanation, not counterfactual.  
D) ✓ Fairness and transparency needs make counterfactuals valuable.  

**Correct:** A, D


#### 7. Which of the following presentation techniques are best suited for non-technical audiences?  
A) ✓ Natural language summaries and highlighted tokens are accessible to non-technical users.  
B) ✗ Numerical tables alone are often too technical and hard to interpret without visualization.  
C) ✗ Visual heatmaps may be hard for non-experts to interpret without guidance.  
D) ✗ Symbolic rules and complex trees are usually too technical for lay audiences.  

**Correct:** A


#### 8. Regarding model-specific intrinsic explainability:  
A) ✓ It uses internal structures like attention maps or filter activations to explain predictions.  
B) ✗ It does not require post-hoc external tools; it leverages built-in model features.  
C) ✓ Examples include decision trees, linear regression, CNNs with Grad-CAM, and Transformers with attention visualization.  
D) ✗ It applies to interpretable parts of models, not only black-box models with millions of parameters.  

**Correct:** A, C


#### 9. Which of the following statements about explainability dimensions is correct?  
A) ✗ Global explanations focus on overall model behavior, not individual predictions.  
B) ✗ Local explanations focus on individual predictions, not overall model behavior.  
C) ✓ Model-agnostic methods can be applied to any model type regardless of complexity.  
D) ✗ Model-specific methods are designed for particular model types, not any model.  

**Correct:** C


#### 10. Why is the presentation of explanations critical in Explainable AI?  
A) ✗ Explanations alone do not guarantee understanding without clear presentation.  
B) ✓ Even white-box models benefit from visualization to improve comprehension.  
C) ✓ Post-hoc outputs like SHAP values need human-readable formats to be useful.  
D) ✓ Different stakeholders require tailored formats for effective interpretation.  

**Correct:** B, C, D