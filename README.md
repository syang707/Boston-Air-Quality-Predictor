# -Boston-Air-Quality-Predictor-BAQP-
 Boston Air Quality Predictor (BAQP) Time-Series Machine Learning for Next-Day AQI Forecasting in Boston.
# Executive Summary
Air Quality Index is a clear and standardized indicator of air pollution levels, and is of great significance for individuals, communities and policy makers to make well informed decisions to protect the environment and public health. By leveraging spatial and temporal geographic information, we aim to build an accurate and robust Air Quality Index Predictor for Boston city.




# Project Description





# Goals





# Data Collection
Source: 
We will be using online resources for data collection from the last 10 years of Boston. We will use reputable sources such as https://aqicn.org/historical/#!city:boston and government databases. 

Features:
Features will include weather, temperature, air quality index (AQI), and wind speed.





# Data Cleaning




# Feature Extraction




# Modelling
Model Architecture: develop a machine learning model to predict the next day’s AQI in Boston using historical air quality and weather data. We will try testing different architectures including LSTM, OLS Linear Regression and Random Forest Regressor.

Training Approach: 
Supervised Learning: Train the model on historical AQI and weather features to learn the probability distribution of AQI values for the next day. Experiment with different loss functions (e.g., MSE, MAE) and optimizers (Adam, SGD).


# Visualization
Embedding Space Analysis: 
Dimensionality Reduction (PCA, t-SNE, UMAP). Convert high-dimensional AQI and meteorological features into a lower-dimensional space. Visualize how different weather conditions cluster based on their impact on air quality.

Generated Air Quality Visualization: Heatmaps for Spatial Trends. 

Time-Series Forecast Plots: Compare real vs. predicted AQI trends using Matplotlib. Show confidence intervals around predictions.


# Test Plan / Metrics
Data Split:
Training Set (80%): Train the model on historical AQI and weather data from different seasons over the past 10 years (without the last two years).
Testing Set (20%): split about 20% of our data (recently two years' data) as validation data to test as we train the model.

Evaluation Metrics:
Mean Absolute Error (MAE): Measures the average absolute difference between predicted and actual AQI values.
Mean Squared Error (MSE): Penalizes larger errors more than MAE, useful for assessing severe mispredictions.
R-squared (R²): Measures how well the model explains the variance in AQI.
Prediction Stability: Compare next-day predictions over different test periods to ensure consistency and avoid erratic fluctuations.
