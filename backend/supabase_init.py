import json
from supabase import create_client, Client

with open("config.json") as config_file:
    config = json.load(config_file)

supabase_url: str = config["SUPABASE_URL"]
supabase_key: str = config["SUPABASE_KEY"]

supabase: Client = create_client(supabase_url, supabase_key)
print("Supabase initialized successfully:", supabase)