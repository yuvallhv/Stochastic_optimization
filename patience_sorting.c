#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

double * add_to_arr(double * arr, int arr_len, int occupied_len, double val);
int patience_sort(double * lst, int len);

int main(int argc, char **argv) {
    
    double arr[10] = {7.0,2.0,8.0,1.0,3.0,4.0,10.0,6.0,9.0,5.0};
    patience_sort(arr, 10);
    
    return 0;
}


// add val to the dynamic arr (increase arr size if needed). 
// returns new arr pointer
double * add_to_arr(double * arr, int arr_len, int val_position, double val) {

	// there is a need to increase the array size by 2
	if (arr_len == val_position) {
		double * new_arr = (double *)calloc(arr_len * 2, sizeof(double));

		// copy arr to new arr
		for (int i=0; i<arr_len; i++) {
			new_arr[i] = arr[i];
		}

		// add val to the new arr
		new_arr[arr_len] = val;

		// fill the rest of the arr with -1
		for (int i=arr_len+1; i<2*arr_len; i++) {
			new_arr[i] = -1;
		}

		free(arr);
		return new_arr;
	}

	// arr is big enough
	else {
		arr[val_position] = val;
		return arr;
	}

}


int patience_sort(double * lst, int lst_len) {
    
    int estimated_size = 2 * (int)(sqrt(lst_len));
    estimated_size += (int)(sqrt(estimated_size));

    // the stacks array saves only the top card of each stack
    // initialized with -1 and estimated size (E(no. of stacks) + a little more)
    double * stacks_arr = (double *)calloc(estimated_size, sizeof(double));

    // this varialbe will change dynamically
    int stacks_len = estimated_size;

    for (int i=0; i<stacks_len; i++) {
    	stacks_arr[i] = -1;
    }

    // go through lst, each card put on the appropriate stack 
    // (by the patience sortinf algorithm)
    int subsequence_len = 0;
    for (int i = 0; i < lst_len; ++i)
    {
    	int j = 0;
    	while ((j < stacks_len) && (stacks_arr[j] != -1) && (stacks_arr[j] < lst[i])) {
    		j++;
    	}

    	stacks_arr = add_to_arr(stacks_arr, stacks_len, j, lst[i]);

    	if (stacks_len == j) {
    		stacks_len *= 2;	
    	}

    	// update subsequnce length
    	if (j > subsequence_len) {
    		subsequence_len = j;
    	}
    }

    subsequence_len++; 
    
    free(stacks_arr);
    return subsequence_len;

}


