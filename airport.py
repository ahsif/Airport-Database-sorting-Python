#Written by Ahsif Safdar. Ahsif.Safdar@gmail.com
class Airport:
  def __init__(self, code, name, city, state):
    self._code = code
    self._name = name
    self._city = city
    self._state = state
    self._origin_flights = []
    self._dest_flights = []
  #Written by Ahsif Safdar. Ahsif.Safdar@gmail.com
  def get_code(self):
    return self._code

  def get_name(self):
    return self._name

  def get_city(self):
    return self._city
  #Written by Ahsif Safdar. Ahsif.Safdar@gmail.com
  def get_state(self):
    return self._state

  def get_origin_flights(self):
    return self._origin_flights

  def get_dest_flights(self):
    return self._dest_flights
  #Written by Ahsif Safdar. Ahsif.Safdar@gmail.com
  def add_origin_flight(self, flight):
    self._origin_flights.append(flight)

  def add_dest_flight(self, flight):
    self._dest_flights.append(flight)

  def __repr__(self):
    return "(" + self._code + ", " +self._name + ", "+ self._city +", " + self._state  + ", "+ str(len(self._origin_flights)) + ", "+ str(len(self._dest_flights)) + ")"
    #We use the str(len()) in order to return the amount of destination and origin flights, not the flight objects themselves.