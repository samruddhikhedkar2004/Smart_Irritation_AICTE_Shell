# Smart Irrigation System – Machine Learning Project

This project was developed as part of the **AICTE - Edunet Foundation Internship (Cycle 2)**.  
It focuses on applying machine learning to automate decisions in an irrigation system using sensor data.

The model predicts:
- Whether to turn the **irrigation pump ON/OFF**
- Whether to **apply fertilizer**
- And one additional output (based on the third label in the dataset)

---

## 📁 Dataset

- **Total Rows:** 2000
- **Input Features (X):** 20 sensor values (e.g., `sensor_0` to `sensor_19`)
- **Output Labels (y):** 3 targets (e.g., `Pump`, `Fertilizer`, and a third label)

These inputs and outputs are used to train a multi-label classification model.

---

## ⚙️ Technologies Used

- Python
- Pandas, Matplotlib, Seaborn
- Scikit-learn:
  - Random Forest Classifier
  - MultiOutputClassifier
- Jupyter Notebook in VS Code

---

## 🚀 Model Workflow

1. Load and clean the dataset (`irrigation_machine.csv`)
2. Drop unnecessary columns (e.g., `Unnamed: 0`)
3. Normalize the input features using `MinMaxScaler`
4. Split data into training and testing sets
5. Train a **Random Forest model** inside a `MultiOutputClassifier` to handle multiple output columns
6. Evaluate model performance using `classification_report`
7. Save the trained model using `joblib`

---

## 📈 Outputs

- Model predicts 3 output labels simultaneously
- Classification report printed for each label
- (Optional) Data visualizations using Seaborn & Matplotlib

---

## 💾 Model Saving

The model is saved using `joblib` in `.pkl` format so it can be reused without retraining.

---

## 🎓 Internship Info

**Program:** AICTE Virtual Internship (Cycle 2)  
**Organization:** Edunet Foundation  
**Track:** Green Skilling – Python, ML, Deep Learning & Computer Vision  
**Duration:** 4 weeks  

---

## 👩‍💻 Author

**Samruddhi Khedkar**  
BTech – Electronics and Telecommunication  
