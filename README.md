# Farm Data Analysis

A collection of beginner-friendly Python exercises that use pandas and NumPy to explore sample poultry, maize and livestock records.

## Included projects
- `chicken_farm_dataframe.py` — summarizes weekly egg production, feed use, mortality and sample revenue with pandas.
- `numpy_farm_data_maize_yield.py` — calculates maize-yield statistics, sample revenue and rainfall/yield correlation with NumPy.
- `goat_weight_tracker.py` — applies simple illustrative breed weight thresholds and lists animals below those thresholds.

## Requirements
Python 3.9+, pandas and NumPy.

## Run

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python chicken_farm_dataframe.py
python numpy_farm_data_maize_yield.py
python goat_weight_tracker.py
```

## Notes
All records, prices and thresholds in these scripts are sample data for programming practice. They are not verified farm records, market quotations or veterinary/agricultural recommendations. The rainfall correlation is descriptive and does not establish causation.
