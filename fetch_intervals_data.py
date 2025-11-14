import requests

athlete_id = "<358634>"
api_key = "<734t12g78z7vam8upqt713rf9>"

url = f"https://intervals.icu/api/v1/athlete/{athlete_id}"

r = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
print(r.status_code, r.text)
