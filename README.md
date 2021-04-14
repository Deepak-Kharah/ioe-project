# IOE Project

The IOE project contains two separate modules i.e. arduino and django

# Arduino

This module contains code for NodeMCU. Basically, this module is responsible for reading current consumed by the load (ie. bulb in our case), calculating the power out of it and sending it to the django's rest API using the inbuild Wi-Fi module.

# Django

This module contains code for reading the data from the nodeMCU and displaying the content as a graph into the webpage. For the graph, I am using Chart.js.

# Components

- NodeMCU
- ACS712 current sensor
- 9W bulb
- breadboard
- wires
- AC power source
- bulb holder
- plug

# Formulas I have used

Power = Potential Difference \* Current
Energy = Power \* time
Base Tariff = Energy \* Base cost

# APIs

| Method | url              | data  | description                   |
| :----- | :--------------- | :---: | :---------------------------- |
| GET    | /api/measurement |   -   | get raw power data            |
| POST   | /api/measurement | power | post power data to the server |
| GET    | /dashboard       |       | show graph data               |


# Try it out
In order to set up the django server, you need to have pipenv. Set up a pipenv and install the requirements from the requirement.txt and requirement-dev.txt. Later, run the migrations and then run the server using this command.

```shell
python3 manage.py runserver 0.0.0.0:8000
```

Remember to change all the code's endpoint with your device's IP address.

Now, upload the arduino code into the nodeMCU and setup the circuit accordingly.


# References

- [Demo Video](https://www.youtube.com/watch?v=qeBfdch5eps)
- [Presentation](static/smart_electric_meter.pps)
