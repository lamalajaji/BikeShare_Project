import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
  
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input( '\nWould you like to see data for Chicago, New Yor, or Washington?)\n') 
    
    cities_list = ['chicago','new york','washington']
    months_list = ['all','january','february','march','april','may', 'june']
    days_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    while city in cities_list == 'false':
        print('invalid input! , please enter the city again')

        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('please enter month from janury to june or type "all" ')
    while month in months_list == 'false':



        print('invalid input! , please enter a month again')



        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)



    day = print(input('please enter a day or type "all" for all days'))

    while day in days_list == 'false':

        print('invalid input! please enter a day again')




    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
   """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    
# filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1  
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
      
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    freq_mon = df['month'].mode()
    print('most common month is : ',freq_mon,'\n')

    
    # TO DO: display the most common day of week
    freq_day = df['day'].mode()
    print ('most common day is : ',freq_day,'\n')

    
    # TO DO: display the most common start hour
    freq_hour = df['hour'].mode()
    print ("most common hour is : ",freq_hour,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    # TO DO: display most commonly used start station
   
    print("most common Start Station is: ",df['Start Station'].mode())

    
    # TO DO: display most commonly used end station
   
    print("most common End Station is: ",df['End Station'].mode())

    
    # TO DO: display most frequent combination of start station and end station trip
    co_station = (df['Start Station']==df['End Station']).mode()
    print('most frequent combination of start station and end station trip is : ',co_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    # TO DO: display total travel time
   
    print('the total of travel time is : 'df['Trip Duration'].count())

    
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('the average of travel time is : ',avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('the count of user types is : ',user_types,'\n')
    
   

    # TO DO: Display counts of gender
    # note : only NYC and chicago have a 'Gender' in their data
    while city == 'chicago' or city == 'new york':
        df['Gender'].dropna()
        gender_count = df['Gender'].value_counts()
        print('counts of gender is :',gender_count,'\n')
        
        
        
  
    # TO DO: Display earliest, most recent, and most common year of birth
    # note : only NYC and chicago have a 'Birth year' in their data
    while city == 'chicago' or city == 'new york':
        df['Birth Year'].dropna()
        min_db = df['Birth Year'].min()
        print('the earliest year of birth is : ',min_bd,'\n')
        max_db  = df['Birth Year'].max()
        print('the most recent year of birth is : ',max_bd,'\n')
        freq_bd = df['Birth Year'].mode()
        print('the most frequent year of birth is : ',freq_bd,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break 
      
    
if __name__ == "__main__":
	main()