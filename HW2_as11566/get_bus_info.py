
from __future__ import print_function
import json
import sys
import urllib2


if not len(sys.argv) == 4:
	print ("Invalid number of arguments. Run as: python get_bus_info_as11566.py <KEY> <BUS_LINE> <BUS_LINE>.csv")
	sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

fout = open(sys.argv[3],"w")
fout.write("Latitude,Longitude,Stop Name,Stop Status")

 
Count_bus = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

print('Bus Name:', sys.argv[2])
print ('Number of Vehicles:', Count_bus)

for i in range(Count_bus):
    Lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    Long = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    if data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']=={}:
        stop_name = 'NA'
    else: 
        stop_name = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    if data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']=={}:
        stop_status = 'NA'
    else: 
        stop_status = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'] 

fout.write("/n%s,%s,%s,%s" %(Lat, Long, stop_name, stop_status))

