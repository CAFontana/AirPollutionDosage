import math


class Converter:
    
    @staticmethod
    def linear(aqihigh, aqilow, conchigh, conclow, conc):
        return round(((conc - conclow) / (conchigh - conclow)) * (aqihigh - aqilow) + aqilow)

    @staticmethod
    def inv_linear(aqihigh, aqilow, conchigh, conclow, a):
        return ((a - aqilow) / (aqihigh - aqilow)) * (conchigh - conclow) + conclow

    @staticmethod
    def aqi_pm25(conc):
        aqi = 0
        c = (math.floor(10 * conc)) / 10
        if 0 <= c < 12.1:
            aqi = Converter.linear(50, 0, 12, 0, c)
        elif 12.1 <= c < 35.5:
            aqi = Converter.linear(100, 51, 35.4, 12.1, c)
        elif 35.5 <= c < 55.5:
            aqi = Converter.linear(150, 101, 55.4, 35.5, c)
        elif 55.5 <= c < 150.5:
            aqi = Converter.linear(200, 151, 150.4, 55.5, c)
        elif 150.5 <= c < 250.5:
            aqi = Converter.linear(300, 201, 250.4, 150.5, c)
        elif 250.5 <= c < 350.5:
            aqi = Converter.linear(400, 301, 350.4, 250.5, c)
        elif 350.5 <= c < 500.5:
            aqi = Converter.linear(500, 401, 500.4, 350.5, c)
        return aqi
     
    @staticmethod
    def aqi_pm10(conc):
        aqi = 0
        c = math.floor(conc)
        if 0 <= c < 55:
            aqi = Converter.linear(50, 0, 54, 0, c)
        elif 55 <= c < 155:
            aqi = Converter.linear(100, 51, 154, 55, c)
        elif 155 <= c < 255:
            aqi = Converter.linear(150, 101, 254, 155, c)
        elif 255 <= c < 355:
            aqi = Converter.linear(200, 151, 354, 255, c)
        elif 355 <= c < 425:
            aqi = Converter.linear(300, 201, 424, 355, c)
        elif 425 <= c < 505:
            aqi = Converter.linear(400, 301, 504, 425, c)               
        elif 505 <= c < 605:
            aqi = Converter.linear(500, 401, 604, 505, c)
        return aqi
                                 
    @staticmethod
    def aqi_co(conc):
        aqi = 0
        c = (math.floor(10 * conc)) / 10
        if 0 <= c < 4.5:
            aqi = Converter.linear(50, 0, 4.4, 0, c)
        elif 4.5 <= c < 9.5:
            aqi = Converter.linear(100, 51, 9.4, 4.5, c)
        elif 9.5 <= c < 12.5:
            aqi = Converter.linear(150, 101, 12.4, 9.5, c)
        elif 12.5 <= c < 15.5:
            aqi = Converter.linear(200, 151, 15.4, 12.5, c)
        elif 15.5 <= c < 30.5:
            aqi = Converter.linear(300, 201, 30.4, 15.5, c)
        elif 30.5 <= c < 40.5:
            aqi = Converter.linear(400, 301, 40.4, 30.5, c)
        elif 40.5 <= c < 50.5:
            aqi = Converter.linear(500, 401, 50.4, 40.5, c)
        return aqi
                                                             
    @staticmethod
    def aqi_so2_1hr(conc):
        aqi = 0
        c = math.floor(conc)
        if 0 <= c < 36:
            aqi = Converter.linear(50, 0, 35, 0, c)
        elif 36 <= c < 76:
            aqi = Converter.linear(100, 51, 75, 36, c)
        elif 76 <= c < 186:
            aqi = Converter.linear(150, 101, 185, 76, c)
        elif 186 <= c <= 304:
            aqi = Converter.linear(200, 151, 304, 186, c)
        elif 304 <= c <= 604:
            aqi = Converter.linear(500, 201, 604, 305, c)
        return aqi
                                                                                 
    @staticmethod
    def aqi_so2_24hr(conc):
        aqi = 0
        c = math.floor(conc)
        if 0 <= c <= 304:
            aqi = Converter.linear(200, 0, 304, 0, c)
        elif 304 <= c < 605:
            aqi = Converter.linear(300, 201, 604, 305, c)
        elif 605 <= c < 805:
            aqi = Converter.linear(400, 301, 804, 605, c)
        elif 805 <= c <= 1004:
            aqi = Converter.linear(500, 401, 1004, 805, c)
        return aqi
                                                                                                 
    @staticmethod
    def aqi_ozone_8hr(conc):
        aqi = 0
        c = (math.floor(conc)) / 1000
        if 0 <= c < .055:
            aqi = Converter.linear(50, 0, 0.054, 0, c)
        elif .055 <= c < .071:
            aqi = Converter.linear(100, 51, .070, .055, c)
        elif .071 <= c < .086:
            aqi = Converter.linear(150, 101, .085, .071, c)
        elif .086 <= c < .106:
            aqi = Converter.linear(200, 151, .105, .086, c)
        elif .106 <= c < .201:
            aqi = Converter.linear(300, 201, .200, .106, c)
        elif .201 <= c < .605:
            aqi = Converter.linear(500, 301, .605, .201, c)
        return aqi

    @staticmethod
    def aqi_ozone_1hr(conc):
        aqi = 0
        c = (math.floor(conc)) / 1000
        if 0 <= c <= .124:
            aqi = Converter.linear(100, 0, .124, 0, c)
        elif .125 <= c < .165:
            aqi = Converter.linear(150, 101, .164, .125, c)
        elif .165 <= c < .205:
            aqi = Converter.linear(200, 151, .204, .165, c)
        elif .205 <= c < .405:
            aqi = Converter.linear(300, 201, .404, .205, c)
        elif .405 <= c < .505:
            aqi = Converter.linear(400, 301, .504, .405, c)
        elif .505 <= c < .605:
            aqi = Converter.linear(500, 401, .604, .505, c)
        return aqi                                                                     

    @staticmethod
    def aqi_no2(conc):
        aqi = 0
        c = math.floor(conc) / 1000
        if 0 <= c < .054:
            aqi = Converter.linear(50, 0, .053, 0, c)
        elif .054 <= c < .101:
            aqi = Converter.linear(100, 51, .100, .054, c)
        elif .101 <= c < .361:
            aqi = Converter.linear(150, 101, .360, .101, c)
        elif .361 <= c < .650:
            aqi = Converter.linear(200, 151, .649, .361, c)
        elif .650 <= c < 1.250:
            aqi = Converter.linear(300, 201, 1.249, .650, c)
        elif 1.250 <= c < 1.650:
            aqi = Converter.linear(400, 301, 1.649, 1.250, c)
        elif 1.650 <= c <= 2.049:
            aqi = Converter.linear(500, 401, 2.049, 1.650, c)
        return aqi

    @staticmethod
    def conc_pm25(a):
        conc = 0
        if a >= 0 < a <= 50:
            conc = Converter.inv_linear(50, 0, 12, 0, a)
        elif 50 < a <= 100:
            conc = Converter.inv_linear(100, 51, 35.4, 12.1, a)
        elif 100 < a <= 150:
            conc = Converter.inv_linear(150, 101, 55.4, 35.5, a)
        elif 150 < a <= 200:
            conc = Converter.inv_linear(200, 151, 150.4, 55.5, a)
        elif 200 < a <= 300:
            conc = Converter.inv_linear(300, 201, 250.4, 150.5, a)
        elif 300 < a <= 400:
            conc = Converter.inv_linear(400, 301, 350.4, 250.5, a)
        elif 400 < a <= 500:
            conc = Converter.inv_linear(500, 401, 500.4, 350.5, a)
        return conc

    @staticmethod
    def conc_pm10(a):
        conc = 0
        if a >= 0 < a <= 50:
            conc = Converter.inv_linear(50, 0, 54, 0, a)
        elif 50 < a <= 100:
            conc = Converter.inv_linear(100, 51, 154, 55, a)
        elif 100 < a <= 150:
            conc = Converter.inv_linear(150, 101, 254, 155, a)
        elif 150 < a <= 200:
            conc = Converter.inv_linear(200, 151, 354, 255, a)
        elif 200 < a <= 300:
            conc = Converter.inv_linear(300, 201, 424, 355, a)
        elif 300 < a <= 400:
            conc = Converter.inv_linear(400, 301, 504, 425, a)
        elif 400 < a <= 500:
            conc = Converter.inv_linear(500, 401, 604, 505, a)
        return conc
    
    @staticmethod
    def conc_co(a):
        conc = 0
        if 0 < a <= 50:
            conc = Converter.inv_linear(50, 0, 4.4, 0, a)
        elif 50 < a <= 100:
            conc = Converter.inv_linear(100, 51, 9.4, 4.5, a)
        elif 100 < a <= 150:
            conc = Converter.inv_linear(150, 101, 12.4, 9.5, a)
        elif 150 < a <= 200:
            conc = Converter.inv_linear(200, 151, 15.4, 12.5, a)
        elif 200 < a <= 300:
            conc = Converter.inv_linear(300, 201, 30.4, 15.5, a)
        elif 300 < a <= 400:
            conc = Converter.inv_linear(400, 301, 40.4, 30.5, a)
        elif 400 < a <= 500:
            conc = Converter.inv_linear(500, 401, 50.4, 40.5, a)
        return conc

    @staticmethod
    def conc_so2_1hr(a):
        conc = 0
        if 0 < a <= 50:
            conc = Converter.inv_linear(50, 0, 35, 0, a)
        elif 50 < a <= 100:
            conc = Converter.inv_linear(100, 51, 75, 36, a)
        elif 100 < a <= 150:
            conc = Converter.inv_linear(150, 101, 185, 76, a)
        elif 150 < a <= 200:
            conc = Converter.inv_linear(200, 151, 304, 186, a)
        return conc

    @staticmethod
    def conc_so2_24hr(a):
        conc = 0
        if 201 < a <= 300:
            conc = Converter.inv_linear(300, 201, 604, 305, a)
        elif 300 < a <= 400:
            conc = Converter.inv_linear(400, 301, 804, 605, a)
        elif 400 < a <= 500:
            conc = Converter.inv_linear(500, 401, 1004, 805, a)
        return conc

    @staticmethod
    def conc_ozone_8hr(a):
        conc = 0
        if 0 < a <= 50:
            conc = Converter.inv_linear(50, 0, 54, 0, a)
        elif 50 < a <= 100:
            conc = Converter.inv_linear(100, 51, 70, 55, a)
        elif 100 < a <= 150:
            conc = Converter.inv_linear(150, 101, 85, 71, a)
        elif 150 < a <= 200:
            conc = Converter.inv_linear(200, 151, 105, 86, a)
        elif 200 < a <= 300:
            conc = Converter.inv_linear(300, 201, 200, 106, a)
        return conc

    @staticmethod
    def conc_ozone_1hr(a):
        conc = 0
        if a > 100 < a <= 150:
            conc = Converter.inv_linear(150, 101, 164, 125, a)
        elif 150 < a <= 200:
            conc = Converter.inv_linear(200, 151, 204, 165, a)
        elif 200 < a <= 300:
            conc = Converter.inv_linear(300, 201, 404, 205, a)
        elif 300 < a <= 400:
            conc = Converter.inv_linear(400, 301, 504, 405, a)
        elif 400 < a <= 500:
            conc = Converter.inv_linear(500, 401, 604, 505, a)
        return conc

    @staticmethod
    def conc_no2(a):
        conc = 0
        if 0 < a <= 50:
            conc = Converter.inv_linear(50, 0, 53, 0, a)
        elif 50 < a <= 100:
            conc = Converter.inv_linear(100, 51, 100, 54, a)
        elif 100 < a <= 150:
            conc = Converter.inv_linear(150, 101, 360, 101, a)
        elif 150 < a <= 200:
            conc = Converter.inv_linear(200, 151, 649, 361, a)
        elif 200 < a <= 300:
            conc = Converter.inv_linear(300, 201, 1244, 650, a)
        elif 300 < a <= 400:
            conc = Converter.inv_linear(400, 301, 1644, 1245, a)
        elif 400 < a <= 500:
            conc = Converter.inv_linear(500, 401, 2044, 1645, a)
        return conc
