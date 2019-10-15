# ZhenVis

ZhenVis is my AI Assistant, currently it is used to watering flowers.

This is the course project from [Internet of Things](https://www.andrew.cmu.edu/user/mm6/95-733/schedule.html) from [Michael J. McCarthy](https://www.andrew.cmu.edu/user/mm6/).

## Origin
ZhenVis is the "real" Jarvis, Zhen Means True in Chinese.

## Version
| Version | Networking                  | Power Control | AI Water Saving               |
| ------- | --------------------------- | ------------- | ----------------------------- |
| v1      | socketxp (*NOW EXPIRED*)    | USB Portal    | No                            |
| v2      | MQTT  (with AWS as Server)  | USB Portal    | No                            |
| v3      | MQTT   (with AWS as Server) | Relay         | No                            |
| v4      | MQTT  (with AWS as Server)  | Relay         | Weather API with ML Algorithm |



## Shopping List
* Raspberry Pi
* Dupont Wire (female-male)
* Soil Moisture Sensor
* Watering Pump System:
  * version 1, 2:5V Water Pump with USB Input
  * version 2+:
    * Small Watering System: 5V Water Pump with USB Input+ USB Relay + USB Charger
    * Strong watering system: 50V 2A Water Pump + Relay + 50V 2A transformer
