
def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                id, name, age = line.split(",")
                cats.append({"id": id, "name": name, "age": age.strip()})
        return cats
    except Exception as e:
        print(f"Ooops: {e}")

cats_info = get_cats_info("cats.txt")
print(cats_info)
