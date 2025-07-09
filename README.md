# Life Expectancy Prediction 🚑📈

This project predicts **Life Expectancy** using multiple machine learning models, including:

- **Linear Regression**
- **LightGBM**
- **CatBoost**

It evaluates each model using **R² Score** and **RMSE**, enabling you to identify the best performing model for the dataset.

---

## 📂 Project Structure

```

life-expectancy-prediction/
│
├── data/
│   └── life\_expectancy\_data.csv
│
├── life\_expectancy\_prediction.ipynb
├── requirements.txt
└── README.md

````

---

## 🛠️ Features

✅ Data Cleaning and Imputation  
✅ Feature Scaling (StandardScaler)  
✅ Model Training (Linear Regression, LightGBM, CatBoost)  
✅ Evaluation using R² and RMSE  
✅ Visualization of Predictions vs Actual Values  
✅ Ready for deployment as an API or integration into dashboards.

---

## 📊 Results

| Model              | R² Score | RMSE |
|---------------------|----------|------|
| **Linear Regression** | ~0.955  | ~1.97 |
| **LightGBM**         | ~0.967  | ~1.68 |
| **CatBoost**         | ~0.969  | ~1.65 |

CatBoost showed the best performance, indicating strong predictive capabilities using the prepared features.

---

## 📸 Visualizations

### 1️⃣ Global Life Expectancy Comparision

![GlobalLifeExpectancy](images/GlobalLife.png)

---

### 2️⃣ Variable Correlations

![Corr](images/Corr.png)

---

### 3️⃣ Actual vs Predicted (LightGBM)

![ActualPredicted](images/Actual_Predicted.png)

---

## 💡 Next Improvements

* Add **hyperparameter tuning** using GridSearchCV.
* Deploy using **FastAPI** for API predictions.
* Add **explainability tools (SHAP)** for transparency in healthcare decisions.

---

## 📬 Contact

For questions or collaborations:

* **Name:** Basil Rehan
* **Email:** [basilsiddiqui17@gmail.com](mailto:basilsiddiqui17@gmail.com)
* **LinkedIn:** [Your LinkedIn](https://www.linkedin.com/in/brs6)

---

🩺 **Empowering data-driven healthcare decisions, one prediction at a time.**
