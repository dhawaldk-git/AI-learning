from database.database import get_connection

def add_asset(asset):
    """Add a new asset to the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO assets (assetnum, description, STATUS) VALUES (?, ?, ?)',
                   (asset.assetnum, asset.description, asset.status))
    conn.commit()
    conn.close()

def get_assets():
    """Retrieve all assets from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM assets')
    rows = cursor.fetchall()
    conn.close()
    return [{"assetnum": row[0], "description": row[1], "status": row[2]} for row in rows]

def get_asset_by_num(assetnum):
    """Retrieve an asset by its asset number."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''select * from assets where assetnum = ?''', (assetnum,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"assetnum": row[0], "description": row[1], "status": row[2]}
    return None

def update_asset(assetnum, asset):
    """Update an existing asset in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''update assets set description = ?, status = ? where assetnum = ?''', 
                   (asset.description, asset.status, assetnum))
    conn.commit()
    updated_rows = cursor.rowcount
    conn.close()
    return updated_rows > 0

def delete_asset(assetnum):
    """Delete an asset from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''delete from assets where assetnum = ?''', (assetnum,))
    conn.commit()
    deleted_rows = cursor.rowcount
    conn.close()
    return deleted_rows > 0