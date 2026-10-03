import duckdb

def test_query():
    conn = duckdb.connect("evidence.db")
    count = conn.execute("SELECT COUNT(*) FROM normalized_events").fetchone()[0]
    print(f"Total events found in database: {count}")
    
    print("\nSample records:")
    samples = conn.execute("SELECT record_id, timestamp_utc FROM normalized_events LIMIT 5").fetchall()
    for row in samples:
        print(f" - Record ID: {row[0]} | Timestamp: {row[1]}")
        
    conn.close()

if __name__ == "__main__":
    test_query()
