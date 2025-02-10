# Boston Air Quality Predictor (BAQP)
 _Time-Series Machine Learning for Next-Day AQI Forecasting in Boston._
# Executive Summary
Air Quality Index is a clear and standardized indicator of air pollution levels, and is of great significance for individuals, communities and policy makers to make well informed decisions to protect the environment and public health. By leveraging spatial and temporal geographic information, we aim to build an accurate and robust Air Quality Index Predictor for Boston city.


# Project Description
This project aims to predict Boston’s next-day Air Quality Index (AQI) using past year’s air quality and weather data. We will analyze variables such as temperature, wind speed, and precipitation. We hope to identify key influences on air pollution and improve forecasting accuracy. We aim to collect at least 10 years of AQI data from aqi and weather data from sources of local database. Our approach includes baseline models such as linear regression, alongside more advanced methods like LSTM and Random Forest Regressor to capture time-series consistentices and variations. Visualization will include time-series plots, correlation heatmaps, and feature importance charts. Seasonal variations will also be analyzed to ensure model robustness.
By leveraging machine learning, this project aims to develop a practical tool for AQI prediction, helping Boston residents and policymakers make informed decisions about air quality.


# Goals
- Prediction Accuracy: Forecast next-day AQI with improved accuracy over baseline models (moving average & linear regression). We will identify weather factors such as temperature, wind speed and precipitation that can impact AQI and analyze seasonal trends.

- Data Processing will be used through collecting and cleaning at least 10 years of AQI and weather data, handling missing values and outliers. Visualization through the use of time-series plots, heatmaps, and feature importance charts to interpret model predictions. Lastly, we will use model robustness to ensure consistency across seasons and test on extreme AQI events.



# Data Collection 
- Source: 
We will be using online resources for data collection from the last 10 years of Boston, MA. We will use reputable sources such as https://aqicn.org/historical/#!city:boston, https://www.wunderground.com/history/monthly/us/ma/boston and other government databases. 

- Features:
  - Temperature: the temperature daily
  - Air quality index ( AQI): determining the pollution in the air 
  - Wind speed: direction of the wind and speed
  - Precipitation: the amount of rainfall or snowfall recorded each day.
  - Time of day: the air quality can change throughout the day 


# Data Cleaning
To make sure our data is accurate and useful for predicting air quality, we will clean it by:

- Filling in Missing Data: If there are gaps in AQI, temperature, or wind speed data, we will estimate the missing values using simple methods like averaging nearby data points or carrying forward previous values when appropriate.
- Removing Errors and Outliers: Sometimes, sensors might record incorrect values, like a sudden spike in AQI that doesn’t match the trend. We will identify and remove these extreme values using statistical methods.
- Smoothing Data: Air quality readings can fluctuate due to sudden short-term factors like traffic or temporary weather changes. These fluctuations can make it harder for the model to detect trends. To reduce this, we will take Rolling Averages. We will take the average AQI over a small time window, to smooth out short-term fluctuations and highlight long-term trends.

# Feature Extraction
- Past AQI Values: Using AQI from previous days (1-day, 3-day) to help the model detect trends.
- Rolling Averages: Smoothing AQI fluctuations by averaging values over the past few days.
- Weather Factors: Including temperature, humidity, and wind speed to account for their impact on air quality.
- Time-Based Features: Adding day of the week and season to reflect pollution patterns.

Since these factors have different units, we will scale them for consistency.

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
