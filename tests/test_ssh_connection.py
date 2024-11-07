# test_connect.py

import os
from dotenv import load_dotenv
from vanna.base import VannaBase

# Load environment variables from .env file
load_dotenv()

class TestVanna(VannaBase):
    def add_ddl(self, ddl): pass
    def add_documentation(self, documentation): pass
    def add_question_sql(self, question, sql): pass
    def assistant_message(self, message): pass
    def generate_embedding(self, text): pass
    def get_related_ddl(self, question): pass
    def get_related_documentation(self, question): pass
    def get_similar_question_sql(self, question): pass
    def get_training_data(self): pass
    def remove_training_data(self, training_id): pass
    def submit_prompt(self, prompt): pass
    def system_message(self, message): pass
    def user_message(self, message): pass

def test_mysql_connection():
    vn = TestVanna(config={})
    
    # Retrieve configuration from environment variables
    host = os.getenv('DB_HOST')
    dbname = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    port = int(os.getenv('DB_PORT', 3306))  # Default to 3306 if not provided
    use_ssh_tunnel = os.getenv('USE_SSH_TUNNEL', 'False').lower() == 'true'
    ssh_host = os.getenv('SSH_HOST')
    ssh_user = os.getenv('SSH_USER')
    pem_path = os.getenv('SSH_PEM_PATH')
    
    # Connect to MySQL with optional SSH tunnel
    vn.connect_to_mysql(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port,
        use_ssh_tunnel=use_ssh_tunnel,
        ssh_host=ssh_host,
        ssh_user=ssh_user,
        pem_path=pem_path
    )
    
    # Example SQL command
    df = vn.run_sql("SELECT * FROM card_transactions LIMIT 10;")
    print(df)

if __name__ == "__main__":
    test_mysql_connection()
