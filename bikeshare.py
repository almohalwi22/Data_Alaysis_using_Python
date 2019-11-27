# This project will help you to improve your data analysis skills
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
    city = input("Please Enter one of these cities name: (chicago, new york city, washington): ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Please Enter the correct city name: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month =  input("Please Enter the month name: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Please Enter the correct month name: ").lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input("Please Enter the day name: ").lower()
    #while month not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        #month = input("Please Enter the correct month name").lower()
    
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract the month of the year
    df['month'] = df['Start Time'].dt.month
    
    # extract the day of the week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
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
    popular_month = df['month'].mode()[0]
    print("The most common month is: ", popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day is: ", popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common hour is: ", popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_StartStation = df['Start Station'].mode()[0]
    print("The most popular start station is: ", popular_StartStation)
    
    # TO DO: display most commonly used end station
    popular_EndStation = df['End Station'].mode()[0]
    print("The most popular end station is: ", popular_EndStation)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start&end Station'] = df['Start Station']+ " " + df['End Station']
    popular_Station = df['Start&end Station'].mode()[0]
    print("The most popular station is: ", popular_Station)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['Trip Duration'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    total_travel = str(df['Trip Duration'].sum())
    print('The total travel is: ', total_travel)

    # TO DO: display mean travel time
    average_travel = str(df['Trip Duration'].mean())
    print('The average travel is: ', average_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    num_userTypes = df['User Type'].value_counts()
    print("This shows the counts for each user type: ", num_userTypes)


    # TO DO: Display counts of gender
    try:    
        gender = df['Gender'].value_counts()
        print("This only shows the number of gender in cities of Chicago and New york city: ", gender)
    except:
        print("The city of wagshonton does not have information for gender")

    # TO DO: Display most common year 

    common_year = df['Birth Year'].mode()[0]
    print("The most common year is: ", int(common_year))
    
    # TO DO: Display earliest year of birth
    earliest_year = df['Birth Year'].min()
    print("The most earliest year is: ", int(earliest_year))
    
    # TO DO: Display recent year of birth
    recent_year = df['Birth Year'].max()
    print("The most recent year is: ", int(recent_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):

    start_data = 0
    end_data = 5

    start_display = input("Do you want to see the first five rows of the raw data?: ").lower()
    
    if start_display == "yes":
        while end_data <= df.shape[0]:
            
            print(df.iloc[start_data:end_data,:])
            
            start_data = start_data + 5
            end_data = end_data + 5

            end_display = input("Do you want to see more raw data?: ").lower()
            if end_display == 'no':
                break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()