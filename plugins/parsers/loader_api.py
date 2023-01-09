from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Novel:
    Name: str
    Author: str
    Genre: str

@dataclass
class Record:
    Title: str
    Novels: list[Novel]
    PublishHouse: str
    PublishYear: int
    DateStart: datetime
    DateFinish: datetime
    Pages: int

class ILoader:
    @abstractmethod
    def title( self ) -> str:
        pass

    @abstractmethod
    def extension( self ) -> str:
        pass

    @abstractmethod
    def exportRecords( self, data: dict[ str, list[Record] ] ):
        pass

    @abstractmethod
    def importRecords( self ) -> dict[ str, list[Record] ]:
        pass

