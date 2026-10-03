import os
import duckdb
from Evtx.Evtx import Evtx
import xml.etree.ElementTree as ET

def init_db(db_path="evidence.db"):
    conn = duckdb.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS normalized_events (
            record_id VARCHAR,
            timestamp_utc VARCHAR,
            host VARCHAR,
            user VARCHAR,
            event_id VARCHAR,
            channel VARCHAR,
            message TEXT
        )
    """)
    conn.close()

if __name__ == "__main__":
    print("EVTX Parser Module Ready.")