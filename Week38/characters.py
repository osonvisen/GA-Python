characters = [
    {
        "name": "John",
        "age": 34,
        "job": "Engineer"
    },
    {
        "name": "Jane",
        "age": 28,
        "job": "Hair dresser"
    }
]

for character in characters:
    name = character.get("name")
    print(name)

# John,34,Engineer
# with open("characters.txt", "w", encoding="utf-8") as file:
#    for character in characters:
#        file.write(f"{character.get("name")},{character.get('age')},{character.get('job')}\n")

with open("characters.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(",")
        age = parts[1]
        job = parts[2]
        print(f"{parts[0]}, {age}, {job}")

