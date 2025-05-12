from dotenv import load_dotenv
import os
load_dotenv()

api = os.getenv("API_KEY")
token = os.getenv("TOKEN")
print(api)
print(token)
