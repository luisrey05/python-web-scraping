import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver



driver = webdriver.Chrome()
driver.get('http://oxylabs.io/blog')
results = []
other_results= []
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll(attrs='css-bnfvmw ez2v0aa1'):
    name = a.find('a')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='css-1ozkpwn e9shfhl0'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)
print(results)
print(other_results)
df = pd.DataFrame({'Names': results, 'Dates':other_results })
df.to_csv('names.csv', index=False, encoding='utf-8')



