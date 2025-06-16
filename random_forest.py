from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# ✅ Sample data: Area vs Price
data = {
    'Area': [1000, 1500, 2000, 2500, 3000],
    'Price': [12000, 18000, 25000, 32000, 38000]
}


# ✅ Or use the inline data
df = pd.DataFrame(data)

# Show first 5 rows
print("Data Preview:")
print(df.head())

# ✅ Define features and target
X = df[['Area']]
y = df['Price']

# ✅ Create and train the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# ✅ Take user input for area
area = float(input("Enter the area of the house in square feet: \n"))

# ✅ Predict price
predicted_price = model.predict([[area]])

print(f"Predicted price (Random Forest): Tk {predicted_price[0]:,.2f}")

