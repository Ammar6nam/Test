city=input('Enter the name of the city: ')
population=input('Enter the number of population: ')
co1=city.isalpha()
co2=population.isnumeric()
if city.isalpha() and population.isnumeric():
    print(f'City:{city}',f'({co1})')
    print(f'population: {population}')
else:
    print('There is an Error in your input! ')