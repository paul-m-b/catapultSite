from flask import Flask
from flask import Flask, render_template
from flask import Flask, request, redirect
import RPi.GPIO as GPIO
import math 
import time
app = Flask(__name__)

#setup GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50) 

pwm.start(0)

def calibrateMotor():
    duties = [12, 12.5, 12, 12.5, 12.5] 
    for x in range(len(duties)):
        pwm.ChangeDutyCycle(duties[x])
        time.sleep(0.3)
        pwm.ChangeDutyCycle(0)
        time.sleep(0.3)

def launchProjectile(angle:int):
    angle = 90-angle
    angle = 180-angle
    duty = angle / 18 + 2.9
    pwm.ChangeDutyCycle(float(duty))
    time.sleep(0.2)
    pwm.ChangeDutyCycle(0)
    

def calculateRange(angle:float):
    angleRelease = math.radians(angle)

    angleOfArm = 90-angle
    angleOfArm = math.radians(angleOfArm)

    sinTheta_release = math.sin(angleRelease)
    cosTheta_release = math.cos(angleRelease)

    sinTheta_arm = math.sin(angleOfArm)
    cosTheta_arm = math.cos(angleOfArm)

    yi = 0.12*sinTheta_arm #height = arm*sin(theta)
    xi = 0.12*cosTheta_arm #xinitial = arm*sin(theta)

    vix = 0.7*cosTheta_release
    viy = 0.7*sinTheta_release

    #quadratic formula
    a, b, c = -4.905, viy, yi
    d=(b**2)-(4*a*c)
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)

    if sol1 > 0:
        t = sol1
    else:
        t = sol2

    x = vix*t
    x = x-xi
    return x

@app.route("/")
def run():
    return render_template("index.html") 

@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    angle = request.form["angle"]
    calc_range = calculateRange(int(angle))

    return render_template("returnRange.html",range_=calc_range) 

@app.route("/calibrate", methods=["POST", "GET"])
def calibrate():
    calibrateMotor()
    return render_template("calibration.html")

@app.route("/launch", methods=["POST", "GET"])
def launch():
    angle = request.form["angle"]
    calc_range = calculateRange(float(angle))
    launchProjectile(float(angle))
    #add in return statement
    return render_template("launched.html", range_=calc_range)

if __name__ == "__main__":
    app.run()

