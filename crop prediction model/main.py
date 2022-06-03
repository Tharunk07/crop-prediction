from flask import Flask, render_template,request
import predictor as pre
import configparser
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=["POST"])
def crop():
    if request.method=="POST":
        nitrogen=float(request.form["NITROGEN"])
        phosphorus=float(request.form["PHOSPHORUS"])
        potassium=float(request.form["POTASSIUM"])
        temperature=float(request.form["TEMPERATURE"])
        humidity=float(request.form["HUMIDITY"])
        rainfall=float(request.form["RAINFALL"])
        end=pre.crop(nitrogen,phosphorus,potassium,temperature,humidity,rainfall)
        return render_template("index.html",temp=end[0])
        
    else:
        return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)  