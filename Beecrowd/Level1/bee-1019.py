duration = int(input())

hours = int(duration / 60 / 60)
minutes = int((duration / 60) - (hours * 60))
seconds = int(duration - (hours * 60 * 60) - (minutes * 60))

print(f'{hours}:{minutes}:{seconds}')

# Time Conversion
# https://www.beecrowd.com.br/judge/en/problems/view/1019