from datetime import timedelta
import datetime
import time
# Potentailly could do all this with a DB to make the queries easier
class Event(object):
	"""Represnets an event trigger"""
	_TIME_BEFORE_SHOW = 5

	_name = "DEFAULT"
	_fired = False
	_times = []
	_display = False

	"""Default constructor"""
	def __init__(self, name, times=[]):
		super(Event, self).__init__()
		self._name = name
		self._times = times

	def Name( self ):
		return self._name;

	""" Has the event fired?"""
	def Fired(self):
		return self._fired

	"""Should the event be displayed
	   Should be checked after WithinWindow"""
	def ToDisplay(self):
		return self._display

	"""Reset the event"""
	def Reset(self):
		self._fired = False
		self._display = False

	""" Stop displaying the event"""
	def StopDisplay(self):
		self._display = False
		self._fired = False


	"""Is the event within this window"""
	def WithinWindow(self):
		# Check if any items within the times match the current window
		# Current time
		currentTime = datetime.datetime.now();
		currentDelta = timedelta( 
			hours = currentTime.time().hour, 
			minutes =currentTime.time().minute, 
			seconds = currentTime.time().second )

		for time in self._times:
			eventDelta = timedelta(
				hours = time.tm_hour,
				minutes = time.tm_min,
				seconds = time.tm_sec
				)

			delta = eventDelta - currentDelta
			# Convert this to the minutes difference between event firing and current time
			minutes_delta = delta.total_seconds() / 60 
			# If positive and within window, needs to be displayed
			if minutes_delta > 0  and minutes_delta < self._TIME_BEFORE_SHOW:
				self._display = True