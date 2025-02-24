# SQLite Table Viewer

This is a simple Python script that connects to an SQLite database, lists all tables, displays their structure, and previews sample data.

## 📌 Features
- List all tables in an SQLite database
- Show table structure (column names & data types)
- Display sample data from each table (up to 5 rows)

## 🛠️ Requirements
- Python 3.7+
- `sqlite3` (built-in)

## 🚀 Usage
1. Clone the repository:
```sh
git clone https://github.com/your-username/sqlite-table-viewer.git
cd sqlite-table-viewer
```
   
2. Ensure you have an SQLite database file (e.g., `attendance.db`).
Run the script:
```sh
python check_db.py
```

4. The script will print:
- A list of tables
- Table structure (columns & types)
- Sample data (up to 5 rows)

### 📝 Example Output
```pgsql
=== DB 테이블 목록 ===

테이블: users
구조:
컬럼: id, 타입: INTEGER
컬럼: name, 타입: TEXT
컬럼: age, 타입: INTEGER

데이터 샘플:
{'id': 1, 'name': 'Alice', 'age': 25}
{'id': 2, 'name': 'Bob', 'age': 30}

==================================================

```
