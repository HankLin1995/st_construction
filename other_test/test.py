from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# 創建資料庫引擎
engine = create_engine('mysql+mysqlconnector://root:a0912052274@localhost:3306/engineering_qc')

# 創建一個會話
Session = sessionmaker(bind=engine)
session = Session()

# 定義 ALTER TABLE 語句
alter_sql = text('ALTER TABLE projects ADD COLUMN new_column_name VARCHAR(255)')

# 執行 ALTER TABLE 語句
session.execute(alter_sql)
session.commit()

# 關閉會話
session.close()