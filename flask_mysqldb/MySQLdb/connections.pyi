import MySQLdb
from typing import Any, Optional

class Connection:
    def cursor(self, cursorclass: Optional[Any] = ...) -> MySQLdb.cursors.BaseCursor: ...
