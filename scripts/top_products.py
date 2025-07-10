import sqlite3
import pandas as pd
from pathlib import Path

# Путь к базе данных
# Path to the database
db_path = Path(__file__).resolve().parent.parent / "data" / "sales.db"
conn = sqlite3.connect(db_path)

# SQL-запрос
# SQL query
query = """
SELECT product,
       SUM(quantity) AS total_quantity,
       SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 10;
"""

# Загрузка результата в DataFrame
# Loading the result into a DataFrame
df = pd.read_sql_query(query, conn)

# Закрытие соединения
# Closing the connection
conn.close()

# Путь для сохранения отчета
# Path to save the Excel report
output_path = Path(__file__).resolve().parent.parent / "reports" / "top_products.xlsx"
df.to_excel(output_path, index=False)

# Сообщение
# Message
print(f"✅ Отчет по топ-10 продуктам сохранен: {output_path.name}")
print(f"✅ Top 10 products report saved: {output_path.name}")
