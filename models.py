import pandas as pd


def load_data():
    try:
        comp_df = pd.read_csv('synthetic_data_with_hidden_patterns.csv')
        return comp_df
    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.ParserError:
        print("Error: Could not parse file.")
    except Exception as e:
        print(f"Error: {str(e)}")

