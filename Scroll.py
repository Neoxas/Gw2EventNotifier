import scrollphathd as sphd

sphd.clear();
_SCROLL_TIME = 5 * 60;
while True:
	# Update all events
	for event in BossEvents.BossEvents:
		event.WithinWindow();
	
	# If the event requires display, scroll it for set time
	for event in BossEvents.BossEvents:
		if( event.ToDisplay() and not event.Fired() ):
			# Scroll here then mark it as displayed
			event.StopDisplay()
		