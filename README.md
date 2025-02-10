# Boston Air Quality Predictor (BAQP)
 Time-Series Machine Learning for Next-Day AQI Forecasting in Boston.
# Executive Summary
Air Quality Index is a clear and standardized indicator of air pollution levels, and is of great significance for individuals, communities and policy makers to make well informed decisions to protect the environment and public health. By leveraging spatial and temporal geographic information, we aim to build an accurate and robust Air Quality Index Predictor for Boston city.


# Project Description
This project’s goal is to predict stock price movements using past stock prices and options data. We aim to develop a model that can provide better-than-random predictions of stock returns using machine learning methods, helping investors make more informed decisions. The project will include data collection, cleaning, feature extraction, visualization, model training, and more.
Stock price prediction is a hard task to predict due to the highly volatile nature of the financial markets. But by using options data such as implied volatility and open interest, we aim to draw out signs that may indicate future stock price movements.
Our approach will involve testing various machine learning models, from linear regression to more complex deep learning architectures, to find which method provides the best predictions. The model's performance will be evaluated against a buy-and-hold guideline strategy to determine its practical use.


# Goals
- Create a predictive model for short-term stock price movements by using past stock data and options market indicators.
- Identify the most important features, such as implied volatility, open interest, trading volume) that correlate with fluctuations in stock prices.
- Construct a machine learning conduit that can be applied to multiple stocks
- Analyze model performance against benchmark strategies (buy-and-hold, simple moving average strategies) to assess its practicality and effectiveness.
- Visualize financial market patterns and feature importance through time-series plots to compare and contrast actual stock price movements with our model predictions.
- Optimize predictive accuracy and generalizability by experimenting with different modeling techniques.


# Data Collection 
- Source: 
We will be using online resources for data collection from the last 10 years of Boston, MA. We will use reputable sources such as https://aqicn.org/historical/#!city:boston and government databases. 

- Features:
  - Weather: the temperature daily
  - Air quality index ( AQI): determining the pollution in the air 
  - Wind speed: direction of the wind and speed
  - Time of day: the air quality can change throughout the day 


# Data Cleaning




# Feature Extraction




# Modelling
- Model Architecture: develop a machine learning model to predict the next day’s AQI in Boston using historical air quality and weather data. We will try testing different architectures including LSTM, OLS Linear Regression and Random Forest Regressor.

- Training Approach: 
  - Supervised Learning: Train the model on historical AQI and weather features to learn the probability distribution of AQI values for the next day. Experiment with different loss functions (e.g., MSE, MAE) and optimizers (Adam, SGD).


# Visualization
- Embedding Space Analysis: 
Dimensionality Reduction (PCA, t-SNE, UMAP). Convert high-dimensional AQI and meteorological features into a lower-dimensional space. Visualize how different weather conditions cluster based on their impact on air quality.

- Generated Air Quality Visualization: Heatmaps for Spatial Trends. 

- Time-Series Forecast Plots: Compare real vs. predicted AQI trends using Matplotlib. Show confidence intervals around predictions.


# Test Plan / Metrics
- Data Split:
  - Training Set (80%): Train the model on historical AQI and weather data from different seasons over the past 10 years (without the last two years).
  - Testing Set (20%): split about 20% of our data (recently two years' data) as validation data to test as we train the model.

- Evaluation Metrics:
  - Mean Absolute Error (MAE): Measures the average absolute difference between predicted and actual AQI values.
  - Mean Squared Error (MSE): Penalizes larger errors more than MAE, useful for assessing severe mispredictions.
  - R-squared (R²): Measures how well the model explains the variance in AQI.
  - Prediction Stability: Compare next-day predictions over different test periods to ensure consistency and avoid erratic fluctuations.
