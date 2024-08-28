
import os
import bcrypt

secret = bcrypt.gensalt()

config = {
    'DATABASE_URL': os.getenv('DATABASE_URL', 'postgresql+psycopg2://chungdinh:18102005@localhost:5432'),
    'BCRYPT_SECRET': os.getenv('BCRYPT_SECRET', bcrypt.gensalt())
}