'''
  sendSMS.py - This is basic SMS Service example.
  Created by Yasin Kaya (selengalp), October 31, 2018.
'''
from cellulariot import cellulariot
import time

node = cellulariot.CellularIoTApp()
node.disable()
time.sleep(0.5)
node.enable()
time.sleep(0.5)
node.powerUp()

node.getResponse("RDY")
node.sendATComm("ATE1","OK\r\n")

node.sendSMS("+905433988390","hello world from turkey")
