import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['All','January','February','March',
          'April','May','June']

days = ['Monday','Tuesday','Wednesday','Thursday',
        'Friday','Saturday','Sunday','All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data from chicago, new york city, or washington? \n")
    city = city.lower()
    while(city not in CITY_DATA.keys()):
        city = input("Oops! your input is not there. Try different city ..\n")
        city = city.lower()

    # get user input for month (all, january, february, ... , june)
    month = input("\n\nWhich month? january, february, march, april, may, june or all of them? \n")
    month = month.title()
    while(month not in months):
        month = input("Oops! your input is not there. Try different month ..\n")
        month = month.title()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\n\nWhich day of the week? or do you want them all \n")
    day = day.title()
    while(day not in days):
        day = input("Oops! your input is not there. Try different day ..\n")
        day = day.title()

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
    df['day_of_week'] = df['Start Time'].dt.weekday

    if month != 'All':
        month = months.index(month)
        df = df[df['month'] == month]

    if day != 'All':
        day = days.index(day)
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print("\nMost common month is:   ", months[common_month])

    # display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday
    common_day = df['day_of_week'].mode()[0]
    print("\nMost common day is:   ", days[common_day])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("\nMost common hour is:   ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("\nMost common start station is:   ", common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nMost common end station is:   ", common_end_station)

    # display most frequent combination of start station and end station trip
    common_both_stations = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print("\nMost common trip is:   ", common_both_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("\nThe total travel time is:   ", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("\nThe mean travel time is:    ", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if 'User Type' in df.columns:
        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print("\nThe count of user types is:\n", user_types)
    else:
        print("\nUser type information are not available in this city\n")

    if 'Gender' in df.columns:
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print("\nThe count of genders is:\n", gender)
    else:
        print("\nGender information are not available in this city\n")

    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print("\nThe earliest birth is {}\nThe recent birth is {}\nThe most common birth is {}".format(int(earliest_birth),
        int(recent_birth), int(common_birth)))
    else:
        print("\nBirth year information are not available in this city\n")


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
        print(df)
        
        i = 0
        while True:
            raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
            if raw_data.lower() != 'yes':
                break
            print(df.iloc[i+0:i+5])
            i += 5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
