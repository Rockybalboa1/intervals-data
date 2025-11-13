import base64
import requests, json, datetime, os

api_key = os.getenv("INTERVALS_API_KEY")
athlete_id = "358634"

token = base64.b64encode(f":{api_key}".encode()).decode()
headers = {"Authorization": f"Basic {token}"}

since = (datetime.date.today() - datetime.timedelta(days=60)).isoformat()
url = f"https://intervals.icu/api/v1/athlete/{athlete_id}/activities?oldest={since}"

resp = requests.get(url, headers=headers)
resp.raise_for_status()
activities = resp.json()
with open("activities.json", "w") as f:
    json.dump(activities, f, indent=2)
