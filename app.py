from flask import Flask, render_template, request
import joblib
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize Flask app
app = Flask(__name__)

# Load the vectorizer and model
vectorizer = joblib.load("model/count_mnd_vectorizer.pkl")
model = joblib.load("model/logistic_regression_pipeline.pkl", strict=False)

# Define the clean function
lemmatizer = WordNetLemmatizer()

def clean(doc): # doc is a string of text
    
    
    # Remove punctuation and numbers.
    doc = "".join([char for char in doc if char not in string.punctuation and not char.isdigit()])

    # Converting to lower case
    doc = doc.lower()
    
    # Tokenization
    tokens = nltk.word_tokenize(doc)

    # Lemmatize
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Stop word removal
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in lemmatized_tokens if word.lower() not in stop_words]
    
    # Join and return
    return " ".join(filtered_tokens)

# Label mapping
label_mapping = {1: "Positive", 0: "Negative"}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        cleaned_text = clean(text)  # Apply preprocessing
        transformed_text = vectorizer.transform([cleaned_text])  # Vectorize
        prediction = model.predict(transformed_text)[0]  # Predict sentiment
        output_label = label_mapping[prediction]  # Map to label
        return render_template("index.html", text=text, prediction=output_label)

    return render_template("index.html", text="", prediction="")

if __name__ == "__main__":
    app.run(debug=True)
