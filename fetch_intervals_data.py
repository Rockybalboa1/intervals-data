import os
import requests, json, datetime

api_key = os.getenv("INTERVALS_API_KEY")
athlete_id = os.getenv("ATHLETE_ID")

# ensure numeric only
athlete_id = athlete_id.replace("i", "")  

# use repo root from GitHub Actions
workspace = os.getenv("GITHUB_WORKSPACE")
output_path = os.path.join(workspace, "activities.json")

since = (datetime.date.today() - datetime.timedelta(days=60)).isoformat()
url = f"https://intervals.icu/api/v1/athlete/{athlete_id}/activities?oldest={since}"

print("Using workspace:", workspace)
print("Fetching activities since", since)

headers = {"Authorization": f"Bearer {api_key}"}
resp = requests.get(url, headers=headers)

if resp.status_code != 200:
    print("❌ Failed:", resp.status_code, resp.text)
    resp.raise_for_status()

activities = resp.json()

with open(output_path, "w") as f:
    json.dump(activities, f, indent=2)

print(f"Saved {len(activities)} activities to:", output_path)
