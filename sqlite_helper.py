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
    
    def insert_data(self, table_name: str, data: Dict[str, Any]) -> int:
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        params = tuple(data.values())
        
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"데이터 삽입 오류: {e}")
            return -1

    def fetch_data(self, table_name: str, condition: str = "", params: tuple = ()) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        return self.execute_query(query, params)

    def update_data(self, table_name: str, data: Dict[str, Any], condition: str, params: tuple) -> int:
        set_clause = ', '.join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        params = tuple(data.values()) + params
        
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            print(f"데이터 수정 오류: {e}")
            return -1

    def delete_data(self, table_name: str, condition: str, params: tuple) -> int:
        query = f"DELETE FROM {table_name} WHERE {condition}"
        
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            print(f"데이터 삭제 오류: {e}")
            return -1
