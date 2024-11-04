import csv
import ast
rows = []
with open('top_50_2023.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)

danceability = header.index('danceability')

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

sum_dance = 0
counter = 0
for row in rows:
    if is_float(row[danceability]):
        sum_dance += float(row[danceability])
        counter +=1
print(sum_dance / counter)



print(is_float('12.3'))
print(rows)
for row in rows:
    row[4] = ast.literal_eval(row[4])
print(rows)

GENRES = 4
genres_dict = {}
for row in rows:
    for genre in row[GENRES]:
        if genre in genres_dict:
            genres_dict[genre] += 1
        else:
            genres_dict[genre] = 1

# x = (key, value)
top_three = sorted(genres_dict.items(), key = lambda x: x[1], reverse=True)
print(top_three)

def sum_1(a, b):
    return a + b

sum_2 = lambda x, y: x + y
print(sum_2(1, 4))



total_liveliness = 0
count = 0
energy_index = header.index('energy')
liveliness_index = header.index('liveness')

for row in rows:
    energy = float(row[energy_index])
    liveliness = float(row[liveliness_index])
    if energy > 0.5:
        total_liveliness += liveliness
        count += 1
average_liveliness = total_liveliness / count
print(average_liveliness)



artist_counts = {}
artist_index = header.index('artist_name')
for row in rows:
    artist_name = row[artist_index]
    if artist_name in artist_counts:
        artist_counts[artist_name] += 1
    else:
        artist_counts[artist_name] = 1

max_count = 0
for count in artist_counts.values():
    if count > max_count:
        max_count = count

frequent_artists = []
for artist, count in artist_counts.items():
    if count == max_count:
        frequent_artists.append(artist)

for artist in frequent_artists:
    print(artist)




release_date_index = header.index('album_release_date')
year_count = {}
for row in rows:
    release_date = row[release_date_index]
    year = release_date.split('-')[0]

    if year in year_count:
        year_count[year] += 1
    else:
        year_count[year] = 1

max_year = None
max_count = 0

for year, count in year_count.items():
    if count > max_count:
        max_count = count
        max_year = year

print(f'{max_count} in {max_year}')




