# <b> ClusterFraud </b>     
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)  
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/concealedtea/)

## Features
<b>Includes :</b>   
  
- Prevent Fraudulent Click Rates in App with K-Means clustering, implemented in Python 
- Reads in data in csv format, clusters using k-means clustering algorithm  
- Implemented without use of kmeans library   
- Uses Google's [FTRL](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41159.pdf) stepping algorithm to better determine cluster amount for AdClick Prediction   

## How to Run  
Edit this line to your own local/server address where your data is located.   
```
fileInput = r"\Users\thatq\Desktop\ML\Work\test"
```  
Navigate to file location on your local drive, run with 
```
python testClustering.py
```
