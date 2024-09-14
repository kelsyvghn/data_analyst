#a) The manager requests a code that will identify which consecutive months contribute towards the highest sales
#and then use that info to create targeted ads for the months before and after. To do this we would want to look at all
#the months, and take the average, this will be our base_median which we will use to compare each value against. If a value
# is higher than this we know it's above average and may be one of our top months. Values below this average will be the months likely
# to be targeted for the advertising. We should go through the data in two loops to first determine an average, and then
# determine which months are below or above this value. We keep track of the highest and lowest months, to determine which
# months to advertise.
# The code will need to store each high earning months in an array and return these.
#


earnings = {
    "Jan":	100,
    "Feb":	113,
    "Mar":	110,
    "Apr":	85,
    "May":	81,
    "Jun":	101,
    "Jul":	94,
    "Aug":	106,
    "Sep":	105,
    "Oct":	102,
    "Nov":	86,
    "Dec":	63 }

def target_months(dataset):

    months_total = 0
    median_value = 0
    bottom_months = []
    top_months = []

    for month in dataset:
        months_total += dataset[month]
        median_value = months_total / len(dataset)
        #print(median_value)

    for month in dataset:

        if dataset[month] < median_value-1:
            bottom_months.append(month)

            #print(bottom_months)
        if dataset[month] > median_value:

            top_months.append(month)

    print('these months are the top performers: ', top_months,'these months are the bottom performers: ', bottom_months)
    return top_months, bottom_months


# c) since we run two loops in our code, the complexity of this function is 2 O(N), because we are looking directly at
# one month at a time, going through all months in each loop. There are no nested loops, however, which keeps our time
# complexity lower.


print(target_months(earnings))

# d) limitations to this function are if the dataset has one extraordinarily high or low month, which alters the average
# and make all months either higher or lower, it will only return one or two outliers, which may be relatively low earning
# months, but not compared to the one extraordinary outlier. Other limitations are that the code may find months that are
# higher or lower than the median, but are not consecutive to months in the same category and this 'stand alone' as low or
# high respectively.
