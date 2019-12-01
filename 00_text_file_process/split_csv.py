import pandas as pd

for i,chunk in enumerate(pd.read_csv('path_to_your_csv_file', chunksize=100)):
    chunk.to_csv('chunk{}.csv'.format(i))
    
