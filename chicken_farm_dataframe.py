import pandas as pd

data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "eggs": [312, 298, 320, 305, 290, 315, 308],
    "feed_kg": [18.5, 18.0, 19.2, 18.8, 17.5, 18.6, 19.0],
    "deaths": [0, 1, 0, 0, 2, 0, 0],
    "pen": ["A", "A", "A", "B", "B", "B", "A"],
}

df = pd.DataFrame(data)
df["revenue_kes"] = df["eggs"] * 18  # Illustrative price per egg.

print("WEEKLY EGG PRODUCTION")
print(df.to_string(index=False))
print("\nShape:", df.shape)
print("\nSummary statistics:")
print(df[["eggs", "feed_kg", "deaths"]].describe().round(1))
print(f"\nTotal eggs: {df['eggs'].sum()}")
print(f"Average eggs/day: {df['eggs'].mean():.1f}")
print(f"Lowest production: {df.loc[df['eggs'].idxmin(), 'day']} ({df['eggs'].min()} eggs)")
print(f"Highest production: {df.loc[df['eggs'].idxmax(), 'day']} ({df['eggs'].max()} eggs)")
print(f"Illustrative weekly revenue: KES {df['revenue_kes'].sum():,}")
