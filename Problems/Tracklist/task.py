# tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
#                       "On the Other Side": "Samara"},
#           "Cure": {"Disintegration": "Lovesong",
#                    "Wish": "Friday I'm in love",
#                    "Seventeen Seconds": "A Forest"}}


def tracklist(**kwargs):
    for key, value in kwargs.items():
        print(key)
        for key_inner, value_inner in value.items():
            print(f"ALBUM: {key_inner} TRACK: {value_inner}")


# tracklist(**tracks)
