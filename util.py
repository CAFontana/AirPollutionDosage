import math

def roundToMultiple(x, base=60):
    return x - (x % base)

def Linear(AQIhigh, AQIlow, Conchigh, Conclow, Conc):
    a=((Conc-Conclow)/(Conchigh-Conclow))*(AQIhigh-AQIlow)+AQIlow
    return round(a)


def AQINO2(Conc):
    c=math.floor(Conc)/1000
    if c>=0 and c<.054:
        AQI=Linear(50,0,.053,0,c)
    elif c>=.054 and c<.101:
        AQI=Linear(100,51,.100,.054,c)
    elif c>=.101 and c<.361:
        AQI=Linear(150,101,.360,.101,c)
    elif c>=.361 and c<.650:
        AQI=Linear(200,151,.649,.361,c)
    elif c>=.650 and c<1.250:
        AQI=Linear(300,201,1.249,.650,c)
    elif c>=1.250 and c<1.650:
        AQI=Linear(400,301,1.649,1.250,c)
    elif c>=1.650 and c<=2.049:
        AQI=Linear(500,401,2.049,1.650,c)
    else:
        AQI="Out of Range"
    return AQI

