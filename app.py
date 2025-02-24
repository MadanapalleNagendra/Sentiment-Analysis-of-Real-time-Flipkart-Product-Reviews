import streamlit as st
import joblib
import os

# Set page configuration
st.set_page_config(page_title="Sentiment Analysis", page_icon="📊", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stTextArea textarea { font-size: 18px; }
    .stButton button { background-color: #4CAF50; color: white; font-size: 18px; padding: 10px 20px; }
    .stTitle { color: #0078D7; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Load Model with error handling
model_path =r"sentiment_model.pkl" # Relative path for cloud compatibility

if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("🔴 Error: Model file not found! Please train and save 'sentiment_model.pkl' before running the app.")
    st.stop()  # Stop execution if model is missing

# UI Design
st.title("📊 Flipkart Product Reviews Sentiment Analysis")
st.subheader("🔍 Enter a review to predict sentiment")

# Input Text Box
review_text = st.text_area("📝 Write a Review Below:", height=150)

# Predict Sentiment Button
if st.button("🔍 Predict Sentiment"):
    if review_text.strip():
        prediction = model.predict([review_text])[0]
        sentiment_label = "😊 Positive" if prediction == 1 else "😞 Negative"

        # Display Result
        st.success(f"🎯 **Predicted Sentiment:** {sentiment_label}")

        # Display feedback message
        st.info("✅ If the prediction is correct, great! Otherwise, consider retraining the model.")
    else:
        st.warning("⚠️ Please enter a review before clicking 'Predict Sentiment'.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;'>📌 Developed by <b>Nagendra</b> | MLOps & Data Science</p>", unsafe_allow_html=True)
