import json

data = '''{
    "cities": [
        {"name":"Kochi","main":{"temp":31.5,"humidity":78}},
        {"name":"Delhi","main":{"temp":36.2,"humidity":45}},
        {"name":"Mumbai","main":{"temp":33,"humidity":70}},
        {"name":"Bengaluru","main":{"temp":27.4,"humidity":60}}
    ]
}'''

weather = json.loads(data)

rows = []
for c in weather["cities"]:
    rows.append([c["name"], c["main"]["temp"], c["main"]["humidity"]])

print("City       Temp    Humidity")
for r in rows:
    print(r[0], r[1], r[2])

temps = [r[1] for r in rows]
hum = [r[2] for r in rows]

print("\nTotal Cities:", len(rows))
print("Average Temperature:", sum(temps)/len(temps))
print("Average Humidity:", sum(hum)/len(hum))
print("Hottest City:", max(rows, key=lambda x:x[1])[0])
print("Coldest City:", min(rows, key=lambda x:x[1])[0])