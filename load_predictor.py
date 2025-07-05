import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Step 1: Load the data
df = pd.read_csv('smart_grid_data.csv')

# Step 2: Define features and target
X = df[['Voltage', 'Current', 'Frequency']]
y = df['Load']

# Step 3: Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make predictions
predictions = model.predict(X_test)

# Step 6: Compare results
plt.figure(figsize=(10,5))
plt.plot(y_test.values, label='Actual Load', marker='o')
plt.plot(predictions, label='Predicted Load', marker='x')
plt.title('Actual vs Predicted Load')
plt.xlabel('Sample Index')
plt.ylabel('Load (kW)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 7: Evaluate
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.4f}")
