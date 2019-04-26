import yaml
from Event import Event

def event_representer( dumper, data ):
	return dumper.represent_scalar( '!Event', data)

yaml.add_representer( Event, event_representer )

def event_constructor( loader, node ):
	print( node )
	fields = loader.construct_mapping(node)
	print( fields )
	print( fields['times'])
	# Something strange is going on here
	# If I watch the constructor or fields parameter, time is blank
	# however if  I check the value, it is set
	return Event( **fields )
yaml.add_constructor( '!Event', event_constructor )

test = Event( "Namez", ["00:00"])
print( test.Name() )
print( test.Times() )
print( test )
print()

stream = open( 'EventConfig.yaml', 'r' )
eventArr = []
for data in yaml.load_all( stream, Loader=yaml.Loader ):
	eventArr.append( data )
	print( data )
	print( data.Name() )
	print( data.Times() )
	print( data.RawTimes())

print( eventArr[ 0 ] )
print( eventArr[ 0 ].Times() )