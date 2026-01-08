# HAHE Analysis

A data analysis project examining higher education performance and quality indicators published by the Hellenic Authority for Higher Education (HAHE).

This repository includes datasets, Python code to collect the data, and exploratory analysis used to extract insights about Greek higher education institutions, across multiple academic years (2021–2024). The analysis was designed to provide transparency and support data-driven discussion on institutional performance, trends, and policy considerations.

- Article: [Taking a Look into the Greek Higher Education System](https://florjandhima.substack.com/p/taking-a-look-into-the-greek-higher?r=2we65b)  
- Kaggle Dataset: https://www.kaggle.com/datasets/floriandima/hahe-statistics-all-programmes  
- Kaggle Notebook: https://www.kaggle.com/code/floriandima/hahe-analytics-all-programs

---

## Overview

This project aims to:

- Collect and prepare publicly available HAHE data on Greek higher education programmes and institutions.  
- Perform exploratory data analysis on quality and performance indicators.  
- Highlight patterns, trends, and potential areas for further research or policy insight.  
- Publish findings in an accompanying article explaining methodology and results in a clear, reproducible format.

---

## Repository Contents

| Folder / File | Description |
|---------------|-------------|
| `datasets/` | Raw and processed HAHE dataset for each academic year |
| `hahe_all_21_24.csv` | Final HAHE dataset (all academic years) |
| `charts/` | Visualizations created during analysis |
| `hahe-analytics.ipynb` | Core Jupyter Notebook with analysis steps |
| `requirements.txt` | Python dependencies used in the collecting and analysis of the data |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/fdhima/hahe-analysis.git
cd hahe-analysis
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the analysis
Open and run hahe-analytics.ipynb in Jupyter Notebook or Jupyter Lab or in [Kaggle](https://www.kaggle.com/code/floriandima/hahe-analytics-all-programs). This notebook walks through data loading, cleaning, visualization, and summary results.

---

## Methodology

The analysis follows these general steps:

1. Data collection: Collect, load and inspect the HAHE data.
2. Cleaning & preprocessing: Standardize variable formats, handle missing values, translate Greek titles in English.
3. Exploratory analysis: Generate key descriptive statistics and visualizations to understand institutional performance differences and trajectories.
4. Visualization: Use charts to illustrate insights clearly.

## Contributions
Contributions are welcome! You can:

- Suggest improvements via Issues
- Add additional visualizations
- Enhance the data cleaning pipeline
- Expand the analysis to include more years or new indicators

## License
This project is licensed under the terms described in the LICENSE.md file in the project root.