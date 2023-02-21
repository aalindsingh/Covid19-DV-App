# Covid19-DV-App
Python application for data visualization on Covid 19 datasets.


The global pandemic caused by the virus SARS-CoV-2 imposed one of the most significant challenges our society faced in more than a hundred years. Millions of lives were lost, and the societal and economic impact will still reverberate for years to come, however, thanks to an unprecedent collaboration between researchers worldwide, we were able to develop several different vaccines using more than one type of technology, reducing the overall impact of this disease.

In this application, we will explore two different datasets, the first,  worldometer.csv, is a comma separate file containing the following columns:

Country/Region - this is the country for which the data is provided
Continent – Continent information with regards to a country
Population – The population of a specific country at that time;
Total Cases - The absolute number of cases in a particular country;
Total Deaths - The absolute number of deaths in a particular country;
Total Recovered - The absolute number of recovered patients in a particular country;
Active cases – Number of active patients in a particular country at the time the data was collected;
Serious/Critical - Number of serious/critical patients in a particular country at the time the data was collected;
Tot Cases/1M pop – Total number of cases divided by 1 million (normalised);
Deaths/1M pop - Total number of deaths divided by 1 million (normalised);
Total Tests - The absolute number of tests performed by a particular country;
Tests/1M pop - Total number of tests divided by 1 million (normalised);
 

The second, country_vaccinations.csv, is a comma separate file containing the following columns:

Country - this is the country for which the vaccination information is provided;
Country ISO Code - ISO code for the country;
Date - date for the data entry; for some of the dates we have only the daily vaccinations, for others, only the (cumulative) total;
Total number of vaccinations - this is the absolute number of total immunizations in the country;
Total number of people vaccinated - a person, depending on the immunization scheme, will receive one or more (typically 2) vaccines; at a certain moment, the number of vaccination might be larger than the number of people;
Total number of people fully vaccinated - this is the number of people that received the entire set of immunization according to the immunization scheme (typically 2); at a certain moment in time, there might be a certain number of people that received one vaccine and another number (smaller) of people that received all vaccines in the scheme;
Daily vaccinations (raw) - for a certain data entry, the number of vaccination for that date/country;
Daily vaccinations - for a certain data entry, the number of vaccination for that date/country;
Total vaccinations per hundred - ratio (in percent) between vaccination number and total population up to the date in the country;
Total number of people vaccinated per hundred - ratio (in percent) between population immunized and total population up to the date in the country;
Total number of people fully vaccinated per hundred - ratio (in percent) between population fully immunized and total population up to the date in the country;
Number of vaccinations per day - number of daily vaccination for that day and country;
Daily vaccinations per million - ratio (in ppm) between vaccination number and total population for the current date in the country;
Vaccines used in the country - total number of vaccines used in the country (up to date);
Source name - source of the information (national authority, international organization, local organization etc.);
Source website - website of the source of information;
 

Project Specification.

The objective of this project is to produce an application that allows the user to explore some of the most interesting aspects of these two Covid-19 datasets.
