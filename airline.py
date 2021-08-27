class Airline:
  
  def __init__(self, code, name):
    self._code = code
    self._name = name
    self._flight = [] #a list of flight objects that belong to this airline is created for access later

  def get_code(self):
    return str(self._code)
  #Written by Ahsif Safdar. Ahsif.Safdar@gmail.com
  def get_name(self):
    return str(self._name)

  def get_flights(self):
    return self._flight
  #Written by Ahsif Safdar. Ahsif.Safdar@gmail.com
  def add_flight(self, flight):
    self._flight.append(flight)
    
  def __repr__(self):
    return "(" + self._code +", "+ self._name +", "+ str(len(self._flight))+")"