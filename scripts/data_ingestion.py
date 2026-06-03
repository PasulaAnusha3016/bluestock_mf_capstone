from pathlib import Path
import pandas as pd

raw_path = Path("data/raw")

for file in raw_path.glob("*.csv"):
    print("\n" + "="*60)
    print("FILE:", file.name)

    try:
        df = pd.read_csv(file)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())
        
        print("\nDuplicates:")
        print(df.duplicated().sum())
    except Exception as e:
        print(f"Error reading {file.name}: {e}")