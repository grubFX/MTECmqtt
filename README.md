## fork of [MTECmqtt](https://github.com/croedel/MTECmqtt) by [@croedel](https://github.com/croedel) who thankfully did all the hard work

- the ultimate goal is to write an MTEC integration for HomeAssistant, that locally talks to your MTEC inverter
- I plan to reuse the existing local Modbus communication implementation to talk to the inverter as previously
- but instead of running the script on another server and pushing the data to HomeAssistant via MQTT I want to have HomeAssistant run the communication and directly expose the respective values as sensors
- nice to have: config_flow / nice onboarding, without any manual yaml config required
