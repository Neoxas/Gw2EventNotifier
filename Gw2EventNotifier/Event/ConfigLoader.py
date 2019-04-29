from Event import Event
import yaml


"""Yaml dumper for Event class"""
def _event_representer( dumper, data ):
        return dumper.represent_mapping( '!Event', data)                                                    
yaml.add_representer( Event, _event_representer )

"""Yaml constructor for the Event class"""
def _event_constructor( loader, node ):
        # Deep maping description here
        # https://stackoverflow.com/questions/43812020/what-does-deep-true-do-in-pyyaml-loader-construct-mapping
        fields = loader.construct_mapping(
                node, deep=True)
        return Event( **fields )

yaml.add_constructor( '!Event', _event_constructor )

"""loads event array from config file"""
def load_config( filePath ):
    # Open stream and load events using
    # defined constructor
    stream = open( filePath, 'r')
    events = []
    for event in yaml.load_all( 
            stream, Loader=yaml.Loader):
        events.append( event )
    return events

