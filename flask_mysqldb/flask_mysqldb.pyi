import MySQLdb

class MySQL(object):
    @property
    def connection(self) -> MySQLdb.connections.Connection:...

    def init_app(self,app):...
