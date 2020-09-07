import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

import re
def text_tokenizer(text):
  if not (text == "" or pd.isnull(text)): 
    text = re.sub(r'URL_[A-Za-z0-9]+', ' ', text)
    return re.sub(r'[^A-Za-z0-9]+', ' ', text).lower().strip()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['GET', 'POST'])
def predict():

    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)

    #output = round(prediction[0], 2)

    features = request.form['job_title'] + ' ' + request.form['location'] + ' ' + request.form['department'] + ' ' + request.form['company_profile'] + ' ' + request.form['description'] + ' ' + request.form['requirements']
    features = features +  request.form['benefits'] + ' ' + request.form['employment_type'] + ' ' + request.form['required_experience']+ ' ' + request.form['required_education'] + ' ' + request.form['industry'] + ' ' + request.form['function']
    #inp = vectorizer.transform([text_tokenizer("hello there")])
    #output = round(prediction[0], 2)

    #return render_template('index.html', prediction_text=model.predict(inp))
    return render_template('index.html', prediction_text=features)


if __name__ == "__main__":
	app.run(debug=True)