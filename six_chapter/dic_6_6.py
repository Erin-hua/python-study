favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
survey_peoples = ['jen', 'erin', 'phil', 'wang']
for people in survey_peoples:
    if people in favorite_languages.keys():
        print('Welcome, ' + people.title() + '!')
    else:
        print(people.title() + ", we invite you for a survey.")
