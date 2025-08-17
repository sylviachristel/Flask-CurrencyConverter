from flask import Flask, render_template, request
import requests

api_key = "40f2469fa9b76a06502435085cbacf37" 

url = "http://data.fixer.io/api/latest?access_key=" + api_key  # Api request

app = Flask(__name__)

@app.route("/",methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency") # for example USD
        secondCurrency = request.form.get("secondCurrency") # for example TRY

        amount = request.form.get("amount") # 15
        response = requests.get(url) # Send get request
        app.logger.info(response) # Log response status

        infos = response.json() # Convert response to JSON

        firstValue = infos["rates"][firstCurrency] # "USD": 1.180373
        secondValue = infos["rates"][secondCurrency] # "TRY": 47.029949

        result = (secondValue/firstValue) * float(amount)

        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result # This will be sent to index.html

        return render_template("index.html",info=currencyInfo) # Send data to the template 
    else:
        return render_template("index.html") 





if __name__ == "__main__":
    app.run(debug=True)