import sqlite3 
import pandas as pd
from pathlib import Path

# Подключение к базе данных
# Connecting to the database
db_path = Path(__file__).resolve().parent.parent / "data" / "sales.db"
conn = sqlite3.connect(db_path)

# SQL-запрос
# SQL query
query = """
SELECT product,
       COUNT(*) AS purchase_count,
       SUM(quantity) AS total_quantity,
       SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY product
HAVING COUNT(*) > 1
ORDER BY purchase_count DESC;
"""

# Загрузка результата в DataFrame
# Loading the result into a DataFrame
df = pd.read_sql_query(query, conn)

# Закрытие соединения
# Closing the connection
conn.close()

# Сохранение в Excel
# Saving to Excel
output_path = Path(__file__).resolve().parent.parent / "reports" / "repeated_products.xlsx"
df.to_excel(output_path, index=False)

# Сообщение
# Console message
print(f"✅ Отчет по повторным покупкам сохранен: {output_path.name}")
print(f"✅ Repeat purchases report saved: {output_path.name}")