import census2010

print(census2010.all_data['AK']['Anchorage'])
anchorage_pop = census2010.all_data['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was ' + str(anchorage_pop))
