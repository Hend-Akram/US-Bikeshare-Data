import time
import pandas as pd
import numpy as np
import statistics

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

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
    print('would you like to see data for Chicago, New_yourk_city or Washington? ')
    city = input().lower()

    while (city != 'new_yourk_city' and city !='chicago'and city !='washington')  :
      print('Please Enter one of this three cities chicago , new_yourk_city or washinton')
      city = input().lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    print ('Please enter the month you want to analyze in lyrics [january, february, march, april, may, june].')
    month = input().lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    while month == 'all':
        break

    while (month not in ['january', 'february', 'march', 'april', 'may', 'june'] and month!='all' ):
        print('please Enter one of this values [january, february, march, april, may, june]')
        month = input().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Please enter the day of week  you want to analyze in lyrics [ monday, tuesday, ... sunday].')
    day = input()
    while day == 'all':
        break

    while (day not in ['monday', 'tuesday', ' wednesday',' thursday',' friday','saturday' ,'sunday'] and day !='all' ):
        print('please Enter one of this values [ monday, tuesday, ... sunday]')
        day = input().lower()

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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day

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

    print (df)
    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.month
    popular_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return ('the most popular month is {} , the most popular day is {} and the most popular hour is {}'.format(popular_month , popular_day ,popular_hour))

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popStartStation = df['Start Station'].value_counts().head(1)
    # TO DO: display most commonly used end station
    popEndStation = df['End Station'].value_counts().head(1)

    # TO DO: display most frequent combination of start station and end station trip
    comStartEnd = (df['Start Station'] + df['End Station']).value_counts().head(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('\nThe most commonly used start station is {}'.format(popStartStation))
    print('\nThe most commonly used End station is {}'.format(popEndStation))
    print('\nThe most frequent combination of start station and end station trip is {} '.format(comStartEnd))

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal travel time is \n{}'.format(df['Trip Duration']))

    # TO DO: display mean travel time
    print('\nMean travel time is {}'.format(statistics.mean(df['Trip Duration'])))

    print('Summation of all trip duration is {}'.format(df['Trip Duration'].sum()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Users_type = df['User Type'].value_counts()
    print('\nCounts of user types\n{}'.format(Users_type))

    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('Ooops gender and birth Year data are not available for washington !')

    else:
        Users_gender = df['Gender'].value_counts()
        print('\nCounts of gender\n{}'.format(Users_gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        most_old = df['Birth Year'].sort_values(ascending=True).head(1)
        print('\nthe earliest year of birth\n{}'.format(most_old))
        most_recent = df['Birth Year'].sort_values(ascending=False).head(1)
        print('\nthe most recent year of birth is\n{} '.format(most_recent))
        most_common = df['Birth Year'].value_counts().head(1)
        print(most_common)

        def display_data():
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
            start_loc = 0
            while (view_data == 'yes'):
                print(df.iloc[start_loc])
                start_loc += 5
                view_display = input('Do you wish to continue?: ').lower()


        display_data()
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)



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

#c=list(get_filters())
#load_data(c[0], c[1], c[2])
#load_data('chicago','february','monday')
# b = pd.DataFrame(load_data(c[0], c[1], c[2]))
# print(time_stats(b))
#df = pd.read_csv(CITY_DATA['chicago'])
# c=list(df)
#time_stats(df)
#station_stats(df)
#trip_duration_stats(df)
#user_stats(df)
#get_filters()
#print('washington'in CITY_DATA)

