host = "pg-1176ee36-bundedatta-b8b4.i.aivencloud.com"
port = 16998
username = "avnadmin"
password = "AVNS_6ZkEkDkvs8wDyMPBxac"
database = "defaultdb"
schema = "dev"

DATABASE_URL= f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}?sslmode=require"