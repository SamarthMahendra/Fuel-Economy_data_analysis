import pandas as pd
from sqlalchemy import create_engine, Table, Column, MetaData, String, Integer, Float
from sqlalchemy import inspect


# Load the data from CSV
df = pd.read_csv('vehicles.csv')

# Define your database connection details
db_url = 'postgresql://samarthmahendra:@localhost:5432/machinelearning'  # Adjust based on your DB

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Define table name
table_name = 'vehicles'

# Create metadata object
metadata = MetaData()

# Dynamically create columns based on the DataFrame
columns = []
for column_name, dtype in df.dtypes.items():
    if pd.api.types.is_integer_dtype(dtype):
        column_type = Integer
    elif pd.api.types.is_float_dtype(dtype):
        column_type = Float
    else:
        column_type = String
    columns.append(Column(column_name, column_type))

# Create table dynamically
table = Table(table_name, metadata, *columns)

# Create an inspector to check if the table exists
inspector = inspect(engine)

# Drop table if it exists (for re-running the script)
if inspector.has_table(table_name):
    table.drop(engine)

# Create the table in the database
metadata.create_all(engine)

# Dump data into the table
df.to_sql(table_name, engine, if_exists='append', index=False)

print(f"Data from DataFrame has been uploaded to the {table_name} table.")