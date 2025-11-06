def load_df(path="india_deforestation_2011_2025_statewise.csv"):
    """Load the dataset and raise a clear error if the file is missing."""
    try:
        import pandas as pd
        return pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset file '{path}' not found. Please ensure the CSV file is in the same directory as the notebook.")
    except Exception as e:
        raise ValueError(f"Error loading dataset: {str(e)}")

def set_plotly_notebook(renderer="notebook"):
    """Configure Plotly to render inline in the notebook."""
    try:
        import plotly.io as pio
        pio.renderers.default = renderer
    except ImportError:
        print("Warning: Plotly not installed. Install it with: pip install plotly")