from my_secrets import get_my_accounts, get_other_accounts, get_korea_accounts
import pandas as pd
import sqlite3

my_accounts = get_my_accounts()
other_accounts = get_other_accounts()
korea_accounts = get_korea_accounts()
total_accounts = my_accounts + other_accounts + korea_accounts

data = {'user_id': list(range(1,len(total_accounts) + 1)),
        'account_name': total_accounts}

df = pd.DataFrame(data)

# Creating the SQLite Table and connecting to it and populating the database
conn = sqlite3.connect('league_stats.db')
c = conn.cursor()

#c.execute('''DROP TABLE users''')
#c.execute('''CREATE TABLE users(user_id int, account_name text)''')

df.to_sql('users', conn, if_exists='append', index=False)

my_df = pd.read_sql('''SELECT * FROM users''', conn)
my_df = my_df.drop_duplicates()
pd.set_option('display.max_rows', None)
print(my_df)
