import requests, json, datetime, os

api_key = os.getenv("INTERVALS_API_KEY")
athlete_id = os.getenv("ATHLETE_ID")
headers = {"Authorization": f"Basic {api_key}"}

# Get last 60 days of activities
since = (datetime.date.today() - datetime.timedelta(days=60)).isoformat()
url = f"https://intervals.icu/api/v1/athlete/{athlete_id}/activities?oldest={since}"

print("Fetching activities since", since)
resp = requests.get(url, headers=headers)
resp.raise_for_status()
activities = resp.json()

with open("activities.json", "w") as f:
    json.dump(activities, f, indent=2)

print(f"Saved {len(activities)} activities to activities.json")
