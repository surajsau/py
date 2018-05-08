#!/usr/bin/python
import sqlite3
import struct

TABLE_NAME = 'tbl_name'
DB_NAME = 'Japanese4.db'

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect(DB_NAME)

conn.row_factory = dict_factory

tables = conn.execute('SELECT * FROM sqlite_master WHERE type=\'table\'')

for table in tables:
    if table[TABLE_NAME] == 'entry_examples':
        table_cursor = conn.execute('SELECT * FROM ' + table[TABLE_NAME] + ' LIMIT 3')

        results = table_cursor.fetchall()

        for result in results:
            blob = result['Examples']
            f = open('blob.txt', 'w')
            f.write(struct.unpack(">i", blob))
            # print result
        # print results

conn.close()
