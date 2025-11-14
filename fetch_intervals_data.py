import os
import requests
import json
import datetime

api_key = os.getenv("INTERVALS_API_KEY")
athlete_id = os.getenv("ATHLETE_ID")

# Ensure numeric (remove i-prefix if it exists)
athlete_id = athlete_id.lstrip("i")

since = (datetime.date.today() - datetime.timedelta(days=60)).isoformat()
url = f"https://intervals.icu/api/v1/athlete/{athlete_id}/activities?oldest={since}"

print("Requesting:", url)

resp = requests.get(
    url,
    auth=(athlete_id, api_key)   # <-- THIS is the correct Intervals API login
)

if resp.status_code != 200:
    print("❌ Failed:", resp.status_code, resp.text)
    resp.raise_for_status()

activities = resp.json()

output_path = os.path.join(os.getenv("GITHUB_WORKSPACE"), "activities.json")

with open(output_path, "w") as f:
    json.dump(activities, f, indent=2)

print(f"Saved {len(activities)} activities to:", output_path)
