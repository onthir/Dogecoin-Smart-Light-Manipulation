import tinytuya
import json
import random
from doge import *
import schedule

# random color generator
def colorGenerator():
    num1 = random.randrange(0,257)
    num2 = random.randrange(0,257)
    num3 = random.randrange(0,257)

    return num1, num2, num3

def get_all_smart_lights():
    # read all devices from devices.json
    with open("devices.json") as file:
        content = json.load(file)
    return content


# set the color of the light
def set_color_light(bulbObj, color):
    rbgValueColor = tuple(bytes.fromhex("#00000"))


# get doge price
def dogePrice():
    currentPrice = get_doge_price()
    # compare prices

    if currentPrice < 0.05:
        print("Buy the dip")
        execute(0,255,0)

    elif currentPrice > 0.06:
        print("Selling Dip")
        execute(255,0,0)
    
    elif currentPrice >= 0.05:
        print("Okay value")
        execute(0,0,255)

# execute light actions
def execute(r, g, b):
    lightObjs = []              # light objects

    lights = get_all_smart_lights()
    
    for light in lights:
        lightId = light["id"]
        lightKey = light["key"]
        lightIp = light["ip"]
        d = tinytuya.BulbDevice(lightId, lightIp, lightKey)
        d.set_version(3.3)
        data = d.status()  

        lightObjs.append(d)
    
    for d in lightObjs:
        # color 
        d.turn_on()
        d.set_colour(r, g, b)
        
        # d.set_mode('music')



def main():
  schedule.every(10).seconds.do(dogePrice)
  while True:
      schedule.run_pending()
main()