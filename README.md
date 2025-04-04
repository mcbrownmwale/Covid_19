# COVID-19 Trends Analysis (Jan-July 2020)

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-1.0+-blue.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0+-blue.svg)

## Project Overview

This data analysis project examines COVID-19 trends during the initial six months of the pandemic (January-July 2020), answering key questions about the virus's spread and impact across different countries.

## Key Questions Answered

1. Which countries had the highest number of COVID-19 deaths?
2. Which countries had the highest positivity rates (positive cases vs tests conducted)?
3. Which countries conducted the most tests relative to their population?
4. Which countries were most/least affected relative to population size?

## Dataset

- Source: [Kaggle](https://www.kaggle.com/)
- Timeframe: January 2020 - July 2020
- Records: 10,903 initial entries (filtered to 3,781 country-level records)
- Variables: 14 columns including cases, deaths, tests, and recovery metrics

## Methodology

1. **Data Preparation**:
   - Filtered to country-level data
   - Cleaned column names and standardized formats
   - Split into cumulative and daily metrics datasets

2. **Analysis Techniques**:
   - Aggregation and pivot tables
   - Population-adjusted metrics
   - Ranking system for comparative impact assessment
   - Data visualization with Matplotlib/Seaborn

## Key Findings

### Deaths Analysis
- **United States**: 98,536 cumulative deaths (highest)
- **Italy**: 33,415 deaths
- **United Kingdom**: 33,186 deaths

### Testing & Positivity Rates
- **Highest testing volume**: United States (17.2M tests), Russia (10.5M), Italy (4M)
- **Highest positivity rates**: 
  - United Kingdom (11.3%)
  - United States (10.9%)
  - Turkey (8.1%)

### Population-Adjusted Impact
- **Most tests per capita**: Russia (7.2%), Italy (6.8%), United States (5.2%)
- **Most affected country**: Italy
- **Least affected country**: India

## Repository Structure

```
.
└── Covid_19
    ├── .gitignore
    ├── ancillary_func.py
    ├── covid_19.csv
    ├── covid_19.py
    ├── Covid-19.ipynb
    ├── LICENSE
    └── README.md
```
## Technologies Used

- Python 3
- Pandas (Data manipulation)
- NumPy (Numerical operations)
- Matplotlib/Seaborn (Visualization)
- Jupyter Notebooks (Interactive analysis)