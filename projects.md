---
layout: page
title: Projects
---

### AWS SageMaker - Fraud Detection service

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/aws-SageMaker-fraud-detection)

The goal of this project is to underdstand the complete machine learning work flow 
(from data collection, data storing, data preprocessing, model selection, training and finally to model deployement) 
using AWS SageMaker. I built an end to end fraud detection service system using services provided by AWS.
Trained machine learning job and deployed model using SageMaker, created endpoint that can be invoked by Lambda, 
created API with API Gateway in order to send request to flask application.
Deployed the application on AWS Cloud9 environment and finally integrated the application with SNS service to alert client by sending email when fraud is detected.
<img src="images/fraud.png?raw=true"/>

---
### FPGA Neural Network Accelerator

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/tirumalnaidu/opencl-cnn-accelerator)

We designed a Neural Network Accelerator for Darknet Reference Model (which is 2.9 times faster than AlexNet and attains the same top-1 and 
top-5 performance as AlexNet but with 1/10th the parameters) for 
image classification on Imagenet Dataset on Intel Cyclone V Soc FPGA, while working as a part-time undergrad researcher under 
guidance of [Prof. Vinod Kumar Jain](https://sites.google.com/view/dr-vinod-kumar-jain/home?authuser=0). When connected to ARM Cortex A9 processor using OpenCL framework, 
it achieved around 300% faster inference speed than CPU.
<img src="images/fpga-acc.png?raw=true"/>

---
### Forecasting Air pollution

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/forecasting-air-pollution)

Explored various models for forecasting time series. I then compared the performance of the models over two different metrics. Forecasted the amount of pollution in air based on the historical pollution data. 
Used Beijing pollution public dataset - which contains data from 2010-14, along with extra weather features such as temperature, windspeed, pressure etc.
<img src="images/airp.png?raw=true"/>

---
### Heartbeat anomaly detection

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/jithendrabsy/mini-projects/blob/main/heart-ECG-anomaly-detection/AutoEncoder_AnomalyDetection.ipynb)

Detected anomalies in heartbeats using LSTM Auto-encoder. The dataset used contains 5000 time series sequences with 140
timestamps obtained with ECG and corresponds to heartbeats from a
single patient. Trained and evaluated autoencoder, chose a threshold for anomaly
detection and finally classified unseen examples as normal or anomaly.
<img src="images/heartbeat.png?raw=true"/>

---
### Buy or Sell Stocks? - Dual Moving Average Crossover (DMAC) trading strategy

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/jithendrabsy/mini-projects/blob/main/buy-or-sell-stocks/MARUTI_DMAC.ipynb)

Predicted when to buy or sell stocks using simple dual moving average crossover strategy. And then backtested it over 5 years of stock.
I used Yahoo! finance data downloader to download the stocks of Maruti Suzuki (MARUTI.NS).
A return of 113% in 5 years estimated by DMAC strategy with short and long windows 13 and 48 respectively. However - It is up to the trader to 
choose the number of days to which the two moving averages are set. This should be done 
after testing and evaluating the system thoroughly in the recommended way, using the trader’s method.
<img src="images/buysell.png?raw=true"/>

---
### Stock data analysis and forecasting

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/mini-projects/tree/main/forecasting-Stocks)

This is a playground project where I explored time series data of historical stock prices of some publicly listed companies. 
Stock data was collected using Pandas Datareader with the help of Tiingo API.
Experimented with  Long Short Term Memory(LSTM) networks and Facebook's Prophet to forecast the stocks.
<img src="images/stock.png?raw=true"/>

---
### What's common between top songs on Spotify from 2010-19

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendray/mini--projects/tree/main/when-music-meets-datascience/analyzing-top-spotify-songs_from-2010-19)

Performed analysis on top songs on Spotify charts from 2010-19.
<img src="images/musicds1.png?raw=true"/>

---
### Analyzing my personal Spotify streaming history

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendray/mini--projects/tree/main/when-music-meets-datascience/analyzing-my-music-taste-variation)

Collected my streaming history using Spotipy which is a light weight client to extract many features from Spotify's web API. Analyzed my spotify streaming history to understand how my music taste is varying over time. I then compared my music preferences to top 50 songs of 2019 to see how different my taste is from the world's general preferences.
<img src="images/musicds.png?raw=true"/>

---
### Clustering songs based on features

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendray/mini--projects/tree/main/when-music-meets-datascience/clustering-songs-based-on-features)

I sometimes want to listen relaxing songs of my favorite artists and sometimes more energetic and loud songs. It is hard to manually seperate songs from every album.. So, I performed clustering. I used KMeans algorithm to cluster all the songs of an artist into two clusters - Relaxing and Energetic. Using Spotipy, I then automatically added the clusters back to my spotify library as seperate playlists.
<img src="images/musicds3.png?raw=true"/>

---
### Reading Captchas

[![View on GitHub](https://img.shields.io/badge/GitHub-View_on_GitHub-blue?logo=GitHub)](https://github.com/jithendrabsy/mini-projects/tree/main/reading-captcha)

This is a playground computer vision project where I experimented with Lenet using Keras to detect and read the numbers from captcha images. 
<img src="images/captcha.png?raw=true"/>

---
