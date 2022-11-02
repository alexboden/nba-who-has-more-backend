import os, json
# import django
# print(os.getcwd())
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nba.settings")
# django.setup()
# from question.models import Player

os.chdir('/Users/boden/docs/gh/nba/json_data')
list_of_json = os.listdir()

# for cur in list_of_json:
os.chdir('/Users/boden/docs/nba-site/nba/question/json_data_correct')
list_of_json = os.listdir()
for x in list_of_json:
    player_data = json.load(open(x))
    p = Player()
    p.name = x[:-5]
    p.data = player_data
    p.save()

# for x in list_of_json:
#     text = open(x).read()
#     text = text.replace('NaN', '0')
#     os.chdir('/Users/boden/docs/nba-site/nba/question/json_data_correct')
#     open(x[:-5] + ".json", 'w').write(text)
#     os.chdir('/Users/boden/docs/gh/nba/json_data')

# list_of_json = os.listdir()
# for x in list_of_json:
#     if "zero" in x:
#         os.remove(x)