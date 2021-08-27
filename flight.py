#Written by Ahsif Safdar. Ahsif.Safdar@gmail.com
class Flight:
  def __init__(self, year, month, day, airline, flight_num, origin_airport, dest_airport, scheduled_departure, departure_time, departure_delay, scheduled_arrival, arrival_time, arrival_delay):
    self._date = str(year)+'-'+ str(f'{int(month):02d}') +'-'+ str(f'{int(day):02d}') #format the date so that it remains uniform yyyy-mm-dd
    self._year = year
    self._month = month
    self._day = day
    self._airline = airline
    self._flight_num = flight_num
    self._origin_airport = origin_airport
    self._dest_airport = dest_airport
    self._scheduled_departure = scheduled_departure
    self._departure_delay = departure_delay
    self._scheduled_arrival = scheduled_arrival
    self._arrival_time = arrival_time
    self._arrival_delay = arrival_delay
    self._departure_time = int(departure_time)

  def get_date(self):
    return self._date
    
  def get_year(self):
    return self._year

  def get_month(self):
    return self._month

  def get_day(self):
    return self._day

  def get_airline(self):
    return self._airline

  def get_flight_num(self):
    return self._flight_num

  def get_origin_airport(self):
    return self._origin_airport

  def get_dest_airport(self):
    return self._dest_airport

  def get_scheduled_departure(self):
    return self._scheduled_departure

  def get_departure_time(self):
    return self._departure_time

  def get_departure_delay(self):
    return self._departure_delay

  def get_scheduled_arrival(self):
    return self._scheduled_arrival

  def get_arrival_time(self):
    return self._arrival_time

  def get_arrival_delay(self):
    return self._arrival_delay
  def __repr__(self):
    return "(" + self._date +", "+ self._airline.get_code()+", "+ str(self._flight_num)+", "+self._origin_airport.get_code()+", "+self._dest_airport.get_code()+", "+str(self._scheduled_departure)+", "+str(self._departure_time)+", "+str(self._departure_delay)+", "+str(self._scheduled_arrival)+", "+str(self._arrival_time)+", "+str(self._arrival_delay)+")"