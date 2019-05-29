from datetime import timedelta
import datetime
import time
import yaml

# Potentailly could do all this with a DB to make the queries easier
class Event:
	"""Represnets an event trigger"""
	__TIME_BEFORE_SHOW = 5

	"""Default constructor"""
	def __init__(self, name, times):
		self.__name = name
		self.__rawTimes = times
		self.__fired = False
		self.__display = False
		self.__times = self.__convertTime( self.__rawTimes )

	def __repr__(self):
		return "%s(name=%r, times=%r)" %(
			self.__class__.__name__, self.__name, self.__rawTimes) 

	def __convertTime(self, times ):
		_tmp = []
		for eventTime in times:
			_tmp.append( 
				time.strptime( eventTime, "%H:%M" ) )
		return _tmp

	def Name( self ) -> str:
		return self.__name;

	def Times( self ) -> List[ datetime ]:
		# This occurs here due to (potential) lazy load problem with yaml
		return self.__convertTime( self.__rawTimes );

	def RawTimes( self ) -> List[ str ]:
		return self.__rawTimes;

	""" Has the event fired?"""
	def Fired(self) -> bool:
		return self.__fired

	"""Should the event be displayed
	   Should be checked after WithinWindow"""
	def ToDisplay(self) -> bool:
		return self.__display
        
        def Displayed( self ):
            self.__display = True

	"""Reset the event"""
	def Reset(self):
		self.__fired = False
		self.__display = False

	""" Stop displaying the event"""
	def StopDisplay(self):
		self.__display = False
		self.__fired = True


	"""Is the event within this window"""
	def WithinWindow(self) -> bool:
		# Check if any items within the times match the current window
		# Current time
		currentTime = datetime.datetime.now();
		currentDelta = timedelta( 
			hours = currentTime.time().hour, 
			minutes =currentTime.time().minute, 
			seconds = currentTime.time().second )

		for time in self.__times:
			eventDelta = timedelta(
				hours = time.tm_hour,
				minutes = time.tm_min,
				seconds = time.tm_sec
				)

			delta = eventDelta - currentDelta
			# Convert this to the minutes difference between event firing and current time
			minutes_delta = delta.total_seconds() / 60 
			# If positive and within window, needs to be displayed
			if minutes_delta > 0  and minutes_delta < self.__TIME_BEFORE_SHOW:
				self.__display = True
                return self.__display
