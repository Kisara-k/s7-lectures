## 9. Time Series Analysis and Forecasting

## Study Notes

### 1. 📅 Introduction to Time Series

#### What is a Time Series?

A **time series** is a sequence of data points collected or recorded at regular, evenly spaced time intervals. These intervals could be hourly, daily, weekly, monthly, or yearly. The key feature is that the data points are ordered in time, which means the order of observations matters.

Formally, a time series can be represented as:


$$
y_t, y_{t-1}, y_{t-2}, \ldots
$$


where $y_t$ is the value of the variable at time $t$.

#### Examples of Time Series Data

Time series data is everywhere and appears in many fields:

- **Finance:** Stock prices, exchange rates, interest rates.
- **Meteorology:** Temperature, rainfall, air pressure.
- **Retail:** Sales volume, consumer demand.
- **Economics:** GDP growth, inflation rate, unemployment rate.
- **IoT (Internet of Things):** Sensor readings, electricity consumption, traffic flows.
- **Healthcare:** Patient counts, heart rate, blood pressure.

For example, daily electricity consumption in Sri Lanka or monthly tourism revenues are typical time series datasets.

#### Characteristics of Time Series Data

Understanding the nature of time series data is crucial for analysis:

- **Ordered Nature:** The sequence in which data points occur is essential. Unlike other data types, time order cannot be ignored.
- **Temporal Dependence:** Current values often depend on past values. For example, today’s temperature is likely related to yesterday’s.
- **Temporal Structure:** Time series often show patterns such as:
  - **Trend:** Long-term increase or decrease.
  - **Seasonality:** Regular repeating patterns (e.g., daily, weekly, yearly).
  - **Cyclical Patterns:** Longer-term oscillations without fixed periods.
- **Dynamic Behavior:** Statistical properties like mean and variance may change over time, a phenomenon called **non-stationarity**.

#### Types of Time Series

- **Univariate Time Series:** Observations of a single variable over time (e.g., daily stock price).
- **Multivariate Time Series:** Multiple variables recorded simultaneously over time (e.g., temperature, humidity, and rainfall).
- **Panel Time Series:** Observations of one or more variables for multiple entities over time (e.g., sales data for multiple stores).


### 2. 🔍 Fundamental Components of Time Series

Time series data can be decomposed into several components that help us understand and model the data better.

#### 2.1 Trend Component

The **trend** is the long-term direction or movement in the data. It shows whether the data is generally increasing, decreasing, or stable over a long period, ignoring short-term fluctuations.

- **Upward Trend:** Data values increase over time.
- **Downward Trend:** Data values decrease over time.
- **Stationary/Horizontal:** No significant change over time.
- **Non-linear Trends:** Trends that follow exponential, logarithmic, or polynomial shapes.

#### 2.2 Seasonal Component

**Seasonality** refers to patterns that repeat at fixed intervals, such as daily, weekly, monthly, or yearly cycles. These patterns are often caused by calendar effects or natural phenomena.

Examples:

- Electricity usage peaks during daytime hours (daily seasonality).
- Retail sales increase on weekends (weekly seasonality).
- Tourism peaks during holiday seasons (annual seasonality).

Seasonality helps in planning and resource management.

#### 2.3 Cyclical Component

**Cycles** are long-term fluctuations around the trend but unlike seasonality, they do not have a fixed period. They can last several years and are often related to economic or business cycles.

- Duration: Usually 2 to 10+ years.
- Irregular periods and amplitudes.
- Examples: Economic recessions and expansions.

Cycles are harder to detect because they overlap with other components and require long historical data.

#### 2.4 Irregular Component

The **irregular** or **residual** component represents random, unpredictable fluctuations that cannot be explained by trend, seasonality, or cycles. This is often called "noise."

- Caused by unexpected events like natural disasters or measurement errors.
- Important for validating models and understanding forecast uncertainty.


### 3. 📈 Stationarity and Autocorrelation in Time Series

#### 3.1 What is Stationarity?

A time series is **stationary** if its statistical properties (mean, variance, covariance) do not change over time. Stationarity is important because many forecasting models assume the data is stationary.

- **Stationary:** Constant mean, variance, and covariance over time.
- **Non-stationary:** These properties change over time (e.g., presence of trend or seasonality).

#### How to Test Stationarity?

- **Statistical Test:** Augmented Dickey-Fuller (ADF) test checks for a unit root. If the p-value ≤ 0.05, the series is stationary.
- **Visual Inspection:** Look for trends or seasonality in plots.

#### Making Data Stationary

- **Transformation:** Apply log or square root to stabilize variance.
- **Differencing:** Subtract previous values to remove trends (first-order differencing removes linear trends).

#### 3.2 What is a Lag?

A **lag** refers to how many time steps back we look in the series.

- Lag 1 compares $y_t$ with $y_{t-1}$.
- Lag k compares $y_t$ with $y_{t-k}$.

#### 3.3 Autocorrelation

**Autocorrelation** measures how related a time series is with its past values (lags).

- **ACF (Autocorrelation Function):** Shows overall correlation at different lags.
- **PACF (Partial Autocorrelation Function):** Shows direct correlation at a specific lag after removing effects of intermediate lags.

Positive values indicate positive correlation, negative values indicate negative correlation, and values near zero indicate weak or no correlation.


### 4. 🔮 Time Series Forecasting

#### 4.1 What is Forecasting?

Time series forecasting is predicting future values based on past observations by modeling underlying patterns like trend and seasonality. It helps in decision-making and planning.

Mathematically:


$$
\hat{y}_{t+h} = f(y_t, y_{t-1}, \ldots, y_0)
$$


where $\hat{y}_{t+h}$ is the forecast for $h$ steps ahead.

#### 4.2 Single-step vs Multi-step Forecasting

- **Single-step forecasting:** Predict the next immediate value (h=1).
- **Multi-step forecasting:** Predict multiple future values (h > 1).

Multi-step forecasting can be done in three ways:

- **Recursive:** Predict one step ahead, then use that prediction to predict the next step, and so on.
- **Direct:** Build separate models for each future time step.
- **Multiple-output:** One model predicts all future steps at once.

#### 4.3 Forecasting Horizons

Forecasting horizons define how far into the future predictions are made:

- **Short-term:** Hours to days (e.g., daily sales).
- **Mid-term:** Weeks to months (e.g., inventory planning).
- **Long-term:** Months to years (e.g., economic growth).

#### 4.4 Train-Validation-Test Split in Time Series

Unlike typical machine learning, time series data **cannot be randomly shuffled** because it would break temporal order and cause data leakage.

The correct approach is to split data **chronologically**:

- Train on the earliest data.
- Validate on the next segment.
- Test on the latest segment.

A common split ratio is 70% train, 10% validation, 20% test.


### 5. 🛠️ Preprocessing Time Series Data

Preprocessing is essential to prepare time series data for modeling.

#### 5.1 Handling Missing Values

Missing data can occur due to sensor failure or recording errors and can disrupt continuity.

Common imputation methods:

- **Statistical:** Mean, median, or mode imputation.
- **Forward/Backward Fill:** Use last or next valid observation.
- **Interpolation:** Estimate missing points using linear or spline methods.
- **Deep Learning:** Autoencoders or GANs for imputation.

⚠ Important: Imputation should be done **after splitting** to avoid leaking future information.

#### 5.2 Noise Reduction

Noise refers to random fluctuations that obscure true patterns.

- **Smoothing techniques:**
  - Moving Average: Average over a sliding window.
  - Exponential Smoothing: Weights recent observations more.

#### 5.3 Outlier Handling

Outliers are unusual data points that deviate significantly from the pattern.

- Detect using Z-score or Interquartile Range (IQR).
- Handle by imputation or smoothing.

#### 5.4 Normalization

Scaling data to a standard range improves model training and prevents features with large ranges from dominating.

- **Min-Max Scaling:** Rescales data to [0,1].
- **Z-score Normalization:** Centers data to mean 0 and variance 1.

⚠ Fit scalers only on training data to avoid data leakage.

#### 5.5 Data Augmentation

Creating synthetic variations of data to increase dataset size and diversity, improving model robustness.

- **Jittering:** Add small random noise.
- **Scaling:** Multiply series by a factor.

Used mainly when data is limited.

#### 5.6 Feature Engineering

Creating new features to improve model accuracy:

- **Temporal features:** Lag values, rolling means, differences.
- **Calendar features:** Day of week, month, holidays.
- **Domain-specific:** Weather, promotions, economic indicators.

Deep learning models may require less manual feature engineering.

#### 5.7 Sequence Creation

Time series data is converted into overlapping sequences for model input.

Example:

| Input Sequence (X)       | Target (y) |
|-------------------------|------------|
| [x1, x2, x3]            | x4         |
| [x2, x3, x4]            | x5         |
| [x3, x4, x5]            | x6         |

This sliding window approach helps models learn temporal dependencies.


### 6. 🕰️ Evolution of Time Series Forecasting Models

Time series forecasting has evolved from classical statistical models like ARIMA to advanced machine learning and deep learning models such as Gradient Boosting, DeepAR, and Temporal Fusion Transformers.

Each generation of models improves the ability to capture complex patterns and dependencies in data.


### 7. 📊 Evaluation Metrics for Forecasting

Forecasting is a regression task, so we measure how close predictions are to actual values.

Common metrics:

- **Mean Absolute Error (MAE):** Average absolute difference; easy to interpret.
- **Mean Squared Error (MSE):** Penalizes larger errors more.
- **Root Mean Squared Error (RMSE):** Square root of MSE; same units as data.
- **Mean Absolute Percentage Error (MAPE):** Percentage error; sensitive to zero values.

Choosing the right metric depends on the data and forecasting goals.


### 8. 🚀 Advanced Topics in Time Series Forecasting

#### 8.1 Probabilistic Forecasting

Instead of predicting a single value, probabilistic forecasting estimates a range of possible outcomes with associated probabilities. This helps quantify uncertainty.

Techniques include:

- Statistical models with prediction intervals.
- Machine learning models like Gradient Boosting.
- Deep learning models like DeepAR and Temporal Fusion Transformer.

Evaluation metrics include Pinball Loss and Continuous Ranked Probability Score (CRPS).

#### 8.2 Multivariate Time Series Forecasting

Involves predicting one or more variables using multiple related variables over time.

Example: Forecasting electricity demand using temperature, humidity, and past demand.

Challenges:

- **Multicollinearity:** High correlation among predictors.
- **Curse of dimensionality:** Too many variables can cause overfitting.
- **Normalization:** Needed to handle different scales.
- **Missing data:** Requires imputation.

#### 8.3 Panel Data Forecasting

Forecasting multiple entities (e.g., stores, regions) simultaneously over time.

Example: Predicting monthly sales for multiple stores by leveraging both temporal and cross-sectional patterns.

Challenges:

- **Heterogeneity:** Different entities behave differently.
- **Cross-sectional dependence:** Entities influence each other.
- **Unbalanced data:** Missing values for some entities.
- **Normalization:** Needed due to varying scales.


### Summary

Time series analysis and forecasting involve understanding the temporal structure of data, decomposing it into components, ensuring stationarity, and applying appropriate models to predict future values. Preprocessing steps like handling missing data, noise reduction, and feature engineering are crucial for model success. Advanced forecasting includes probabilistic methods and multivariate or panel data approaches, which handle more complex real-world scenarios.