import requests, json, datetime, os, sys

api_key = os.getenv("INTERVALS_API_KEY")
athlete_id = os.getenv("ATHLETE_ID")

if not api_key:
    sys.exit("❌ Missing INTERVALS_API_KEY environment variable.")
if not athlete_id:
    sys.exit("❌ Missing ATHLETE_ID environment variable.")

headers = {"Authorization": f"Basic {api_key}"}
since = (datetime.date.today() - datetime.timedelta(days=60)).isoformat()
url = f"https://intervals.icu/api/v1/athlete/{athlete_id}/activities?oldest={since}"

print(f"Fetching activities since {since} for athlete {athlete_id}")
resp = requests.get(url, headers=headers)
print(f"Response code: {resp.status_code}")

if resp.status_code != 200:
    print("Response text:", resp.text)
    sys.exit("❌ Failed to fetch data. Check API key and athlete ID permissions.")

activities = resp.json()
print(f"✅ Fetched {len(activities)} activities")

with open("activities.json", "w") as f:
    json.dump(activities, f, indent=2)

print("💾 Saved activities.json")
