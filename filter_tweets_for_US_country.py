import json
import sys
import pandas as pd

df = pd.read_csv('only_english_2.csv', index_col=0)
counter = 0

for index, row in df.iterrows():
    # Select Column with name "Place"
    value = str(row['place'])

    # Change Single Quotes to Double Quotes for JSON
    value = value.strip("'<>() ").replace("\'", '\"')
    counter += 1

    try:
        jsonified = json.loads(value)
        code = jsonified['country_code']

        # Remove all rows that are not Canada or United States
        if code == ('US') or code == ('CA'):
            print(code + " yes")
        else:
            df = df.drop(index)
    except:
        print(sys.exc_info())

    print(counter)
    
    
df.to_csv('filteredbyCountry2.csv')
