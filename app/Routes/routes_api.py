from flask import Blueprint, request, redirect, jsonify
import CoolProp.CoolProp as CP

api = Blueprint('api', __name__, url_prefix='/api')

@api.get('/cp/')
def cPCalc():
    incomingData = request.json
    fluid = incomingData.get('fluid')
    outputProp = incomingData.get('outputProp')
    outputUnit = incomingData.get('outputUnit')
    prop1Type = incomingData.get('prop1Type')
    prop1Data = incomingData.get('prop1Value')
    prop1Unit = incomingData.get('prop1Unit')
    prop2Type = incomingData.get('prop2Type')
    prop2Data = incomingData.get('prop2Value')
    prop2Unit = incomingData.get('prop2Unit')
    outputValue = CP.PropsSI
    outputData = {
        'fluid': fluid,
        'outputProp' : outputProp,
        'outputUnit' : outputUnit,
        'outputValue': CP.PropsSI('D','P',1e5,'Q',0,'Water')
    }

    return jsonify(outputData)

