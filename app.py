# importing the necessary dependencies
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

# initialize flask app
app = Flask(__name__)


# route to get to the home page
@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            # read the inputs given by the user
            gre_score = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            if is_research == 'yes':
                research = 1
            else:
                research = 0
            # load model
            #filename = "admission_lr_mode.sav.pickle"
            filename = "finalized_model.pickle"
            loaded_model = pickle.load(open(filename, "rb"))

            # prediction using loaded model

            prediction = loaded_model.predict([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])

            print("Prediction is ", prediction)

            # showing the predictions in UI
            return render_template('results.html', prediction=round(100 * prediction[0]))

        except Exception as e:
            print("The exception message is : ", e)
            return "something is wrong"

    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app
