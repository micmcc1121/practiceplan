import time
import datetime

class AgendaItem:
  """Individual component items of an agenda
  """
  
  def __init__(self, name, minutes):
    """DOC HERE
    """
    self.name = name
    self.minutes = minutes

class Agenda:
  """Composition of a plan made up of items
  """

  def __init__(self, title):
    self.title = title

class Timer:
  """Timer object that keeps time left in each agenda itme.
  """

  def __init__(self, seconds, minutes):
    self.minutes = minutes
    self.seconds = seconds

  def countdown(minutes, seconds): 

    '''Sets and structures the command line timer and signals it's copmletion

    : param minutes : integer
    : param seconds : integer
    '''
    
    t = minutes * 60 + seconds

    while t: 
        minuntes, seconds = divmod(t, 60) 
        timer = '{:02}:{:02}'.format(minutes, seconds) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Time done!! On to the next Item!!!')  
  
class EndingTime:
  """Estimated ending time using dynaimcs of timer app
  """
  def __init__(self):
    pass

    
