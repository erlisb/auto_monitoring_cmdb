import sqlite3

connection = sqlite3.connect('cmdb.db')

cursor = connection.cursor()


# CREATE hosts AND services TABLES
create_table_hosts = "CREATE TABLE IF NOT EXISTS hosts (  host_id INTEGER PRIMARY KEY, \
                                                    host_object_id INTEGER, \
                                                    display_name TEXT, \
                                                    address TEXT, \
                                                    check_interval INTEGER, \
                                                    check_command TEXT, \
                                                    check_command_args TEXT, \
                                                    status TEXT )"

cursor.execute(create_table_hosts)

create_table_services = "CREATE TABLE IF NOT EXISTS services (   service_id INTEGER PRIMARY KEY, \
                                                        host_object_id INTEGER, \
                                                        display_name TEXT , \
                                                        check_interval INTEGER, \
                                                        check_command TEXT, \
                                                        check_command_args  TEXT, \
                                                        status TEXT )"
cursor.execute(create_table_services)

# INSERT ITEMS INTO DB
insert_table_hosts = 'INSERT INTO hosts VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)'
cursor.execute(insert_table_hosts, (1, 'pyrana_host', '127.0.0.1', 2, 'hostalive', None, 'active',))
cursor.execute(insert_table_hosts, (2, 'pyrana_host', '127.0.0.1', 2, 'dummy', None, 'active',))
cursor.execute(insert_table_hosts, (3, 'pyrana_host', '127.0.0.1', 2, 'ping', None, 'new',))

connection.commit()
connection.close()