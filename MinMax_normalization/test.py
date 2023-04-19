import pandas as pd

data = [["10,Calzone,13,Large,Tomato sauce, mozzarella, ham, mushrooms, peppers"]]
df = pd.DataFrame(data, columns=['id,Name,Price,Size,Toppings'])


print(df)
# existing_df = pd.read_csv('menu.csv')
# df = existing_df.append(df, ignore_index=True)
#
# df.to_csv('menu.csv', index=False)
