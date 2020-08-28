from flask import Flask,render_template,request
import pickle
import numpy as np
model=pickle.load(open('Global_active_power.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def y_pred():
    return render_template("index.html")
@app.route('/login',methods=["POST"])
def func2():
    Global_reactive_power=request.form['Global_reactive_power']
    Voltage=request.form['Voltage']
    Global_intensity=request.form['Global_intensity']
    Sub_metering_1=request.form['Sub_metering_1']
    Sub_metering_2=request.form['Sub_metering_2']
    Sub_metering_3=request.form['Sub_metering_3']
    data=[[float(Global_reactive_power),float(Voltage),float(Global_intensity),float(Sub_metering_1),float(Sub_metering_2),float(Sub_metering_3)]]
    pred=model.predict(data)
    print(pred[0])
    output = np.round(pred[0],2)
    output = str(output[0])+'KWh'
    return render_template("index.html",y="Global_active_power is {}".format(output))
if __name__=='__main__':
   app.run(debug= True)