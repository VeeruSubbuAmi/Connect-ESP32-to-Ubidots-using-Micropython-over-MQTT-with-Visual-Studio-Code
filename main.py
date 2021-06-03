from umqtt.robust import MQTTClient

import machine as m

ubidotsToken = "BBFF-0kXKM5Xt4hg2I6cALmQt2WxLvBuQWL"

clientID = "myclient1"

client = MQTTClient("clientID", "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken)

def checkwifi():

    while not sta_if.isconnected():

        time.sleep_ms(500)

        print(".")

        sta_if.connect()

pin13 = m.Pin(13, m.Pin.IN, m.Pin.PULL_UP)

def publish():

    while True:

        checkwifi()

        client.connect()

        lat = 6.2

        lng = -75.56

        #var = repr(pin13.value())

        var = 2

        msg = b'{"location": {"value":%s, "context":{"lat":%s, "lng":%s}}, "pressure": {"value": 78, "context":{"name" : "John"}}, "temperature": {"value": 27, "timestamp": 1514808000000}}' % (var, lat, lng)

        temperature = 27

        humidity = 55

        pressure = 78

        #msg = b'{"temperature": {"value":%s, "timestamp": 1514808000000}, "humidity":%s, {"pressure": {"value":%s, "context":{"lat":%s, "lng":%s}}}}' % (temperature, humidity, pressure, lat, lng)
        
        #{"temperature": {"value": 27, "timestamp": 1514808000000}, "humidity": 55, "pressure": {"value": 78, "context":{"name" : "John"}}}

        print(msg)

        client.publish(b"/v1.6/devices/ESP32", msg)

        time.sleep(20)

publish()