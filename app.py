
import streamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="ProductIQ",
    page_icon="🛍️",
    layout="centered"
)

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("productiq_model.pkl")

model = load_model()

# Sidebar
st.sidebar.title("About ProductIQ")
st.sidebar.write(
    "ProductIQ is an ML-powered system "
    "that predicts e-commerce product categories "
    "using product descriptions."
)

st.sidebar.markdown("---")
st.sidebar.write("**Machine Learning Model:** Linear SVM")
st.sidebar.write("**NLP Technique:** TF-IDF")
st.sidebar.write("**Categories:** 4")

# Main page
st.title("🛍️ ProductIQ")
st.subheader("E-commerce Product Category Prediction")

st.write(
    "Enter a product description and let "
    "machine learning identify its category."
)

st.divider()

# Input section
st.markdown("### Product Description")

product_description = st.text_area(
    "Describe your product:",
    placeholder="Example: Samsung 253L double door refrigerator...",
    height=150
)

# Prediction
if st.button("Predict Category", use_container_width=True):

    if product_description.strip():

        prediction = model.predict([product_description])[0]

        st.divider()
        st.markdown("### Prediction Result")

        st.success(f"Predicted Category: {prediction}")

    else:
        st.warning("Please enter a product description.")

st.divider()

st.caption("ProductIQ | Machine Learning Project")
