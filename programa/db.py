
import psycopg2
from base import DB_CONFIG

def conectar_bd():
    """Establece una conexión con la base de datos PostgreSQL."""
    return psycopg2.connect(**DB_CONFIG)
