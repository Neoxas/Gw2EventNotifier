import yaml
from Event import Event
import ConfigLoader

events = ConfigLoader.load_config( 
        'EventConfig.yaml' )

print( events )
print( events[0] )
