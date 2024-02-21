import json
print("Interface Status\n================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
with open("some_sample.json", "r") as file:
    json_str = file.read()
a = json.loads(json_str)
interfaces = a.get('imdata', [])
for item in interfaces:
    l1physif = item.get('l1PhysIf', {})
    attributes = l1physif.get('attributes', {})
    dn = attributes.get('dn', '')
    description = attributes.get('descr', 'inherit')
    speed = attributes.get('speed', '')
    mtu = attributes.get('mtu', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
