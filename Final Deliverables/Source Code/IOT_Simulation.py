import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "Organization ID"
deviceType = "Device Type"
deviceId = "Device ID"
authMethod = "token"
authToken = "Your Authentication Token"
# Initialize GPIO
M_status="OFF"
def myCommandCallback(cmd):
    
    print("Command received: %s" % cmd.data['Motor_Control'])
    status=cmd.data['Motor_Control']
    global M_status
    if status=='Motor_ON':  
        M_status="ON"
        print("Motor is ON")
    else :
        M_status="OFF"
        print("Motor is OFF")
    #print(cmd)
try:
    deviceOptions = {"org" : organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
    deviceCli=ibmiotf.device.Client(deviceOptions)
except Exception as e:
        print("Caught exception connecting device: %s" % str (e))
        sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11
        temp = random.randint(0, 100)
        Humid=random.randint(0,100)
        S_Mois=random.randint(0,100)

        data = {'Temperature' : temp, 'Humidity': Humid ,'Soil_Moisture' : S_Mois,'Motor_Pump_Status' : M_status }
        #print data
        def myOnPublishCallback():
            print("Published Temperature = %s C"  % temp, "Humidity= %s %%" % Humid, "Soil_Moisture= %s %%" % S_Mois, "Motor_Pump_Status = %s " %M_status, "to IBM Watson")
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        deviceCli.commandCallback = myCommandCallback
# Disconnect the device and application from the cloud
deviceCli.disconnect()
