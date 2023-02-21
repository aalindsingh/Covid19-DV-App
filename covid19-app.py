# Author - Alind Singh
# %%
import pandas as pd                                 #import all the required libraries like panda, matplotlib, tkinter
import matplotlib.pyplot as plt
import tkinter as tk
worldometer_df = pd.read_csv("C:/Users/ALIND SINGH/OneDrive/Desktop/Msc DS&DA/python/Datasets_Project/worldometer_data.csv", encoding = "latin-1") 
country_df = pd.read_csv("C:/Users/ALIND SINGH/OneDrive/Desktop/Msc DS&DA/python/Datasets_Project/country_vaccinations.csv", encoding = "latin-1")
#Load both the datasets in separate variables as data frames for further analysis
def totalCasesPlot():
    print("Please enter one of the following continent name:-")
    continent_list = worldometer_df.Continent.dropna().unique().tolist() #storing unique continent names
    continent_list.sort()
    print(continent_list)
    while(True):
        cont_name = input("Enter continent name: ")
        caps_cont_name = ''
        if ' ' in cont_name:                             #Capitalize continents with space in the name
            split_str = cont_name.split(' ')
            split_str[0] = split_str[0].capitalize()
            split_str[1] = split_str[1].capitalize()
            caps_cont_name = ' '.join(split_str)
        elif '/' in cont_name:                           #Capitalize continents with '/' in the name
            split_str = cont_name.split('/')
            split_str[0] = split_str[0].capitalize()
            split_str[1] = split_str[1].capitalize()
            caps_cont_name = '/'.join(split_str)        
        else:                                            #Capitalize continents with one word names
            caps_cont_name = cont_name.capitalize()    
        if(cont_name in continent_list or caps_cont_name in continent_list):
            cont_name = caps_cont_name
            break
        else:
            print("Please enter correct continent name!")
    print(f"Following is the stacked barplot for {cont_name}:")    
    totalData = worldometer_df[worldometer_df.Continent == cont_name]
    plt.figure(figsize=(12,5), dpi=80)                               #Prepare the stacked bar plot
    plt.bar(totalData['Country/Region'], totalData['TotalCases'], color = 'red')
    plt.bar(totalData['Country/Region'], totalData['TotalRecovered'], bottom=totalData['TotalCases'], color = 'blue')
    plt.bar(totalData['Country/Region'], totalData['TotalDeaths'], bottom=totalData['TotalCases']+totalData['TotalRecovered'], color = 'green') 
    plt.xlabel('Countries', fontsize=14)                                    
    plt.ylabel('Data Summary', fontsize=14)
    plt.legend(['TotalCases','TotalRecovered','TotalDeaths'],loc=1)
    plt.title(f"Covid case study for {cont_name}", fontsize=14)
    plt.xticks(rotation=75)
    plt.show()                                                  #Display the plot prepared for the selected continent
    total_cases = totalData['TotalCases']
    countries = totalData['Country/Region']
    max_cases = total_cases.idxmax()
    min_cases = total_cases.idxmin()
    print(countries[max_cases],total_cases[max_cases],"with max cases.")       #Display country with max cases
    print(countries[min_cases],total_cases[min_cases],"with min cases.")       #Display country with min cases

totalCasesPlot()

# %%
import seaborn as sns            #import seaborn library for plotting lm graph
def relationShipPlot():
    print("Please enter one of the following continent name:-")
    continent_list = worldometer_df.Continent.dropna().unique().tolist() 
    continent_list.sort()
    print(continent_list)
    while(True):
        cont_name = input("Enter continent name: ")
        caps_cont_name = ''
        if ' ' in cont_name:                                  #same as function above
            split_str = cont_name.split(' ')
            split_str[0] = split_str[0].capitalize()
            split_str[1] = split_str[1].capitalize()
            caps_cont_name = ' '.join(split_str)
        elif '/' in cont_name:
            split_str = cont_name.split('/')
            split_str[0] = split_str[0].capitalize()
            split_str[1] = split_str[1].capitalize()
            caps_cont_name = '/'.join(split_str)        
        else:
            caps_cont_name = cont_name.capitalize()
        if(cont_name in continent_list or caps_cont_name in continent_list):
            cont_name = caps_cont_name
            break
        else:
            print("Please enter correct continent name!")
    print(f"Following is the lmplot for {cont_name}:") 
    newData = worldometer_df[worldometer_df.Continent == cont_name]
    sns.lmplot(x ='TotalRecovered', y ='TotalDeaths', data = newData)          #Display the lmplot prepared for the selected continent

relationShipPlot()    

# %%
def continentBarPlot():
    numOfEntries = worldometer_df.groupby('Continent').size()
    numOfTests = worldometer_df.groupby('Continent')['Tests/1M pop'].sum()
    numOfCountries = worldometer_df.groupby('Continent')['Country/Region'].nunique()
    normalizedData = numOfTests / numOfCountries      #Normalizing data
    print('Following is the bar plot for continents:')
    normalizedData.plot.bar()                         #Prepare and display bar plot for all the continents
    plt.title('Number of tests/1M per continent')
    plt.xlabel('Continents')
    plt.xticks(rotation = 70)
    plt.ylabel('No. of tests')

continentBarPlot()    

# %%
def linePlotForCountry():
    print("Please enter one of the following country name:-")
    country_list = ['Ireland','United States','India','Brazil','Japan','Australia']
    print(country_list)
    while(True):
        country_name = input("Enter country name: ")
        caps_country_name = ''
        if ' ' in country_name:
            split_str = country_name.split(' ')
            split_str[0] = split_str[0].capitalize()
            split_str[1] = split_str[1].capitalize()
            caps_country_name = ' '.join(split_str)
        else:
            caps_country_name = country_name.capitalize()    
        if(country_name in country_list or caps_country_name in country_list):
            country_name = caps_country_name
            break
        else:
            print("Please enter correct country name!")
    print(f"Following is the lineplot for {country_name}:") 
    newData = country_df[country_df.country == country_name]
    sns.lineplot(x ='date', y ='daily_vaccinations', data = newData)    #Display the prepared line plot for the selected country

linePlotForCountry()             

# %%
def main():
    print("Welcome to our analysis Pipeline for COVID-19 data!!!")                    #Displaying all the options to the user 
    print("Please, select one of the following options:")                             #available in the application
    print("1) Display cases per country in a specific continent.")
    print("2) Calculate the Recovered and Death percentages per country in a specific continent.")
    print("3) Display number of tests per continent.")
    print("4) Display the daily vaccinations of a specific country.")
    print("5) Exit.")

    choice = int(input("What is your choice of operation? "))      #User input for the choice in the options mentioned above
    if(choice == 1):
        totalCasesPlot()                                           #function call for stacked bar plot
    elif(choice == 2):
        relationShipPlot()                                         #function call for lmplot
    elif(choice == 3):
        continentBarPlot()                                         #function call for bar plot
    elif(choice == 4):
        linePlotForCountry()                                       #function call for line plot
    elif(choice == 5):
        print("Thank You!! Goodbye.")
        exit()                                                     #Exiting and qutting the program with thank you message

main()                            #driver function call for the main application

# %%
