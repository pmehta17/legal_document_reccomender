from dotenv import load_dotenv
import os

from pinecone import Pinecone, ServerlessSpec


class PineconeConnector:

    def __init__(self, PC_KEY):
        try:

            load_dotenv()
            self.PC_KEY = os.getenv('PINECONE_API_KEY')

            if not self.PC_KEY:
                raise ValueError("PINECONE_API_KEY not found in .env file")
            
            self.pc = Pinecone(api_key=self.PC_KEY)

            print("Pinecone client initialized successfully.")
       
        except Exception as e:
            print(f"Error initializing Pinecone client: {e}")
            self.pc = None

    ## Embedding model is [BERT large model (uncased)], which outputs vectors of [1024] dimensions
    ## Cosine similarity so search is not skewed by magnitude
    def create_index(index_name):
        if index_name not in pc.list_indexes().names():
            pc.create_index(
                name=index_name,
                dimension=1024,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud='aws', 
                    region='us-east-1'
                ) 
            ) 
        else: 
            print(f'Error: Could not create index. Index with name "{index_name}" already exists. ')

    
