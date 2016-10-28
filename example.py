records = [{"name":"Jones"}, {"name":"Walter"}, {"name":"Dude"}]

names = []
for record in records:
    name = record["name"]
    print(name)

    names.append(name)

print ("names: " + str(names))