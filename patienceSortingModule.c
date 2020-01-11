#include <Python.h>
#include <math.h>

// ******************************** ** Headers ** ********************************

int patience_sort_c(double * lst, int len);
double * add_to_arr_c(double * arr, int arr_len, int occupied_len, double val);


// ************************* ** Wrappers (for Python) ** *************************

/**
This Function is called from a Python program and calls the patience_sort_c func
Input: args contains a Python list object
*/
static PyObject * patience_sort(PyObject * self, PyObject * args)
{
	PyObject * py_lst;
	PyObject * obj;

	if (! PyArg_ParseTuple(args, "O", &py_lst)) {
        printf("%s\n", "Error - error while parsing");
        return NULL;
    }

	if (!PyList_Check(py_lst)) {
		printf("%s\n", "Error - PyObject is not a list");
		return NULL; //error
	}
	
	int len = PyList_Size(py_lst);
	double lst[len];

	for (int i=0; i<len; i++) {
		if (!(obj = PyList_GetItem(py_lst, i))) {
			printf("%s\n", "Error - failed to get item from the list");
			return NULL;
		}

		if (!PyFloat_Check(obj)) {
			printf("%s\n", "Error - list item is not a float");
			return NULL;
		}

		if (!(lst[i] = (double)PyFloat_AsDouble(obj))) {
			printf("%s\n", "Error - failed to convert list item to long");
			return NULL;
		}
	}

	return Py_BuildValue("i", patience_sort_c(lst, len));
}


static PyMethodDef myMethods[] = {
	{"patience_sort", (PyCFunction)patience_sort, METH_VARARGS, "patience sort algorithm function"},
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef patience_sort_alg = {
	PyModuleDef_HEAD_INIT,
	"patience_sort_alg",
	"patience sort algorithm module",
	-1, 
	myMethods
};

PyMODINIT_FUNC PyInit_patience_sort_alg(void) {
	return PyModule_Create(&patience_sort_alg);
}


// ***************************** ** Functions (C) ** *****************************

// add val to the dynamic arr (increase arr size if needed). 
// returns new arr pointer
double * add_to_arr_c(double * arr, int arr_len, int val_position, double val) {

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


int patience_sort_c(double * lst, int lst_len) {
    
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

    	stacks_arr = add_to_arr_c(stacks_arr, stacks_len, j, lst[i]);

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

