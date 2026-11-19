# ProductIQ
# 🛍️ ProductIQ – E-commerce Product Category Prediction

ProductIQ is a machine learning-powered web application that predicts the category of an e-commerce product based on its textual description.

The system uses Natural Language Processing (NLP), TF-IDF vectorization, and a Linear Support Vector Machine (Linear SVM) classifier to automatically classify products into four categories.

🌐 **Live Demo:** https://ecommerce-category-ai.streamlit.app/

📂 **GitHub Repository:** https://github.com/saumildodiya2007-hash/ProductIQ

## 🎯 Project Objective

The objective of ProductIQ is to automate product categorization using machine learning, reducing the need for manual classification of e-commerce product listings.

Users can enter a product description and receive a predicted product category through an interactive Streamlit application.

## 📊 Dataset Overview

- **Dataset:** Zenodo E-commerce Text Dataset
- **Source:** Hugging Face
- **License:** CC BY 4.0
- **Records after duplicate removal:** 27,802
- **Target Categories:** 4

### Product Categories

- Household
- Books
- Electronics
- Clothing & Accessories

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TF-IDF Vectorization
- Linear SVM
- Streamlit
- Joblib

## 🧠 Machine Learning Workflow

1. Dataset Loading and Exploration
2. Data Cleaning and Preprocessing
3. Duplicate Description Removal
4. Exploratory Data Analysis (EDA)
5. Text Vectorization using TF-IDF
6. Train-Test Split
7. Model Training and Evaluation
8. Model Comparison and Hyperparameter Tuning
9. Model Saving using Joblib
10. Streamlit Application Development
11. Deployment using Streamlit Community Cloud

## 📈 Model Performance

The selected Linear SVM model achieved:

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 95.31% |
| Macro F1-score | 0.9525 |

## 🚀 Live Application

Try ProductIQ by entering any product description into the application.

**Live Demo:** https://ecommerce-category-ai.streamlit.app/

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/saumildodiya2007-hash/ProductIQ.git
```

Navigate into the project folder:

```bash
cd ProductIQ
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
ProductIQ/
│
├── app.py
├── productiq_model.pkl
├── requirements.txt
└── .gitignore
```

## 🔮 Future Improvements

- Improve prediction confidence and user feedback.
- Expand product categories.
- Explore additional NLP techniques.
- Improve the application's user interface.

## 👨‍💻 Author

**Saumil Dodiya**

BSc Data Science Student | Aspiring Data Analyst

---

⭐ If you find this project interesting, consider giving the repository a star!
