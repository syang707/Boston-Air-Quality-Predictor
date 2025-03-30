# Boston Air Quality Predictor (BAQP)
 _Time-Series Machine Learning for Next-Day AQI Forecasting in Boston._
# Summary
The Air Quality Index (AQI) is a standardized measure of air pollution levels and plays a crucial role for individuals, communities and policy makers to make well informed decisions to protect the environment and public health. By leveraging spatial and temporal geographic information, we aim to build an accurate and robust Air Quality Index Predictor for Boston city.

Check our introduction vedio here: https://youtu.be/FVC1Gi_Y0Ps

# Project Description
This project aims to predict Boston’s next-day Air Quality Index (AQI) using past ten years’ air quality and weather data. We will analyze variables such as temperature, wind speed, and precipitation. We hope to identify key influences on air pollution and improve forecasting accuracy. We aim to collect the past 10 years of AQI data from aqi and weather data from sources of local database. Our approach includes RNN to capture time-series consistentices and variations. Visualization will include time-series plots. Seasonal variations will also be analyzed to ensure model robustness.
By leveraging machine learning, this project aims to develop a practical tool for AQI prediction, helping Boston residents and policymakers make informed decisions about air quality.

# Goals
- Prediction Accuracy: Forecast next-day AQI with improved accuracy over baseline models (moving average & linear regression). We will identify weather factors such as temperature, wind speed and precipitation that can impact AQI and analyze seasonal trends.

- Data Processing will be used through collecting and cleaning at least 10 years of AQI and weather data, handling missing values and outliers. Visualization through the use of time-series plots, heatmaps, and feature importance charts to interpret model predictions. Lastly, we will use model robustness to ensure consistency across seasons and test on extreme AQI events.


# Dataset
- Source: 
We used online resources for data collection from the last 10 years of Boston, MA, from 2015 January 1st to 2025 January 1st. We will use reputable sources including https://aqicn.org/historical/#!city:boston and https://www.visualcrossing.com/weather-query-builder/ as our database. For the AQI, we calculated from the basic bata to get a daily AQI.

- Features:
  - Temperature: the temperature daily
  - Air quality index ( AQI): determining the pollution in the air 
  - Wind speed: direction of the wind and speed
  - Precipitation: the amount of rainfall or snowfall recorded each day.


# Data preprocessing
To make sure our data is accurate and useful for predicting air quality, we clean it by:

- Filling in Missing Data: If there are gaps in AQI, temperature, or wind speed data, we will estimate the missing values using simple methods like averaging nearby data points or carrying forward previous values when appropriate.
- Removing Errors and Outliers: Sometimes, sensors might record incorrect values, like a sudden spike in AQI that doesn’t match the trend. We identify and remove these extreme values using statistical methods.
- Smoothing Data: Air quality readings can fluctuate due to sudden short-term factors like traffic or temporary weather changes. These fluctuations can make it harder for the model to detect trends. To reduce this, we apply rolling average AQIs over one-day windows to smooth fluctuations and capture long-term trends.

To check the accuracy of our prediction, we used split data into Training Set (80%) to train the model on historical AQI and weather data from different seasons over the past 10 years (without the last two years) and Testing Set (20%) to split the most recent two years of data (20% of the dataset) for validation to test how we trained with the model.
Also, we used Mean Absolute Error (MAE) as our Evaluation Metric to measure the average absolute difference between predicted and actual AQI values.


# Feature Extraction
- Past AQI Values: Using AQI from previous days to help the model detect trends.
- Rolling Averages: Smoothing AQI fluctuations by averaging values over the past few days.
- Weather Factors: Including temperature, humidity, and wind speed to account for their impact on air quality.
- Time-Based Features: Adding day of the week and season to reflect pollution patterns.

Since these factors have different units, we scale them for consistency.


# Modelling
We developed a GRU-based Sequence Model to predict the next day's AQI in Boston using historical air quality and weather data. It implemented a GRU (Gated Recurrent Unit) network for time-series forecasting of AQI and weather features. 

The architecture consists of:
- 3-layer GRU encoder (hidden_size=32) for temporal pattern extraction
- Fully connected decoder network with ReLU activation for multi-feature prediction
- Multi-output Regression: Simultaneously predicts next-day values for temperature, humidity, precipitation, and AQI (4-dimensional output)

- Training Approach: 
  - Supervised Learning: Train the model on historical AQI and weather features to learn the predicted AQI values for the next day. The input is Sliding windows of 3-day historical sequences (normalized) and the output would be the next-day predicted values. Using loss functions (Mean Squared Error (MSE) for joint feature prediction) and optimizers (Adam (lr=0.001) with gradient clipping).
  - Data Handling: a WeatherDataset class with Z-score normalization per feature, Configurable window size (3 days) and prediction horizon (1 day ahead), NaN handling via zero-imputation and Dynamic batching with collate_fn for variable-length sequences.


# Visualization
We used Time-Series Forecast Plots to compare the real AQI vs. predicted AQI trends using Matplotlib. Date-aware x-axis ticks for temporal alignment, and Feature-specific denormalization for interpretable scales. Show confidence intervals around predictions.

- Multi-feature Diagnostics:
  - Separate subplots for temperature, humidity, precipitation, and AQI predictions
  - Shared time axis for cross-feature comparison

![image](https://github.com/user-attachments/assets/315d5c58-a9b6-4c6a-9a0c-e206dcb2cc50)


# Reproducability
In order to reproduce our result, follow these steps:
- download train_with_aqi.csv and forecast.ipynb
- upload train_with_aqi.csv to forecast.ipynb
- run through forecast.ipynb

