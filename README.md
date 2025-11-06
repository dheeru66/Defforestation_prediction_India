# Deforestation Prediction India

This project analyzes and predicts deforestation trends across different states in India using time series forecasting techniques.

## Data

The project uses the following dataset:
- `india_deforestation_2011_2025_statewise.csv`: Contains historical and projected forest area data for Indian states from 2011-2025.

## Setup

1. Create a Python environment (recommend using conda):
```bash
conda create -n forest python=3.8
conda activate forest
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

Note: For Prophet installation on Windows, it's recommended to install it via conda:
```bash
conda install -c conda-forge prophet
```

## Running the Notebook

1. Start Jupyter Lab/Notebook:
```bash
jupyter lab
```

2. Open `forest_area_prediction.ipynb`
3. Run all cells in sequence

## Dependencies

Key packages used:
- pandas
- numpy 
- matplotlib
- seaborn
- scikit-learn
- plotly
- prophet
- jupyter
- nbformat

See `requirements.txt` for full list with versions.

## Features

- Time series analysis of deforestation trends
- State-wise visualization of forest cover changes
- Future predictions using Prophet and linear regression models
- Interactive Plotly visualizations

## Troubleshooting

If you encounter a "NameError: name 'df' is not defined", make sure:
1. The CSV file is in the same directory as the notebook
2. Run the data loading cell first
3. Check file permissions