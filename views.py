import numpy as np
import pandas as pd
import seaborn as sns
from models import load_data
import matplotlib.pyplot as plt


def handling_missing_values(data):
    df = data
    missing_rows = df.isnull().any(axis=1)
    print()
    print(df[missing_rows])
    check = int(input("Press 1 to deal with missing values : "))
    if check == 1:
        print("\nHandling missing or none values.....\n")
        missing_cols = df.isnull().any()
        missing_cols = missing_cols[missing_cols == True]
        print("Columns containing missing values are : \n\n", missing_cols)

        # separate numerical and object type columns
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        object_cols = df.select_dtypes(include=['object']).columns

        # impute missing values using mean for numerical columns
        for col in numeric_cols:
            if col in missing_cols.index:
                df[col] = df[col].fillna(df[col].mean())

        # impute missing values using mode for object type columns
        for col in object_cols:
            if col in missing_cols.index:
                df[col] = df[col].fillna(df[col].mode()[0])

        print("\nCongratulations! \nMissing values have been imputed.\n")
    return df


def set_outliers(data):
    df = data
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    numerical_df = df[numerical_cols]
    threshold = 3
    outlier_mask = np.zeros(len(numerical_df), dtype=bool)
    outlier_cols = []
    for col in numerical_df.columns:
        # calculate the mean and standard deviation for the column
        mean = numerical_df[col].mean()
        std = numerical_df[col].std()

        z_scores = (numerical_df[col] - mean) / std
        outliers = np.abs(z_scores) > threshold
        outlier_mask = outlier_mask | outliers

        if np.any(outliers):
            outlier_cols.append(col)

    if np.any(outlier_mask):
        print("\nRows containing outliers: \n")
        print(df[outlier_mask])
        print()

        print("Capping outliers:")
        for col in outlier_cols:
            lower_bound = numerical_df[col].quantile(0.01)
            upper_bound = numerical_df[col].quantile(0.99)

            # cast lower_bound and upper_bound to the appropriate dtype
            if numerical_df[col].dtype == np.int64:
                lower_bound = int(lower_bound)
                upper_bound = int(upper_bound)

            numerical_df.loc[numerical_df[col] < lower_bound, col] = lower_bound
            numerical_df.loc[numerical_df[col] > upper_bound, col] = upper_bound
            print(f"Column '{col}' capped.")

    df[numerical_cols] = numerical_df
    return df


def speed_v_price(data):
    df = data
    melted_df = df.melt(id_vars='speed', value_vars='price', value_name='price_values')
    sns.violinplot(x='speed', y='price_values', data=melted_df,
                    palette='Set3', linewidth=1, inner='quartile')
    plt.xlabel('Speed', fontsize=14, fontweight='bold')
    plt.ylabel('Price ($)', fontsize=14, fontweight='bold')
    plt.title('Distribution of Laptop Prices by Speed', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.show()
    

def touch_v_price(data):
    df = data
    plt.hist([df[df['touch'] == 'yes']['price'], df[df['touch'] == 'no']['price']],
         bins=20, alpha=0.7, label=['Touch', 'No Touch'], color=['#1f77b4', '#ff7f0e'])
    plt.xlabel('Price ($)', fontsize=14, fontweight='bold')
    plt.ylabel('Frequency', fontsize=14, fontweight='bold')
    plt.title('Distribution of Laptop Prices by Touch Screen', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.show()


def battery_v_price(data):
    df = data
    sns.regplot(x='battery', y='price', data=df,
            scatter_kws={'alpha': 0.5, 's': 50, 'color': '#1f77b4'},
            line_kws={'color': '#ff7f0e', 'linewidth': 2})
    plt.xlabel('Battery Life (hours)', fontsize=14, fontweight='bold')
    plt.ylabel('Price ($)', fontsize=14, fontweight='bold')
    plt.title('Regression of Laptop Prices on Battery Life', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.show()


def backlit_v_price(data):
    df = data
    sns.stripplot(x='backlit', y='price', data=df, jitter=True,
              color='#1f77b4', alpha=0.7, edgecolor='black', linewidth=1) # Use a single color for all points
    plt.xlabel('Backlit Keyboard', fontsize=14, fontweight='bold')
    plt.ylabel('Price ($)', fontsize=14, fontweight='bold')
    plt.title('Strip Plot of Laptop Prices by Backlit Keyboard', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.show()


def graphic_v_price(data):
    df = data
    sns.pointplot(x='graphics', y='price', data=df,
              hue='graphics',  # Use 'hue' to map colors to different graphics types
              palette=['#1f77b4', '#ff7f0e'],  # Provide a palette for the hue
              alpha=0.7, markers=['o', 's'], markeredgecolor='black', markeredgewidth=1)
    plt.xlabel('Graphics Type', fontsize=14, fontweight='bold')
    plt.ylabel('Price ($)', fontsize=14, fontweight='bold')
    plt.title('Point Plot of Laptop Prices by Graphics Type', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.show()