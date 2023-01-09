from loader_api import ILoader, Record
import json

class JsonLoader( ILoader ):
    def __init__( self, path: str ):
        self.path__ = path

    def title( self ) -> str:
        return "json"

    def extension( self ) -> str:
        return "*.json"

    def exportRecords( self, data: dict[ str, list[Record] ] ):
        json_str = json.dumps( data )
        print( json_str )

    def importRecords( self ) -> dict[ str, list[Record] ]:
        with open( self.path__ ) as src:
            return json.loads( src.read() )
