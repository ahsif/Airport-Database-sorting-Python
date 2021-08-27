#Written by Ahsif Safdar. Ahsif.Safdar@gmail.com
import airline, airport, flight, csv
airline_dict = {}
airport_dict = {}
date_dict = {}
data = []
count = 0
flight_list = []  #this will be used to populate the date_dict

with open('flights_info.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        if (row['AIRLINE'] not in airline_dict.keys()
            ):  #ensure the key does not already exist
            airline_dict[row['AIRLINE']] = airline.Airline(row['AIRLINE'], (row['AIRLINE_NAME']))

        if row['ORIGIN_AIRPORT'] not in airport_dict.keys(
        ):  #ensure the key does not already exist
            airport_dict[row['ORIGIN_AIRPORT']] = airport.Airport(
                row['ORIGIN_AIRPORT'], row['ORIGIN_NAME'], row['ORIGIN_CITY'],
                row['ORIGIN_STATE'])

        if row['DESTINATION_AIRPORT'] not in airport_dict.keys(
        ):  # ensure the key doesnt already exist
            airport_dict[row['DESTINATION_AIRPORT']] = airport.Airport(
                row['DESTINATION_AIRPORT'], row['DESTINATION_NAME'],
                row['DESTINATION_CITY'], row['DESTINATION_STATE'])

        newestFlight = flight.Flight(
            row['YEAR'],
            row['MONTH'], row['DAY'], airline_dict[row['AIRLINE']],
            int(row['FLIGHT_NUMBER']), airport_dict[row['ORIGIN_AIRPORT']],
            airport_dict[row['DESTINATION_AIRPORT']],
            int(row['SCHEDULED_DEPARTURE']), int(row['DEPARTURE_TIME']),
            int(row['DEPARTURE_DELAY']), int(row['SCHEDULED_ARRIVAL']),
            int(row['ARRIVAL_TIME']), int(row['ARRIVAL_DELAY'])
        )  #I will store the newest flight, in order to not have to write all this again later.

        flight_list.append(newestFlight)  #add the newest flight to the overall list of flights that we created

        airline_dict[row['AIRLINE']].add_flight(newestFlight)  #insert it into the airline dictionary by key as well

        airport_dict[row['DESTINATION_AIRPORT']].add_dest_flight(newestFlight)  #insert newest flight into the destionation airports dictionary

        airport_dict[row['ORIGIN_AIRPORT']].add_origin_flight(
            newestFlight)  # and the origin airports dictionary

for n in flight_list:  # this loop is responsible for populating the date dictionary and the main reason I created the flight_list list.
    if n.get_date() not in date_dict.keys(
    ):  # if the date is not yet in the key we need to create a list and insert the flight
        listhere = []
        listhere.append(n)
        date_dict[n.get_date()] = listhere
    else:  # if the key does exist we need to append data into the list
        listhere.append(n)
for keys in date_dict:
    date_dict[keys].sort(key=lambda n: n.get_scheduled_departure(
    ))  #sorts the data inside of the dictionary by SCHEDULED_DEPARTURE


#Queries
def query1():
    for keys in date_dict:
        print(keys + ':')
        date_dict[keys].sort(key=lambda n: n.get_arrival_delay(), reverse=True)
        print(date_dict[keys][0])


def query2():
    for keys in sorted(airport_dict):
        print(airport_dict[keys])

        odelay = len([f for f in airport_dict[keys].get_origin_flights() if f.get_departure_delay() > 15])

        ddelay = len([f for f in airport_dict[keys].get_dest_flights() if f.get_arrival_delay() > 15])

        print("origin delays: " + str(odelay))
        print("destination delays: " + str(ddelay))

#Written by Ahsif Safdar. Ahsif.Safdar@gmail.com
#dict['US airlines'] = data[] = flight objects
def query3():
    for key in sorted(airline_dict, key=lambda e: airline_dict[e].get_name()):
        print(airline_dict[key].get_name())
        for k in date_dict:
            print(k)
            newList = [(f.get_origin_airport().get_code(),
                        f.get_dest_airport().get_code())
                       for f in airline_dict[key].get_flights()
                       if f.get_date() == k]
            dataList = [
                (f.get_origin_airport().get_code(),
                 f.get_dest_airport().get_code(), f.get_arrival_delay())
                for f in airline_dict[key].get_flights() if f.get_date() == k]
            newList.sort()
            dataList.sort()
            mySet = set(newList)  # (flg, phx)
            lastdict = {}
            for x in mySet:  #for tuples of org,dest
                count = 0
                delayed = 0
                for (a, b,
                     d) in dataList:  #for (origin, dest and delay) in datalist
                    if x == (a, b):  #ensure that the origin and dest airports match the set.
                        count += 1
                        if d > 15:  #How many flights were delayed greater than 15 minutes?
                            delayed += 1
                lkey = str(x)[2:5] + ' ' + str(x)[9:12]  #format the strings to remove "(',')" using slicing, giving us org dest airport names and storing them as keys to print
                str1 = (str(count) + ' ' + "{0:.0%}".format((count - delayed) / count))  #I need to format the math as a percentage, this achieves that.
                lastdict[lkey] = str1
            for lk in sorted(lastdict):
                print(lk + ' ' + lastdict[lk])

#Written by Ahsif Safdar. Ahsif.Safdar@gmail.com
#Input Output Testing - DO NOT MODIFY ANYTHING BELOW THIS LINE
testcase = input()
print(testcase)
if testcase == 'testcase 1':
    #Tests classes are created correctly
    airport1 = airport.Airport('PHX',
                               'Phoenix Sky Harbor International Airport',
                               'Phoenix', 'AZ')
    airport2 = airport.Airport('LAS', 'McCarran International Airport',
                               'Las Vegas', 'NV')
    airline1 = airline.Airline('WN', 'Southwest Airlines Co.')
    flight1 = flight.Flight(2021, 2, 16, airline1, '240', airport1, airport2,
                            1230, 1235, 5, 215, 225, 10)
    airport1.add_origin_flight(flight1)
    airport2.add_dest_flight(flight1)
    airline1.add_flight(flight1)
    #Repr Functions
    print(airport1, airport2, airline1, flight1, sep='\n')
    #Airline Getter Functions
    print(airline1.get_code(), airline1.get_name(), airline1.get_flights())
    #Airport Getter Functions
    print(airport1.get_code(), airport1.get_name(), airport1.get_city(),
          airport1.get_state(), airport1.get_origin_flights(),
          airport1.get_dest_flights())
    #Flight Getter Functions
    print(flight1.get_date(), flight1.get_year(), flight1.get_month(),
          flight1.get_day(), flight1.get_airline(), flight1.get_flight_num(),
          flight1.get_origin_airport(), flight1.get_dest_airport(),
          flight1.get_scheduled_departure(), flight1.get_departure_time(),
          flight1.get_departure_delay(), flight1.get_scheduled_arrival(),
          flight1.get_arrival_time(), flight1.get_arrival_delay())
elif testcase == 'testcase 2':
    print(airline_dict)
    print(airport_dict)
    print(date_dict['2015-01-10'])
    if (len(
            set([
                f.get_airline() for d in date_dict.keys() for f in date_dict[d]
            ]))) != 3:
        print("DUPLICATE AIRLINE OBJECTS")
    if (len(
            set([
                f.get_origin_airport() for d in date_dict.keys()
                for f in date_dict[d]
            ]))) != 6:
        print("DUPLICATE AIRPORT OBJECTS: origin")
    if (len(
            set([
                f.get_dest_airport() for d in date_dict.keys()
                for f in date_dict[d]
            ]))) != 6:
        print("DUPLICATE AIRPORT OBJECTS: destination")
elif testcase == 'testcase 3':
    query1()
elif testcase == 'testcase 4':
    query2()
elif testcase == 'testcase 5':
    query3()
else:
    fl = date_dict['2015-01-05'][0]
    for t in (fl.get_date(),fl.get_year(),fl.get_month(),fl.get_day(),fl.get_airline(),fl.get_flight_num(),fl.get_origin_airport(),fl.get_dest_airport(),fl.get_scheduled_departure(),fl.get_departure_time(),fl.get_departure_delay(),fl.get_scheduled_arrival(),fl.get_arrival_time(),fl.get_arrival_delay()):
        print(type(t))
#Written by Ahsif Safdar. Ahsif.Safdar@gmail.com