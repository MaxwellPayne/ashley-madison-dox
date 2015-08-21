def sql_escape(sql_param):
    # should sanitize query here                                                                                               
    return sql_param

def fetchall(cursor, sql_statement):
    cursor.execute(sql_statement)
    return cursor.fetchall()

def fetch_first_or_none(cursor, sql_statement):
    results = fetchall(cursor, sql_statement)
    return results[0] if len(results) else None
