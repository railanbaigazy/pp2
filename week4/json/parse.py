import json
from pathlib import Path

path = Path(__file__).with_name("sample-data.json")
data = json.loads(open(path, "r").read())["imdata"]

print("Interface Status")
print("=" * 100)
print("{:<60} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("{:<60} {:<20} {:<10} {:<10}".format("-" * 60, "-" * 20, "-" * 10, "-" * 7))

for object in data:
    attributes = object["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print("{:<60} {:<20} {:<10} {:<10}".format(dn, descr, speed, mtu))