#import libraries
import numpy as np
from flask import Flask, render_template,request,jsonify
import pickle#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('finalized_model.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')


#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    print(request.form.values())
    int_features = [int(x) for x in request.form.values()]
    X = [np.array(int_features)]
    print(X)
    prediction = model.predict(X)
    output = prediction[0]
    print(output)
    #return "output"+str(output)
    return render_template('index.html', prediction_text='CO2    Emission of the vehicle is :{0}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)