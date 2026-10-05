## 9. Time Series Analysis and Forecasting

## Questions

#### 1. Which of the following statements correctly describe characteristics of time series data?  
A) Time series data always have a fixed periodicity in their cyclical component.  
B) Statistical properties such as mean and variance may change over time in non-stationary series.  
C) Temporal dependence means current observations are independent of past values.  
D) Temporal order of observations is essential for meaningful analysis.  

#### 2. Which of the following are valid methods to handle missing values in time series data without causing data leakage?  
A) Forward fill applied after splitting the dataset into train, validation, and test sets.  
B) Linear interpolation applied before splitting the dataset.  
C) Mean imputation applied only on the training set, then applied to validation and test sets.  
D) Using GAN-based imputation on the entire dataset before splitting.  

#### 3. Consider a time series with a strong upward trend and clear weekly seasonality. Which preprocessing steps would be most appropriate before applying an ARIMA model?  
A) Differencing to remove the trend component.  
B) Applying log transformation to stabilize variance.  
C) Removing seasonality by seasonal differencing or decomposition.  
D) Normalizing the data using min-max scaling on the entire dataset before splitting.  

#### 4. Which of the following statements about autocorrelation and partial autocorrelation functions (ACF and PACF) are true?  
A) ACF shows both direct and indirect correlations at different lags.  
B) Values close to zero in ACF or PACF indicate strong correlation.  
C) PACF is useful for identifying the order of autoregressive terms in an AR model.  
D) PACF isolates the direct correlation at a specific lag by removing intermediate lag effects.  

#### 5. In multi-step time series forecasting, which of the following approaches can be used, and what are their characteristics?  
A) Multiple-output approach: Trains separate models for each forecast horizon.  
B) Direct approach: Uses a single model to predict all future steps simultaneously.  
C) Recursive approach: Predicts one step ahead and feeds predictions back as inputs for subsequent steps.  
D) Direct approach: Builds separate models for each forecast horizon, each predicting a specific future time step.  

#### 6. Which of the following are challenges specific to multivariate time series forecasting compared to univariate forecasting?  
A) Curse of dimensionality increases risk of overfitting with many predictors.  
B) Multicollinearity among predictor variables complicates estimation of individual effects.  
C) Stationarity is not required for multivariate forecasting models.  
D) Differences in variable scales require normalization to avoid bias.  

#### 7. When splitting time series data into training, validation, and test sets, which of the following practices are correct?  
A) Split the data chronologically to prevent temporal information leakage.  
B) Use a typical split ratio of 70% train, 10% validation, and 20% test.  
C) Normalize the entire dataset before splitting to maintain consistent scaling.  
D) Randomly shuffle the entire dataset before splitting to ensure data diversity.  

#### 8. Which of the following statements about the irregular (residual) component of a time series are accurate?  
A) It often follows a normal distribution with mean zero.  
B) It represents random fluctuations that cannot be explained by trend, seasonality, or cycles.  
C) It is usually the dominant component in long-term economic time series.  
D) It can be used to detect outliers and assess forecast uncertainty.  

#### 9. In panel data forecasting, which of the following issues must be addressed to build effective models?  
A) Cross-sectional dependence, where values of one entity influence others.  
B) Ensuring all entities have identical value ranges to avoid bias.  
C) Handling unbalanced panels due to missing data at different time points.  
D) Heterogeneity, where different entities exhibit distinct temporal patterns.  

#### 10. Which of the following evaluation metrics are suitable for assessing probabilistic time series forecasts?  
A) Prediction Interval Coverage Probability (PICP)  
B) Mean Absolute Error (MAE)  
C) Continuous Ranked Probability Score (CRPS)  
D) Pinball Loss (Quantile Loss)  



<br>

## Answers

#### 1. Which of the following statements correctly describe characteristics of time series data?  
A) ✗ Cyclical components do not have fixed periodicity; they are irregular and vary in length.  
B) ✓ Non-stationary series have changing mean, variance, or covariance over time.  
C) ✗ Temporal dependence means current values are influenced by past values, not independent.  
D) ✓ Temporal order is essential because time series analysis depends on the sequence of observations.  

**Correct:** B, D


#### 2. Which of the following are valid methods to handle missing values in time series data without causing data leakage?  
A) ✓ Forward fill after splitting avoids using future data, preventing leakage.  
B) ✗ Interpolation before splitting uses future values, causing data leakage.  
C) ✓ Mean imputation fitted only on training data prevents leakage when applied to validation/test.  
D) ✗ GAN-based imputation on full data before splitting leaks future information.  

**Correct:** A, C


#### 3. Consider a time series with a strong upward trend and clear weekly seasonality. Which preprocessing steps would be most appropriate before applying an ARIMA model?  
A) ✓ Differencing removes trend, making series stationary for ARIMA.  
B) ✓ Log transformation stabilizes variance, often needed for ARIMA assumptions.  
C) ✓ Seasonal differencing or decomposition removes weekly seasonality, improving model fit.  
D) ✗ Normalizing on the entire dataset before splitting leaks future information and is not standard for ARIMA.  

**Correct:** A, B, C


#### 4. Which of the following statements about autocorrelation and partial autocorrelation functions (ACF and PACF) are true?  
A) ✓ ACF shows total correlation at each lag, including indirect effects.  
B) ✗ Values near zero indicate weak or no correlation, not strong correlation.  
C) ✓ PACF helps identify AR order by showing direct lag correlations.  
D) ✓ PACF isolates direct correlation at a lag by removing effects of intermediate lags.  

**Correct:** A, C, D


#### 5. In multi-step time series forecasting, which of the following approaches can be used, and what are their characteristics?  
A) ✗ Multiple-output approach is a single model predicting all horizons, not separate models.  
B) ✗ Multiple-output approach (not direct) predicts all future steps simultaneously with one model.  
C) ✓ Recursive approach predicts one step ahead and feeds predictions back for next steps.  
D) ✓ Direct approach builds separate models for each forecast horizon.  

**Correct:** C, D


#### 6. Which of the following are challenges specific to multivariate time series forecasting compared to univariate forecasting?  
A) ✓ Curse of dimensionality increases complexity and overfitting risk with many predictors.  
B) ✓ Multicollinearity complicates estimating individual predictor effects.  
C) ✗ Stationarity is still important for many multivariate models; it is not ignored.  
D) ✓ Different variable scales require normalization to avoid bias in modeling.  

**Correct:** A, B, D


#### 7. When splitting time series data into training, validation, and test sets, which of the following practices are correct?  
A) ✓ Chronological splitting preserves temporal order and prevents leakage.  
B) ✓ 70:10:20 is a common and reasonable split ratio for time series.  
C) ✗ Normalizing before splitting leaks future information; scaler must be fit on training only.  
D) ✗ Random shuffling breaks temporal order and causes information leakage.  

**Correct:** A, B


#### 8. Which of the following statements about the irregular (residual) component of a time series are accurate?  
A) ✓ It is often modeled as normally distributed with mean zero.  
B) ✓ Irregular component is random noise unexplained by trend, seasonality, or cycles.  
C) ✗ Irregular component is usually not dominant in long-term economic series; trend/cycles dominate.  
D) ✓ Useful for detecting outliers and assessing forecast uncertainty.  

**Correct:** A, B, D


#### 9. In panel data forecasting, which of the following issues must be addressed to build effective models?  
A) ✓ Cross-sectional dependence means entities influence each other, complicating modeling.  
B) ✗ Entities rarely have identical value ranges; normalization is used to handle differences.  
C) ✓ Unbalanced panels with missing data require imputation or omission strategies.  
D) ✓ Heterogeneity means entities behave differently, requiring flexible modeling.  

**Correct:** A, C, D


#### 10. Which of the following evaluation metrics are suitable for assessing probabilistic time series forecasts?  
A) ✓ PICP measures coverage of prediction intervals, relevant for probabilistic forecasts.  
B) ✗ MAE is for point forecasts, not probabilistic forecast evaluation.  
C) ✓ CRPS evaluates the quality of full predictive distributions.  
D) ✓ Pinball Loss measures quantile forecast accuracy, suitable for probabilistic forecasts.  

**Correct:** A, C, D