"""****************************************************************************

	Authors: 		Andrew Anderson
	Date Made: 		03/22/2023
	Date Modified:	03/22/2023
	Purpose:		Implementing a bunch of statistical calculations that I've
                    needed over the course of my research.

*****************************************************************************"""
import math

"""****************************************************************************
    Method name:    mean
    Method purpose: Calculates the average (mean) of an array of numbers,
                    defined by the sum of the array, divided by the length of
                    the array.
	Method Input:   An array of numbers (named array)
	Method Output:  The average of the array, a scalar value.
****************************************************************************"""
def mean( array ):
	return sum(array)/len(array)




"""****************************************************************************
    Method name:    variance
    Method purpose: Calculates the variance of an array of numbers, defined by
                    (1/(n-1))*sum( ( x_i - avg( array ) )^2 )
	Method Input:   An array of numbers (named array)
	Method Output:  The variance of the array, a scalar value.
****************************************************************************"""
def variance( array ):
	average = mean( array )
	var = 0
	for num in array:
		var += math.pow((num - average), 2)
	return var / ( len( array ) - 1)





"""****************************************************************************
    Method name:    pooled_variance
    Method purpose: Calculates the pooled variance of two arrays of numbers.
                    If there are n_1 numbers in the first array (N) and n_2 
                    numbers in the second array (M), the definition is:
		    
                        n_1*var( N ) + n_2*var( M )
                        ---------------------------
                                n_1 + n_2
				
	Method Input:   Two arrays of numbers, first_array and second_array
	Method Output:  The pooled variance of the arrays, a scalar value.
****************************************************************************"""
def pooled_variance( first_array, second_array):
	numerator = (len(first_array) - 1)*variance(first_array) + ( len(second_array) - 1)*variance(second_array)
	denominator = len(first_array) + len(second_array) - 2
	return numerator / denominator







"""****************************************************************************
    Method name:    cohens_d_between
    Method purpose: Calculates the practical significance value for the
                    distance between two means.				
	Method Input:   Two arrays of numbers, first_array & second_array
	Method Output:  Cohen's d, a scalar representation of the practical
                    significance between two averages.
****************************************************************************"""
def cohens_d_between( first_array, second_array ):
	avg_1 = mean( first_array )
	avg_2 = mean( second_array )
	pooled_var = pooled_variance( first_array, second_array )
	return float( abs( avg_1 - avg_2 ) / math.sqrt( pooled_var ) )







"""****************************************************************************
    Method name:    standard_error
    Method purpose: Calculates the standard error between two arrays.		
	Method Input:   Two arrays of numbers, first_array & second_array
	Method Output:  The standard error between the two arrays, a scalar.
****************************************************************************"""
def standard_error( first_array, second_array):
	pooled_var = pooled_variance( first_array, second_array )
	return math.sqrt( (pooled_var/len(first_array ) ) + (pooled_var / len( second_array ) ) )







"""****************************************************************************
    Method name:    two_sample_t_stat
    Method purpose: Calculates the t statistic for two averages
	Method Input:   Two arrays of numbers, first_array & second_array
	Method Output:  The standard error between the two arrays, a scalar.
****************************************************************************"""
def two_sample_t_stat( first_array, second_array ):
	avg_1 = mean( first_array )
	avg_2 = mean( second_array )
	mean_distance = abs( avg_1 - avg_2 )
	std_error = standard_error( first_array, second_array )
	return mean_distance / std_error





"""****************************************************************************
    Method name:    two_sample_degrees_freedom
    Method purpose: Calculates the degrees of freedom between two independent
                    samples.
	Method Input:   Two arrays of numbers, first_array & second_array
	Method Output:  The degrees of freedom (df) for the statistical test, a 
                    scalar.
****************************************************************************"""
def two_sample_degrees_freedom( first_array, second_array ):
	return len(first_array) + len(second_array) - 2