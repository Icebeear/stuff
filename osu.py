import requests
import json

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="osu",
    user="postgres",
    password="12345",
    port=5432
)

cur = conn.cursor()

res = set()

key = "cedb7fcf648182733cfed8f3b78eb53c4ddb0663"

print("Adding maps..")
for year in range(2012, 2024):
    for month in range(1, 13):
        for day in range(1, 32, 2):
            head = {
                "k": key,
                "m": 0,
                "since": f"{year}-{month}-{day} 00:00:01",
            }

            response = requests.get(url="https://osu.ppy.sh/api/get_beatmaps", params=head)
            
            data = response.text

            json_data = json.loads(data)

            try:
                for beatmap in json_data:
                    if (180 <= float(beatmap["bpm"]) <= 200) \
                    and (float(beatmap["genre_id"]) == 11) \
                    and (float(beatmap["total_length"]) >= 120) \
                    and (float(beatmap["approved"]) in (1, 2, 3, 4)) \
                    and (float(beatmap["difficultyrating"]) >= 5.3) \
                    and (float(beatmap["diff_approach"]) >= 9):
                        link = f"https://osu.ppy.sh/beatmapsets/{beatmap['beatmapset_id']}#osu/{beatmap['beatmap_id']}"
                        if link not in res:
                            res.add(link)
                            title = beatmap["title"]
                            difficulty = float(beatmap["difficultyrating"])
                            ar = float(beatmap["diff_approach"])
                            bpm = float(beatmap["bpm"])
                            
                            cur.execute("INSERT INTO maps (title, url, difficulty, ar, bmp, genre) VALUES (%s, %s, %s, %s, %s, %s)", (title, link, difficulty, ar, bpm, 'metal'))
                            conn.commit()
            except:
                pass

print("Complete")
cur.close()
conn.close()

# print(f"Total maps: {len(res)}")
# print("---------------------")
# for beatmap in res:
#     print(beatmap)

    # with open('data.txt', 'w') as f:
    #     f.write(beatmap)


