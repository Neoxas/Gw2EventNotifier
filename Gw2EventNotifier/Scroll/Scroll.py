""" This module deals with scrolling the text on the scrollphat

It deals with checking if any events are within the window and if so
queues them to be executed.
"""
__author__ = 'Alex John Powell'
__version__='0.1'

import scrollphathd as sphd

#TODO Finish implementing plan
""" Planned Method:
    - Loop events
    - If event is within window, add to queue
    - Loop queue, start single thread for displaying message.
        - Lock thread during this point
        - Dequeue event and raise name
        - unlock quue when done
"""

sphd.clear();
_SCROLL_TIME = 5 * 60;
_SCROLL_THREAD = threading.thread()
_SCROLL_LOCK = threading.lock()
_EVENT_QUEUE = List[Event]

def _ScrollText( message: str ):
    # Scroll text on scroll phat

def _StartScrollThread( message: str )
    # Start a thread to scroll the message for the set time

def ScrollEvent( message: str ):
    # Check if lock, if not the start new scroll thread

while True:
	# Update all events
	for event in BossEvents.BossEvents:
            if( event.WithinWindow() and not event.HasFired() ):
                    _EVENT_QUEUE.insert( event, 0 )
                    event.Fired()
         
        # If there is anything in the queue, trigger it to scroll
        if any _EVENT_QUEUE:
            event = _EVENT_QUEUE.pop()
            ScrollEvent( event.Name() )

