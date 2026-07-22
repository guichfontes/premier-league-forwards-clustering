# Premier League Forwards Clustering

Clustering analysis of Premier League 2025/26 forwards based on per-90-minute
performance stats, using unsupervised machine learning (KMeans).

## Overview

This project collects player statistics from Sofascore and applies KMeans
clustering to group forwards into distinct playing style profiles (e.g.
poachers, creators, physical forwards), based on offensive, creative and
physical metrics.

## Project Structure

- `data_collection.py` — scrapes forward statistics from Sofascore and
  exports them to an Excel file.
- `forwards_clustering_analysis.ipynb` — data cleaning, feature selection,
  standardization, KMeans clustering, and cluster profiling/visualization.

## Tech Stack

- Python
- pandas, NumPy
- scikit-learn (KMeans, StandardScaler, PCA)
- seaborn, matplotlib, plotly
- ScraperFC (data collection from Sofascore)

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the data collection script:
   ```bash
   python data_collection.py

3. Open forwards_clustering_analysis.ipynb and run the cells to reproduce the analysis.

## License
This project is licensed under GNU General Public License v3.0 (GPL-3.0).
