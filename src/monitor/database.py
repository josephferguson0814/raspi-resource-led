import mysql.connector
import collector
import time

def make_sql_data_base(num_iterations, host, user, password):
	for i in range(1, num_iterations):
		raw_data = collector.get_usage_info()
		time_stamp = raw_data["time_stamp"]
		cpu_data = raw_data["cpu"]
		ram_data = raw_data["ram"]

		conn = mysql.connector.connect(
		host=host,
		user=user,
		password=password
		)

		cursor = conn.cursor()

		cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")
		cursor.execute("USE my_database")
		cursor.execute("CREATE TABLE IF NOT EXISTS usage_data (row_num INT AUTO_INCREMENT PRIMARY KEY, time_stamp TIMESTAMP, ram FLOAT, cpu FLOAT)")
		cursor.execute("INSERT INTO usage_data (time_stamp, ram, cpu) VALUES (%s, %s, %s)", (time_stamp, ram_data, cpu_data))
		conn.commit()
		time.sleep(5)

	cursor.close()
	conn.close()

make_sql_data_base(100)