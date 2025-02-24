from sqlite_helper import DBHelper

def main():
    # DB 연결
    db = DBHelper("sample.db") # 파일 붙여넣은 뒤 sample.db 부분을 변경해서 조회하면 된다.
    
    # 테이블 목록 조회
    tables = db.execute_query("SELECT name FROM sqlite_master WHERE type='table'")
    
    if not tables:
        print("테이블이 없습니다.")
        return
        
    print("\n=== DB 테이블 목록 ===")
    for table in tables:
        table_name = table['name']
        print(f"\n테이블: {table_name}")
        
        # 테이블 구조 확인
        table_info = db.get_table_info(table_name)
        print("\n구조:")
        for column in table_info:
            print(f"컬럼: {column['name']}, 타입: {column['type']}")
        
        # 데이터 조회
        sample_data = db.execute_query(f"SELECT * FROM {table_name}")
        print("\n데이터 조회:")
        for row in sample_data:
            print(row)
        print("\n" + "="*50)

if __name__ == "__main__":
    main()