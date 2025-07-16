Sure! Here's your `README.md` content **formatted exactly for GitHub** (Markdown syntax), ready to copy and paste into your repository:

---

```markdown
# ✈️ WWII Aircraft Failure Prediction

This is a machine learning-powered web app built with **Streamlit** to predict the **failure (loss)** of aircraft in WWII missions based on mission features.

---

## 📁 Project Structure

```

Final project/
├── app.py                  # Streamlit web application
├── train\_model.py          # Python script to train and save the model
├── cleaned\_dataset.csv     # Cleaned dataset used for training
├── ww2\_model.pkl           # Trained RandomForest model
├── model\_features.pkl      # Feature names used for model input
├── README.md               # Project documentation

````

---

## 🚀 Getting Started

### 🔧 Requirements

Install all required Python libraries:

```bash
pip install pandas scikit-learn streamlit joblib
````

OR, create a `requirements.txt` file and run:

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Training

Run the following script to train the model:

```bash
python train_model.py
```

This will:

* Train a `RandomForestClassifier`
* Save the model to `ww2_model.pkl`
* Save the feature list to `model_features.pkl`

---

## 🌐 Launch the Web App

To run the app locally:

```bash
streamlit run app.py
```

By default, it will open at: [http://localhost:8501](http://localhost:8501)

---

## 🧾 Features

* Predict aircraft failure using mission-level data
* Clean, interactive user interface via Streamlit
* Model is trained on key features including aircraft type, number lost/damaged, location, etc.

---

## ⚠️ Notes

* Make sure the following files are present:

  * `ww2_model.pkl`
  * `model_features.pkl`
* The app will throw errors if either of these files is missing
* The target variable (`Target`) is generated from the `Aircraft Lost` column (`1` if aircraft lost > 0, else `0`)

---

## 🧑‍💻 Author

**Omprakash & Poorvasha**
Mini Project – WWII Aircraft Failure Predictor

---

## 📃 License

This project is for academic use only.

