import os
import duckdb
from Evtx.Evtx import Evtx

def init_db(db_path="evidence.db"):
    conn = duckdb.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS normalized_events (
            record_id INTEGER,
            timestamp_utc VARCHAR,
            host VARCHAR,
            user VARCHAR,
            event_id VARCHAR,
            channel VARCHAR,
            message TEXT
        )
    """)
    conn.close()

def parse_evtx_to_db(evtx_path="app/sample.evtx", db_path="evidence.db"):
    init_db(db_path)
    conn = duckdb.connect(db_path)
    
    print(f"Opening {evtx_path}...")
    inserted_count = 0
    
    try:
        with Evtx(evtx_path) as log:
            for idx, record in enumerate(log.records()):
                try:
                    xml_content = record.xml()
                    timestamp_utc = "" # Can be extracted safely from XML or left blank for raw parsing
                    
                    conn.execute("""
                        INSERT INTO normalized_events (record_id, timestamp_utc, message)
                        VALUES (?, ?, ?)
                    """, (idx + 1, timestamp_utc, xml_content))
                    inserted_count += 1
                except Exception as inner_e:
                    continue
    except Exception as e:
        print(f"Error opening EVTX file: {e}")
        
    conn.close()
    print(f"Parsing complete! Successfully inserted {inserted_count} events into 'evidence.db'.")

if __name__ == "__main__":
    parse_evtx_to_db()