# load all files from a folder
files = [file for file in os.listdir('../data_raw')]
combined = pd.DataFrame()

for file in files:
    delimiter = ',' if file != 'x.csv' else ';'
    current_df = pd.read_csv('../data_raw/' + file, delimiter=delimiter)
    combined = pd.concat([combined, current_df])
combined

# sort out nan's
new_df = data_df[data_df.isna().any(axis=1)]
df.dropna(how='all')

# convert to int
df['col'] = pd.to_numeric(df['col'])

# run function on df
def get_city(address):
  return address.split(',')[1]
df['col'].apply(lambda addr: get_city(addr))

# python f strings
df.apply(lambda addr: f"{get_city(addr)} xy")

# plot labeling
plt.xticks(df['x'].unique(), rotation='vertical', size=8)