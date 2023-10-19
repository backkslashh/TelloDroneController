from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
battery_percentage = tello.get_battery()

def check_battery():
  if battery_percentage <= 10:
    print(f"WARNING: Battery percentage at critical level (%{battery_percentage}). Do not fly far, and please charge after use")
  elif 10 < battery_percentage <= 50:
    print(f"WARNING: Battery percentage at concerning level (%{battery_percentage}). Do not fly far, and please charge after use")
  else battery_percentage >= 50:
    print(f"Good to go! Battery percentage at %{battery_percentage}"

def get_flight_time(percentage):
  return (percentage*0.01)*13

check_battery()
print('Flight Time (min):'+str(get_flight_time(battery_percentage)))
confirmation = input('Takeoff? Y/N')
if confirmation == "Y":
  print('Takeoff!!!!')
  drone.takeoff()
  sleep(15)
  drone.land()
  exit()
elif confirmation == "N":
  print(':( Ok then')
  exit()
    
