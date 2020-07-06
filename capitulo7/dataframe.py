# you can add all the values column by column and then use Pandas 
# to create the dataframe 
# make sure you import pandas library

# first create the values manually column by column, you don't need to use quotes around numbers
# unless you want to capture them as a string

import pandas as pd 

cars = {'brand': ['Honda', 'Toyota', 'Ford', 'Audi'],
        'price': [22000, 25000, 23000, 40000]    
       }

df = pd.DataFrame(cars, columns = ['brand', 'price']) 

print(df)

# great! 
# notice how the table has a column on the left with an index.
# you can add your own index if you'd like

df2 = pd.DataFrame(cars, columns = ['brand','price'], index=['Car_1','Car_2','Car_3','Car_4'])

print (df2)
