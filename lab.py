#lab 11 from csc 201
 
# import pandas and re libraries to use pandas dataframes and regex patterns
import pandas as pd, re

# func name: read_as_dataframe
# arguments: 1 strings representing the file path and name
# return: 1 pandas dataframe
# description: reads the data in a csv file as a pandas dataframe
def read_as_dataframe(filename):
    df = pd.read_csv(filename)
    
    return df

# func name: visually_inspect
# arguments: 1 pandas dataframe
# return: 1 pandas dataframe
# description: visually inspects dataframe for common data problems
def visually_inspect(df):
    # info() --> get data type of each column and additional info in the dataframe
    print(df.info())
    print('\n\n\n')
    
    
    # value_counts(dropna = False) --> look for how many NaN values (missing or blank) are in the Movie column
    print(df['Movie'].value_counts(dropna = False))
    print('\n\n\n')
    
    
    # describe() --> only returns columns in the dataframe that have a numerical type (integer, float)
    print(df.describe())
    print('\n\n\n')
    
    
    # isnull() --> see if there are any missing values and at what index number in the dataframe
    #              shown by locating the the index numbers on the left side wherever you see True in
    #              ANY of the columns in the dataframe
    print(df.isnull())
    print('\n\n\n')
    
    # return nothing because we are only visually inspecting the data
    return

# func name: main
# arguments: none
# return: none
# description: setups up the program by reading the csv data into a pandas dataframe and
#              running functions to visually inspect and clean the data

# func name: clean_movie_column
# arguments: 1 pandas dataframe
# return: none
# description: cleans the data errors in the Movie column
def clean_movie_column(df):
    # create a subset of the dataframe containing only the data with missing values
    # in the Movie column
    missing_subset = df[(df['Movie'].isnull())]
    
    # print the subset containing only missing values in the Movie column
    # TYPE YOUR CODE HERE
    print(missing_subset)
    
    
    print('\n\n\n')
    
    
    # drop the row with the missing data in the Movie column by replacing X with the
    # index number of this row
    # note: use argument inplace and set to True so the changes are saved in the dataframe
    df.drop(df.index[13], inplace = True)
    
    # print the dataframe to make sure it dropped the row with the missing data
    print(df)
    
    print('\n\n\n')
    # drop the duplicate row in the Movie column (i.e., Lion King duplicate should be dropped)
    # note: use argument inplace and set to True so the changes are saved in the dataframe 
    df.drop_duplicates(inplace = True)
    
    
    # look for how many NaN values (missing or blank) are in the Movie column now
    # to make sure there are no NaN values and that Lion King only has one count
    # hint: look back at how you did this in the visually_inspect function
    print(df['Movie'].value_counts(dropna=False))
    print('\n\n\n')
    
    
    # reset the index number of the dataframe 
    df.reset_index(drop = True, inplace = True)
    
    print(df)
    
    
    print('\n\n\n')
    
    
    # return nothing
    return


# func name: clean_year_column
# arguments: 1 pandas dataframe
# return: none
# description: cleans the data errors in the Year column
def clean_year_column(df):
   
    # print the Year column to examine the data errors in it     
    print(df['Year'])
    print('\n\n\n')
    
    # remove the values with commas in the Year column by replacing ',' with ''
    #df['Year'] = df['Year'].str.replace(',','')
    
    # print the Year column to make sure that commas have been removed
    #print(df['Year'])
    
    
    print('\n\n\n')
    
    
    # use regex pattern to only include 4 numbers (removes the extra 0 after some values in this cell)
    #pattern = re.compile('\d{4}')
    
    # apply this pattern to all values in the Year column
    # follow with [0] to only get the string of each value (no list or [] around each year)
    #df['Year'] = df['Year'].apply(lambda x : re.findall(pattern, x)[0])
    # print the Year column to check that all values are correct
    # TYPE YOUR CODE HERE
    
    
    print('\n\n\n')
    
    # convert all values in the Year column to the appropriate numerical type
    #df['Year'] = pd.to_numeric(df['Year'])
    
    # print the Year column to check that all values are correct
    # TYPE YOUR CODE HERE
    
    
    print('\n\n\n')
    
    
    # return nothing
    return


def main():
    # specify the location and name of the csv file with the disney movie data 
    file = 'disney_movies.csv'
    
    # read in csv data as dataframe and store the returned pandas dataframe in variable called df
    df = read_as_dataframe(file)
    
    # call function to visually inspect the dataframe for data errors
    visually_inspect(df)
    
    clean_movie_column(df)
    
    clean_year_column(df)
    
# call the main function to run the program
main()# import pandas and re libraries to use pandas dataframes and regex patterns
import pandas as pd, re

# func name: read_as_dataframe
# arguments: 1 strings representing the file path and name
# return: 1 pandas dataframe
# description: reads the data in a csv file as a pandas dataframe
def read_as_dataframe(filename):
    df = pd.read_csv(filename)
    
    return df

# func name: visually_inspect
# arguments: 1 pandas dataframe
# return: 1 pandas dataframe
# description: visually inspects dataframe for common data problems
def visually_inspect(df):
    # info() --> get data type of each column and additional info in the dataframe
    print(df.info())
    print('\n\n\n')
    
    
    # value_counts(dropna = False) --> look for how many NaN values (missing or blank) are in the Movie column
    print(df['Movie'].value_counts(dropna = False))
    print('\n\n\n')
    
    
    # describe() --> only returns columns in the dataframe that have a numerical type (integer, float)
    print(df.describe())
    print('\n\n\n')
    
    
    # isnull() --> see if there are any missing values and at what index number in the dataframe
    #              shown by locating the the index numbers on the left side wherever you see True in
    #              ANY of the columns in the dataframe
    print(df.isnull())
    print('\n\n\n')
    
    # return nothing because we are only visually inspecting the data
    return

# func name: main
# arguments: none
# return: none
# description: setups up the program by reading the csv data into a pandas dataframe and
#              running functions to visually inspect and clean the data

# func name: clean_movie_column
# arguments: 1 pandas dataframe
# return: none
# description: cleans the data errors in the Movie column
def clean_movie_column(df):
    # create a subset of the dataframe containing only the data with missing values
    # in the Movie column
    missing_subset = df[(df['Movie'].isnull())]
    
    # print the subset containing only missing values in the Movie column
    # TYPE YOUR CODE HERE
    print(missing_subset)
    
    
    print('\n\n\n')
    
    
    # drop the row with the missing data in the Movie column by replacing X with the
    # index number of this row
    # note: use argument inplace and set to True so the changes are saved in the dataframe
    df.drop(df.index[13], inplace = True)
    
    # print the dataframe to make sure it dropped the row with the missing data
    print(df)
    
    print('\n\n\n')
    # drop the duplicate row in the Movie column (i.e., Lion King duplicate should be dropped)
    # note: use argument inplace and set to True so the changes are saved in the dataframe 
    df.drop_duplicates(inplace = True)
    
    
    # look for how many NaN values (missing or blank) are in the Movie column now
    # to make sure there are no NaN values and that Lion King only has one count
    # hint: look back at how you did this in the visually_inspect function
    print(df['Movie'].value_counts(dropna=False))
    print('\n\n\n')
    
    
    # reset the index number of the dataframe 
    df.reset_index(drop = True, inplace = True)
    
    print(df)
    
    
    print('\n\n\n')
    
    
    # return nothing
    return


# func name: clean_year_column
# arguments: 1 pandas dataframe
# return: none
# description: cleans the data errors in the Year column
def clean_year_column(df):
   
    # print the Year column to examine the data errors in it     
    print(df['Year'])
    print('\n\n\n')
    
    # remove the values with commas in the Year column by replacing ',' with ''
    df['Year'] = df['Year'].str.replace(',','')
    
    # print the Year column to make sure that commas have been removed
    print(df['Year'])
    
    
    print('\n\n\n')
    
    
    # use regex pattern to only include 4 numbers (removes the extra 0 after some values in this cell)
    pattern = re.compile('\d{4}')
    
    # apply this pattern to all values in the Year column
    # follow with [0] to only get the string of each value (no list or [] around each year)
    df['Year'] = df['Year'].apply(lambda x : re.findall(pattern, x)[0])
    # print the Year column to check that all values are correct
    print(df['Year'])
    
    
    print('\n\n\n')
    
    # convert all values in the Year column to the appropriate numerical type
    df['Year'] = pd.to_numeric(df['Year'])
    
    # print the Year column to check that all values are correct
    print(df['Year'])
    
    
    print('\n\n\n')
    
    
    # return nothing
    return


# func name: clean_mpaa_column
# arguments: 1 pandas dataframe
# return: none
# description: cleans the data errors in the MPAA Rating column
def clean_mpaa_column(df):
    
    # print the MPAA Rating column to examine the data errors in it
    print(df['MPAA Rating'])
    
     
    print('\n\n\n')
    
    
    # find and replace all instances of General Audiences with G
    # TYPE YOUR CODE HERE
    df['MPAA Rating'] = df['MPAA Rating'].str.replace('General Audiences','G')
    
    # find and replace all instances of Parental Guidance Suggested with PG
    # TYPE YOUR CODE HERE
    df['MPAA Rating'] = df['MPAA Rating'].str.replace('Parental Guidance Suggested','PG')
    
    # print the MPAA Rating column to check that all values are correct
    # TYPE YOUR CODE HERE
    print(df['MPAA Rating'])
     
    print('\n\n\n')
    
    # return nothing
    return


def main():
    # specify the location and name of the csv file with the disney movie data 
    file = 'disney_movies.csv'
    
    # read in csv data as dataframe and store the returned pandas dataframe in variable called df
    df = read_as_dataframe(file)
    
    # call function to visually inspect the dataframe for data errors
    visually_inspect(df)
    
    clean_movie_column(df)
    
    clean_year_column(df)
    
    clean_mpaa_column(df)
    
# call the main function to run the program
main()