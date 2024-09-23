import psycopg2
from psycopg2 import sql
from contract import Sales
import streamlit as st
from dotenv import load_dotenv
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

load_dotenv()

DB_HOST = getenv("DB_HOST")
DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}",
    poolclass=NullPool
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def save_to_postgres(sales: Sales):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        cursor = conn.cursor()

        cursor.execute(
            sql.SQL("INSERT INTO sales (email, date, hour, value, quantity, product) VALUES (%s, %s, %s, %s, %s, %s)")
            .format(
                sql.Identifier("email"),
                sql.Identifier("date"),
                sql.Identifier("hour"),
                sql.Identifier("value"),
                sql.Identifier("quantity"),
                sql.Identifier("product")
            ),
            (
                sales.email,
                sales.date,
                sales.hour,
                sales.value,
                sales.quantity,
                sales.product
            )
        )

        conn.commit()
        cursor.close()
        conn.close()
        st.success("Saved to database!")

    except Exception as e:
        st.error(f"Error saving to database: {e}")