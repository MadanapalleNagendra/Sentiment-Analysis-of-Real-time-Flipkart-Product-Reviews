# Sentiment Analysis of Real-time Flipkart Product Reviews

## AWS EC2 Hosted Application

**Live Demo:** [Click Here](http://18.208.164.102:5000/)

---

## Objective
The objective of this project is to classify customer reviews as **positive** or **negative** and understand the pain points of customers who write negative reviews. By analyzing sentiment, we aim to gain insights into product features that contribute to customer satisfaction or dissatisfaction.

---

## Dataset
A team of Data Engineers has already scraped real-time data from the Flipkart website. The dataset consists of **8,518 reviews** for the **"YONEX MAVIS 350 Nylon Shuttle"** product. Each review includes:
- **Reviewer Name**
- **Rating**
- **Review Title**
- **Review Text**
- **Place of Review**
- **Date of Review**
- **Up Votes**
- **Down Votes**

---

## Data Preprocessing
1. **Text Cleaning**: Remove special characters, punctuation, and stopwords from the review text.
2. **Text Normalization**: Apply **lemmatization** or **stemming** to reduce words to their base forms.
3. **Numerical Feature Extraction**: Apply techniques like:
   - **Bag-of-Words (BoW)**
   - **Term Frequency-Inverse Document Frequency (TF-IDF)**
   - **Word2Vec (W2V)**
   - **BERT models**

---

## Modeling Approach
1. **Model Selection**: Train and evaluate various machine learning and deep learning models using the embedded text data.
2. **Evaluation Metric**: Use **F1-Score** to assess the model's performance in classifying sentiment.

---

## Model Deployment
1. **Flask or Streamlit App Development**: Develop a Flask or Streamlit web application that takes user input in the form of a review and generates the sentiment (positive or negative).
2. **Model Integration**: Integrate the trained sentiment classification model into the Flask or Streamlit app for real-time inference.
3. **Deployment**: Deploy the Flask or Streamlit app on an **AWS EC2 instance** to make it accessible over the internet.

---

## Workflow
1. **Data Loading and Analysis**: Gain insights into product features that contribute to customer satisfaction or dissatisfaction.
2. **Data Cleaning**: Preprocess the review text by removing noise and normalizing the text.
3. **Text Embedding**: Experiment with different text embedding techniques to represent the review text as numerical vectors.
4. **Model Training**: Train machine learning and deep learning models on the embedded text data to classify sentiment.
5. **Model Evaluation**: Evaluate the performance of the trained models using the **F1-Score metric**.
6. **Flask or Streamlit App Development**: Develop a **Flask or Streamlit web application** for sentiment analysis of user-provided reviews.
7. **Model Deployment**: Deploy the trained sentiment classification model along with the Flask or Streamlit app on an **AWS EC2 instance**.
8. **Testing and Monitoring**: Test the deployed application and monitor its performance for any issues or errors.

---

## Project Structure
```
webapp/
│── app.py               # Flask application code
│── naive_bayes.pkl      # Trained sentiment analysis model
│── requirements.txt     # List of required dependencies
│── sentiment.csv        # Dataset file (Flipkart reviews)
│── templates/
│   ├── home.html        # Frontend homepage
│   ├── output.html      # Result page after prediction
```

---

## Installation & Running Locally
### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo-url.git
cd webapp
```
### **2. Create Virtual Environment**
```bash
python3 -m venv .env
source .env/bin/activate
```
### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```
### **4. Run the Flask App**
```bash
python app.py
```
Now, the application should be running on **http://127.0.0.1:5000/**

---

## Deployment on AWS EC2
### **1. SSH into EC2 Instance**
```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```
### **2. Install Python & Virtual Environment**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv -y
```
### **3. Set Up the Flask App**
```bash
mkdir webapp && cd webapp
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
### **4. Run the Flask App in the Background**
```bash
nohup python3 app.py &
```
Your app is now running on **http://your-ec2-public-ip:5000/**

---

## Submission
Click [here](#) to submit your work.

---

## Authors
- **Your Name** - *Developer & Data Scientist*

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


