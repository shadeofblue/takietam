import datetime
import json
import requests

EVENTS_ENDPOINT = "http://145.239.69.80:16655/events"
ACTIVITIES_ENDPOINT = "http://145.239.69.80:16655/activities"

resp = requests.get(EVENTS_ENDPOINT)
events = json.loads(resp.content)

resp = requests.get(ACTIVITIES_ENDPOINT)
activities = json.loads(resp.content)


def process_event(event):
    event["date"] = datetime.datetime.fromisoformat(f"{event['date'][:-1]}+00:00")
    return event


def process_activity(activity):
    activity["start"] = datetime.datetime.fromisoformat(f"{activity['start'][:-1]}+00:00")
    activity["end"] = datetime.datetime.fromisoformat(f"{activity['end'][:-1]}+00:00")
    activity["events"] = list()
    return activity


events = sorted(map(process_event, events["events"]), key=lambda e: e["date"])
activities = sorted(map(process_activity, activities["activities"]), key=lambda a: a["start"])
orphaned = list()

for e in events:
    cnt = 0
    for a in activities:
        if a["start"] <= e["date"] <= a["end"]:
            a["events"].append(e)
            cnt += 1
    if not cnt:
        orphaned.append(e)


def process_activity_back(activity):
    activity["start"] = activity["start"].isoformat()
    activity["end"] = activity["end"].isoformat()
    for e in activity["events"]:
        if isinstance(e["date"], datetime.datetime):
            e["date"] = e["date"].isoformat()
    return activity


for e in orphaned:
    e["date"] = e["date"].isoformat()

out = {
    "activities": [process_activity_back(a) for a in activities if a["events"]],
    "orphaned": orphaned,
}

print(json.dumps(out, indent=2))
