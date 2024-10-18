from langchain import Agent
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
import sqlite3
import pandas as pd

# Function to query the database
def query_database(query):
    conn = sqlite3.connect('example.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Define the LangChain agent
class DatabaseAgent(Agent):
    def __init__(self):
        super().__init__()

    def run(self, query):
        # Execute the query
        results = query_database(query)
        
        # Parse the results
        parsed_output = results.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
        return parsed_output

# Instantiate the agent
agent = DatabaseAgent()

# Define a SQL query
sql_query = "SELECT * FROM users"

# Run the agent
output = agent.run(sql_query)
print(output)
