from database import get_connection

def add_asset(asset):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''Insert INTO assets
    values (?, ?, ?)''', (asset.assetnum, asset.description, asset.status)) 
    conn.commit()
    conn.close()

def get_assets():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM assets''')
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_asset(assetnum):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''select * from assets where assetnum = ?''', (assetnum,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_asset(assetnum, asset):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''update assets set description = ?, status = ? where assetnum = ?''',
                   (asset.description, asset.status, assetnum))
    update_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return update_rows

def delete_asset(assetnum):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''delete from assets where assetnum = ?''', (assetnum,))
    delete_rows = cursor.rowcount
    print(f"Deleted {delete_rows} rows")
    conn.commit()
    conn.close()
    return delete_rows
