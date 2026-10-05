## 9. Time Series Analysis and Forecasting

## Key Points

#### 1. 📅 Definition of Time Series  
- A time series is a sequence of data points collected at successive, evenly spaced time intervals.  
- Time series data can be univariate, multivariate, or panel data.  

#### 2. 🔍 Components of Time Series  
- Trend represents the long-term movement in data (upward, downward, stationary, or non-linear).  
- Seasonal component shows regular, predictable patterns repeating over fixed periods (daily, weekly, monthly, yearly).  
- Cyclical component involves long-term oscillations without fixed periods, typically lasting 2-10+ years.  
- Irregular component consists of random, unpredictable fluctuations (noise or residuals).  

#### 3. 📈 Stationarity  
- A time series is stationary if mean, variance, and covariance remain constant over time.  
- Augmented Dickey-Fuller (ADF) test is used to check stationarity; p-value ≤ 0.05 indicates stationarity.  
- Non-stationary data can be transformed by differencing or applying log/square root transformations.  

#### 4. 🔄 Lag and Autocorrelation  
- Lag k compares the value at time t with the value at time t-k.  
- Autocorrelation Function (ACF) measures overall correlation across lags.  
- Partial Autocorrelation Function (PACF) measures direct correlation at a specific lag after removing intermediate effects.  

#### 5. 🔮 Time Series Forecasting  
- Forecasting predicts future values based on past observations, preserving temporal order.  
- Single-step forecasting predicts one step ahead; multi-step forecasting predicts multiple future steps.  
- Multi-step forecasting methods: recursive, direct, and multiple-output approaches.  
- Train-validation-test splits must be chronological to avoid temporal leakage (typical ratio 70:10:20).  

#### 6. 🛠️ Preprocessing Techniques  
- Missing values can be imputed using mean/median, forward/backward fill, interpolation, or deep learning methods.  
- Noise reduction is done via smoothing techniques like moving average and exponential smoothing.  
- Outliers are detected using Z-score or IQR and handled by imputation or smoothing.  
- Normalization methods include Min-Max scaling and Z-score normalization; scalers must be fit only on training data.  
- Data augmentation techniques include jittering and scaling to increase dataset diversity.  
- Feature engineering involves creating lag features, rolling statistics, calendar features, and domain-specific variables.  
- Sequence creation converts time series into overlapping input-output pairs for modeling.  

#### 7. 📊 Evaluation Metrics  
- Forecasting errors are measured using MAE, MSE, RMSE, and MAPE.  
- Choice of metric depends on data characteristics and forecasting goals.  

#### 8. 🚀 Advanced Topics  
- Probabilistic forecasting predicts a range of outcomes with uncertainty, evaluated by Pinball Loss, CRPS, and PICP.  
- Multivariate forecasting uses multiple predictor variables to improve accuracy but faces challenges like multicollinearity and dimensionality.  
- Panel data forecasting predicts multiple entities simultaneously, dealing with heterogeneity, cross-sectional dependence, and unbalanced data.



<br>

