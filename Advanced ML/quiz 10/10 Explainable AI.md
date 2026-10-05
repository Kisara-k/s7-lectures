## 10. Explainable AI

## Questions

#### 1. What distinguishes interpretability from explainability in AI models?  
A) Interpretability focuses on clarity of the model’s inner workings, explainability focuses on translating model decisions for humans.  
B) Interpretability requires high human effort, whereas explainability is automatic and requires no tools.  
C) Interpretability is inherent to simple models, while explainability uses external methods for complex models.  
D) Explainability applies only to white-box models, interpretability applies only to black-box models.  

#### 2. Which of the following statements about the black box problem are true?  
A) Complex models like CNNs and Transformers have millions of parameters making them hard to interpret directly.  
B) Black box models provide predictions without revealing internal decision logic.  
C) High accuracy of a model guarantees high trustworthiness.  
D) The black box problem only occurs in models with fewer than 100 parameters.  

#### 3. Which dimensions are essential to consider when choosing an explainability method?  
A) Model Type – whether the model is white-box or black-box.  
B) Granularity – whether explanation is global or local.  
C) Training dataset size – whether the dataset is large or small.  
D) Model Dependence – whether the method is model-specific or model-agnostic.  

#### 4. Feature attribution methods:  
A) Are only applicable to tabular data models, not vision or NLP.  
B) Work by training a simpler surrogate model to approximate the complex model.  
C) Identify which input features or neurons most influenced a model’s prediction.  
D) Include techniques like SHAP, Integrated Gradients, and Grad-CAM.  

#### 5. Surrogate model methods:  
A) Examples include LIME and decision tree surrogates.  
B) Require access to the internal weights of the original complex model.  
C) Train a simple interpretable model to mimic the behavior of a complex black-box model.  
D) Are always global explanations and cannot provide local explanations.  

#### 6. Counterfactual explanations are particularly useful when:  
A) Explaining why a specific prediction was made by showing similar examples.  
B) The model is inherently interpretable and simple.  
C) Users want actionable guidance on how to change inputs to alter predictions.  
D) Fairness and transparency in decision-making are critical.  

#### 7. Which of the following presentation techniques are best suited for non-technical audiences?  
A) Visual heatmaps like Grad-CAM for image models.  
B) Numerical tables of SHAP or LIME scores without any visualization.  
C) Textual explanations with natural language summaries and highlighted tokens.  
D) Symbolic rules and decision trees with complex branching logic.  

#### 8. Regarding model-specific intrinsic explainability:  
A) It is applicable only to black-box models with millions of parameters.  
B) It leverages internal structures like attention maps or filter activations to explain predictions.  
C) It requires post-hoc external tools to interpret the model.  
D) Examples include decision trees, linear regression, CNNs with Grad-CAM, and Transformers with attention visualization.  

#### 9. Which of the following statements about explainability dimensions is correct?  
A) Model-agnostic methods can be applied to any model type, regardless of complexity.  
B) Global explanations focus on understanding individual predictions only.  
C) Model-specific methods are designed to work with any model without modification.  
D) Local explanations help understand the overall behavior of the model across the dataset.  

#### 10. Why is the presentation of explanations critical in Explainable AI?  
A) Because post-hoc explanation outputs like SHAP values need to be converted into human-readable formats.  
B) Because explanations alone guarantee human understanding without further effort.  
C) Because even white-box models require visualization to improve human comprehension.  
D) Because different stakeholders (e.g., doctors, policymakers) require tailored explanation formats to interpret results effectively.  



<br>

## Answers

#### 1. What distinguishes interpretability from explainability in AI models?  
A) ✓ Interpretability focuses on clarity of inner workings; explainability translates decisions for humans.  
B) ✗ Explainability requires human effort and tools; it is not automatic or effortless.  
C) ✓ Interpretability is inherent to simple models, while explainability uses external methods for complex models.  
D) ✗ Explainability applies mainly to complex (black-box) models, not only white-box; interpretability applies to simple models.  

**Correct:** A, C


#### 2. Which of the following statements about the black box problem are true?  
A) ✓ Complex models like CNNs and Transformers have millions of parameters making them hard to interpret.  
B) ✓ Black box models provide predictions without revealing internal decision logic.  
C) ✗ High accuracy does not guarantee trust if the model is not interpretable.  
D) ✗ The black box problem occurs in complex models, not those with very few parameters.  

**Correct:** A, B


#### 3. Which dimensions are essential to consider when choosing an explainability method?  
A) ✓ Model Type (white-box vs black-box) is essential.  
B) ✓ Granularity (global vs local) is a key dimension.  
C) ✗ Training dataset size is not a core dimension of explainability methods.  
D) ✓ Model Dependence (model-specific vs agnostic) is important.  

**Correct:** A, B, D


#### 4. Feature attribution methods:  
A) ✗ They apply to tabular, vision, audio, and NLP data, not just tabular.  
B) ✗ Surrogate models are a different explainability approach, not feature attribution.  
C) ✓ They identify which input features or neurons influenced the prediction.  
D) ✓ SHAP, Integrated Gradients, and Grad-CAM are typical feature attribution methods.  

**Correct:** C, D


#### 5. Surrogate model methods:  
A) ✓ LIME and decision tree surrogates are common examples.  
B) ✗ They do not require access to internal weights, only inputs and outputs.  
C) ✓ They train a simple interpretable model to mimic a complex model’s behavior.  
D) ✗ Surrogates can be local (e.g., LIME) or global (e.g., decision tree surrogates).  

**Correct:** A, C


#### 6. Counterfactual explanations are particularly useful when:  
A) ✗ Explaining by similar examples is example-based explanation, not counterfactual.  
B) ✗ They are mainly for complex, non-interpretable models, not inherently simple ones.  
C) ✓ Users want actionable guidance on how to change inputs to alter predictions.  
D) ✓ Fairness and transparency needs make counterfactuals valuable.  

**Correct:** C, D


#### 7. Which of the following presentation techniques are best suited for non-technical audiences?  
A) ✗ Visual heatmaps may be hard for non-experts to interpret without guidance.  
B) ✗ Numerical tables alone are often too technical and hard to interpret without visualization.  
C) ✓ Natural language summaries and highlighted tokens are accessible to non-technical users.  
D) ✗ Symbolic rules and complex trees are usually too technical for lay audiences.  

**Correct:** C


#### 8. Regarding model-specific intrinsic explainability:  
A) ✗ It applies to interpretable parts of models, not only black-box models with millions of parameters.  
B) ✓ It uses internal structures like attention maps or filter activations to explain predictions.  
C) ✗ It does not require post-hoc external tools; it leverages built-in model features.  
D) ✓ Examples include decision trees, linear regression, CNNs with Grad-CAM, and Transformers with attention visualization.  

**Correct:** B, D


#### 9. Which of the following statements about explainability dimensions is correct?  
A) ✓ Model-agnostic methods can be applied to any model type regardless of complexity.  
B) ✗ Global explanations focus on overall model behavior, not individual predictions.  
C) ✗ Model-specific methods are designed for particular model types, not any model.  
D) ✗ Local explanations focus on individual predictions, not overall model behavior.  

**Correct:** A


#### 10. Why is the presentation of explanations critical in Explainable AI?  
A) ✓ Post-hoc outputs like SHAP values need human-readable formats to be useful.  
B) ✗ Explanations alone do not guarantee understanding without clear presentation.  
C) ✓ Even white-box models benefit from visualization to improve comprehension.  
D) ✓ Different stakeholders require tailored formats for effective interpretation.  

**Correct:** A, C, D