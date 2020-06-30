def tallest_people(**people):
    max_height = max(people.values())
    for key, value in sorted(people.items()):
        if value == max_height:
            print(f"{key} : {value}")


# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)
