from pandas import read_csv, concat


def clean_currency(x):
    '''converting each value in price field to float'''
    if isinstance(x, str):
        return x.replace('$', '')
    return x

# merging 3 csv files into 1
df = concat(map(read_csv, [
    'data\daily_sales_data_0.csv',
    'data\daily_sales_data_1.csv',
    'data\daily_sales_data_2.csv']))

# removing the dollar sign out of the price column
df['sales'] = df.quantity * df.price.apply(clean_currency).astype('float')

# viewing only data associated with the pink morsel line
pink_morsel = df[df['product'] == 'pink morsel']

# droping unneccessary columns
pink_morsel.drop(df.columns[[0, 1, 2]], inplace=True, axis=1)

# reordering the columns
pink_morsel = pink_morsel.reindex(columns=['sales', 'date', 'region'])

# exporting to csv
pink_morsel.to_csv(r"E:\Quantium\quantium-starter\data\final.csv", index=False)

print(pink_morsel)