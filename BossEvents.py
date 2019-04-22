import Event
import time as tm

BossEvents = [
	Event.Event( "Admiral Taidha Covington", [
		tm.strptime("00:00", "%H:%M" ),
		tm.strptime("03:00", "%H:%M" ),
		tm.strptime("06:00", "%H:%M" ),
		tm.strptime("09:00", "%H:%M" ),
		tm.strptime("12:00", "%H:%M" ),
		tm.strptime("15:00", "%H:%M" ),
		tm.strptime("18:00", "%H:%M" ),
		tm.strptime("21:00", "%H:%M" )
		]),
	Event.Event( "Claw of Jormag", [ 
		tm.strptime( "02:30", "%H:%M" ),
		tm.strptime( "05:30", "%H:%M" ),
		tm.strptime( "08:30", "%H:%M" ),
		tm.strptime( "11:30", "%H:%M" ),
		tm.strptime( "14:30", "%H:%M" ),
		tm.strptime( "17:30", "%H:%M" ),
		tm.strptime( "20:30", "%H:%M" ),
		tm.strptime( "23:30", "%H:%M" )
		])
];