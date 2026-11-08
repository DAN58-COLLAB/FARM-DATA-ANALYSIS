import numpy as np

# Sample maize yield in 90 kg bags per plot for one illustrative season.
yields = np.array([18, 22, 15, 31, 27, 19, 24, 12, 28, 21, 17, 25])
rainfall_mm = np.array([420, 510, 380, 620, 590, 440, 530, 310, 610, 490, 400, 560])

print("MAIZE YIELD ANALYSIS (90 kg bags per plot)")
print(f"Plots: {len(yields)}")
print(f"Total yield: {yields.sum()} bags ({yields.sum() * 90:,} kg)")
print(f"Mean: {np.mean(yields):.1f} bags/plot")
print(f"Median: {np.median(yields):.1f} bags/plot")
print(f"Standard deviation: {np.std(yields):.1f}")
print(f"Best plot: {yields.max()} bags")
print(f"Worst plot: {yields.min()} bags")
print(f"75th percentile: {np.percentile(yields, 75):.1f} bags")

# Illustrative revenue using KES 2,800 per 90 kg bag.
revenue = yields * 2800
print(f"\nSample total revenue: KES {revenue.sum():,}")
print(f"Sample average revenue/plot: KES {revenue.mean():,.0f}")

correlation = np.corrcoef(rainfall_mm, yields)[0, 1]
print(f"Rainfall/yield correlation: {correlation:.2f}")
print("This is a descriptive correlation, not evidence of causation.")

mean_yield = np.mean(yields)
high_mask = yields > mean_yield
low_mask = ~high_mask
print("\nHIGHER-YIELD PLOTS")
print("Yields:", yields[high_mask])
print(f"Average rainfall: {rainfall_mm[high_mask].mean():.1f} mm")
print("\nAT-OR-BELOW-AVERAGE PLOTS")
print("Yields:", yields[low_mask])
print(f"Average rainfall: {rainfall_mm[low_mask].mean():.1f} mm")
