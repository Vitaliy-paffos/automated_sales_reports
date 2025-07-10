import pandas as pd
import sqlite3
from pathlib import Path

# Подключение к базе
# Connecting to the database
db_path = Path(__file__).resolve().parent.parent / "data" / "sales.db"
conn = sqlite3.connect(db_path)

# SQL-запрос
# SQL query
query = """
SELECT category,
       SUM(quantity) AS total_quantity,
       SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY category
ORDER BY total_revenue DESC;
"""

# Выполнение запроса
# Executing the query
summary = pd.read_sql_query(query, conn)

# Сохранение результата
# Saving the result
output_path = Path(__file__).resolve().parent.parent / "reports" / "category_summary.xlsx"
summary.to_excel(output_path, index=False)

# Закрытие соединения
# Closing the connection
conn.close()

print(f"✅ Таблица создана и отчет успешно сохранен: {output_path.name}")
print(f"✅ Table created and report successfully saved: {output_path.name}")