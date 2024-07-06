
import os

config = {
    'DATABASE_URL': os.getenv('DATABASE_URL', 'postgresql+psycopg2://chungdinh:18102005@localhost:5432')
}