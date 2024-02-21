import requests 


# response = requests.get('https://ru.wikipedia.org')

# if response.status_code == 200:
#     print('Success')
# else:
#     print('Page not found')

# print(response.headers['data'])

# with open('page.html', 'x', encoding = 'utf-8') as file:
#     file.write(response.text)
# print(response.text)

cat_responce = requests.get('https://catfact.ninja/fact')

fact = cat_responce.json()
facts = []
for i in range(10):
    facts += fact['fact']

print(facts)

with open('Lessons/Lesson50/page_facts.txt', 'x', encoding='utf-8'):
    pass