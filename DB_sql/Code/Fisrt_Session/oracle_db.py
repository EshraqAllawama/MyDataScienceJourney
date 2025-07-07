
from sqlalchemy import create_engine, text
import cx_Oracle

# Replace with your actual credentials
# http://shosho:5562/isqlplus
USERNAME = "scott"
PASSWORD = "a1842003"

HOST = "localhost"  # Change if connecting to a remote database
PORT = "5562"       # Default Oracle port
SERVICE_NAME = "shosho" # Change according to your Oracle DB

# Create the engine
engine = create_engine(f"oracle+cx_oracle://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{SERVICE_NAME}")

# Test the connection
with engine.connect() as connection:
    result = connection.execute(text('SELECT sysdate FROM dual'))
    print(result.fetchone())
