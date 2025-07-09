import pandas as pd
from sklearn.linear_model import LinearRegression
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"C:\Users\basil\OneDrive\Desktop\Base\Work\Personal projects\lifeexpectancy\Life Expectancy Data.csv")
df.rename(columns={'Life expectancy ': 'Life expectancy'}, inplace=True)

# Drop rows where target is NaN
df = df.dropna(subset=['Life expectancy'])

# EDA: Developed vs Developing trends
mean_life_expectancy_dev = df[df.Status == "Developed"].groupby("Year")["Life expectancy"].mean()
sns.lineplot(data=mean_life_expectancy_dev)
plt.title("Mean Life Expectancy - Developed Countries")
plt.show()

mean_life_expectancy_dev = df[df.Status == "Developing"].groupby("Year")["Life expectancy"].mean()
sns.lineplot(data=mean_life_expectancy_dev)
plt.title("Mean Life Expectancy - Developing Countries")
plt.show()

# Correlation heatmap
plt.figure(figsize=(16, 12))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Correlation Heatmap of Numerical Features")
plt.show()

# Prepare X and y
X = df.drop(['Life expectancy'], axis=1)
y = df['Life expectancy']

# One-hot encode categorical features
X = pd.get_dummies(X, drop_first=True)

# Impute missing values
imputer = SimpleImputer(strategy='mean')
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)
print("Linear Regression R2:", r2_score(y_test, y_pred_lr))
print("Linear Regression RMSE:", mean_squared_error(y_test, y_pred_lr, squared=False))

# LightGBM
lgbm = LGBMRegressor(random_state=42)
lgbm.fit(X_train, y_train)
y_pred_lgbm = lgbm.predict(X_test)
print("LightGBM R2:", r2_score(y_test, y_pred_lgbm))
print("LightGBM RMSE:", mean_squared_error(y_test, y_pred_lgbm, squared=False))

# CatBoost
catboost = CatBoostRegressor(verbose=0, random_state=42)
catboost.fit(X_train, y_train)
y_pred_catboost = catboost.predict(X_test)
print("CatBoost R2:", r2_score(y_test, y_pred_catboost))
print("CatBoost RMSE:", mean_squared_error(y_test, y_pred_catboost, squared=False))

# Plot actual vs predicted for best model
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred_lgbm, alpha=0.6, color='royalblue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Life Expectancy')
plt.ylabel('Predicted Life Expectancy')
plt.title('Actual vs Predicted Life Expectancy (LightGBM)')
plt.show()