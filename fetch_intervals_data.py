import requests, json, datetime, os

api_key = os.getenv("INTERVALS_API_KEY")
athlete_id = "358634"  # numeric only
headers = {"Authorization": f"Bearer {api_key}"}

since = (datetime.date.today() - datetime.timedelta(days=60)).isoformat()
url = f"https://intervals.icu/api/v1/athlete/athlete_id/activities?oldest={since}"

print("Fetching activities since", since)
resp = requests.get(url, headers=headers)

if resp.status_code != 200:
    print("❌ Failed to fetch data:", resp.status_code, resp.text)
else:
    activities = resp.json()
    with open("activities.json", "w") as f:
        json.dump(activities, f, indent=2)
    print(f"Saved {len(activities)} activities to activities.json")
