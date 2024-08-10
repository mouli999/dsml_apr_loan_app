import pickle
import flask

from flask import Flask
app=Flask(__name__)          #class instantiator

#loading the model
model_pickle=open("./classifier.pkl","rb")
clf=pickle.load(model_pickle)

@app.route("/ping",methods=['GET'])
def ping():
    return "Pinging the model successful"



@app.route("/predict",methods=["POST"])
def prediction():

    loan_req=request.get_json()
    if loan_req["Gender"]=="Male":
        gender=0
    else:
        gender=1
    if loan_req["Married"]=="Unmarried":
        marital_status=0
    else:
        marital_status=1
    
    if loan_req["Credit_History"]=="Uncleared Debts":
        credit_history=0
    else:
        credit_history=1
    
    applicant_income=loan_req["ApplicationIncome"]
    loan_amt=loan_req["LoanAmount"]/1000

    input_data=[[gender,marital_status,credit_history,applicant_income,loan_amt]]

    ## compute inference
    predition=clf.predict(input_data)

    if prediction==0:
        pred="Rejected"
    else:
        pred="Approved"

    return {"loan_approval_status":pred}

@app.route("/get_params",methods=["GET"])
def get_application_params():

    parameters={
        "Gender":"<Male/Female",
        "Married":"<Married/Unmarried>",
        "ApplicantIncome":500000,
        "LoanAmount":50000,
        "Credit_History":"<Cleared Debts/ Uncleared Debts>"
    }
    return parameters


    
