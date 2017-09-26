from __future__ import print_function
import json
import sys
import urllib2


if not len(sys.argv) == 3:
	print ("Invalid number of arguments. Run as: python show_bus_locations_as11566.py <KEY> <LINE>")
	sys.exit()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

#print(json.dumps(data, indent=4))

Count_bus = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

print('Bus Name:', sys.argv[2])
print ('Number of Vehicles:', Count_bus)

for i in range(Count_bus):
	Lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	Long = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	print ('Bus %d - latitude : %s ,longitude : %s' %(i,Lat,Long))
