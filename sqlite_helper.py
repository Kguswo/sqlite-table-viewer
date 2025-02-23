import sqlite3
from typing import List, Dict, Any

class DBHelper:
    def __init__(self, db_path: str):
        self.db_path = db_path
        
    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        try:
            with self.connect() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute(query, params)
                
                if not cursor.description:
                    return []
                    
                columns = [description[0] for description in cursor.description]
                results = []
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
                    
                return results
                
        except sqlite3.Error as e:
            print(f"데이터베이스 오류 발생: {e}")
            return []

    def get_table_info(self, table_name: str) -> List[Dict[str, Any]]:
        query = f"PRAGMA table_info({table_name})"
        return self.execute_query(query)