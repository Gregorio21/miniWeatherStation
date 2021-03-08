# miniWeatherStation
Arduino device to measure temp/humidity and record/graph that data
This project features an arduino, connected to a dht11 sensor to get humidity and temperature, as well as an lcd display to display this data. The data is then collected using a Python program that reads the serial port and records the data on a file. Another python program then graphs the data using the matplotlib library.

The repository contains the dataxx-xx.txt files that contain the collected data named by the date the data is collected. graphxx-xx.png which follows the same naming pattern as the data files and contains a graph of the corresponding data file. 2 Python files named dataCollection and graphing which do as the names suggest. A picture named, arduinoSetup.jpg showing the Arduino wiring. Finally a folder with the same name as the repository which contains the code for the Arduino written in C/C++.
