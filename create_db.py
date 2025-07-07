import sqlite3
import os

def create_db_2nf(db_path='ims_2nf.db'):
    # Remove existing database for a clean start
    if os.path.exists(db_path):
        os.remove(db_path) 

    # Open connection and start a transaction
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("BEGIN TRANSACTION;")

    # 1NF: atomic columns
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            eid     INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT NOT NULL,
            email   TEXT UNIQUE NOT NULL,
            gender  TEXT,
            contact TEXT,
            dob     TEXT,
            doj     TEXT,
            pass    TEXT,
            utype   TEXT,
            address TEXT,
            salary  TEXT
        );
    """)

    # Supplier table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS supplier (
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            contact     TEXT,
            description TEXT
        );
    """)

    # Category table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS category (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL UNIQUE
        );
    """)

    # Product table now references IDs -> 2NF
    cur.execute("""
        CREATE TABLE IF NOT EXISTS product (
            pid          INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id  INTEGER NOT NULL,
            supplier_id  INTEGER NOT NULL,
            name         TEXT NOT NULL,
            price        REAL,
            qty          INTEGER,
            status       TEXT,
            FOREIGN KEY(category_id) REFERENCES category(category_id),
            FOREIGN KEY(supplier_id) REFERENCES supplier(supplier_id)
        );
    """)

    # Commit the transaction to persist schema
    cur.execute("COMMIT;")
    con.close()


if __name__ == '__main__':
    create_db_2nf()  # initialize 2NF schema with transactional DDL


    
