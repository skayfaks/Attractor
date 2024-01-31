# Python
from pathlib import Path
from configparser import ConfigParser, SectionProxy
# External
import pandas as pd
import sqlalchemy as sql
from sqlalchemy.engine.base import Engine, Connection


def load_configs() -> SectionProxy:
    # Load config file
    configs_location = Path(__file__).parent / 'credentials.ini'
    assert configs_location.exists(), f'Unable to find configs at {configs_location}'
    # Get parser
    configs = ConfigParser()
    configs.read(configs_location)
    # Return credentials for the db
    assert 'PostgreSQL' in configs.sections(), 'PostgreSQL section not found'
    print('Configs are loaded...')
    return configs['PostgreSQL']


class Database:

    def __init__(self):
        # Private
        self._configs = None
        self._engine = None
        self._connection = None

    @property
    def configs(self) -> SectionProxy:
        if self._configs is None:
            self._configs = load_configs()
        return self._configs

    @property
    def engine(self) -> Engine:
        if self._engine is None:
            self._engine = self._build_engine()
        return self._engine

    @property
    def connection(self) -> Connection:
        if self._connection is None:
            self._connection = self.engine.connect()
        return self._connection

    def _build_engine(self) -> Engine:
        server = self.configs['Host'] + ':' + self.configs['Port']
        credentials = self.configs['User'] + ':' + self.configs['Password']
        database = self.configs['Database']
        engine = sql.create_engine(fr'postgresql://{credentials}@{server}/{database}')
        return engine

    def reconnect(self) -> Connection:
        self._connection = None
        return self.connection

    def execute(self, query: str) -> pd.DataFrame:
        return pd.read_sql(query, self.connection)


DB = Database()
