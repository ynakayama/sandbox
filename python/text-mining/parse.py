from bs4 import BeautifulSoup
import sys
import re
import glob
import pandas as pd

def parse_html(filename):
    path = glob.glob('./' + filename)

    for p in path:

        name = p.replace('.html','').replace('./html\\','')
        html = open(p,'r',encoding="utf-8_sig")
        soup = BeautifulSoup(html,"html.parser")

        tr = soup.find_all('tr')
        columns = [i.text.replace('\n','') for i in tr[0].find_all('th')]

        df = pd.DataFrame(index=[],columns=columns[1:])

        for l in tr[1:]:
            lines = [i.text for i in l.find_all('td')]
            lines = [i.replace('\n','') if n != 6 else re.sub(r'[\n]+', ",", i)  for n,i in enumerate(lines)]
            lines = pd.Series(lines, index=df.columns)
            df = df.append(lines,ignore_index=True)

        df.to_csv('./'+name+'.csv', encoding='utf_8_sig', index=False)

def main():
    if len(sys.argv) != 2:
        print("Usage: parse.py html")
        sys.exit(1)

    parse_html(sys.argv[1])

if __name__ == '__main__':
    main()
