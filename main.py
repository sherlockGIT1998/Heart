from flask import Flask, render_template, request
from utils import HeartDiesese
app = Flask(__name__)

@app.route("/") 
def hello_flask():
    print("Heart Related Dieseses")   
    return render_template("index.html")

@app.route("/predict_heat_diesese", methods = ["POST", "GET"])

def diesese_info():

    if request.method == "GET":
        print("GET Method")

        age  = eval(request.args.get('age'))
        sex = eval(request.args.get('sex'))
        cp = eval(request.args.get('cp'))
        trestbps = eval(request.args.get('trestbps'))
        chol = eval(request.args.get('chol'))
        fbs = eval(request.args.get('fbs'))
        restecg = eval(request.args.get('restecg'))
        thalach = eval(request.args.get('thalach'))
        exang  = int(request.args.get('exang'))
        oldpeak = eval(request.args.get('oldpeak'))
        slope = eval(request.args.get('slope'))
        ca = eval(request.args.get('ca'))
        thal = eval(request.args.get('thal'))

        heart_diesese = HeartDiesese(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

        yes_no = heart_diesese.get_predicted_heart_di()

        if yes_no == 1:
            yes_no = "The information you provided indiactes that YOU MAY HAVE HEART-RELATED DIESESE.."
    
        else:
            yes_no = "The information you provided indiactes that YOU MAY NOT HAVE HEART-RELATED DIESESE.."

        return render_template("index.html", prediction = yes_no)
    
if __name__ == "__main__":
    app.run()