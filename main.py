from dotenv import load_dotenv
import os

from pinecone import Pinecone, ServerlessSpec




## Error Handling for API key retreival
try: 
            
    load_dotenv()

    PC_KEY = os.getenv('PINECONE_API_KEY')
    print(PC_KEY)

    if not PC_KEY:
        raise ValueError("PINECONE_API_KEY not found in .env file")


except Exception as e:
    print(f"Error: {e}")

pc = Pinecone(api_key=PC_KEY)

