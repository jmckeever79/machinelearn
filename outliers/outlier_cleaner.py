#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    from math import pow

    z = zip(predictions, ages, net_worths)

    first = z[0]

    cleaned_data = [(x[1][0],x[2][0],pow(x[2][0]-x[0][0],2)) for x in z]

    k = lambda x : x[2]
    cleaned_data = sorted(cleaned_data, key=k)

    l = len(cleaned_data)
    x = int(.9 * l)
    temp = cleaned_data[:x]


    ### your code goes here

    
    return temp

