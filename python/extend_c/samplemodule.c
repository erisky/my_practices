#include <Python.h> // including stdio.h/stdlib.h/errno.h/string.h


/*
 * Object 
 * */
static PyObject *
sample_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    /* get the input */
    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    printf("Call to %s\n", command);
    sts = system(command);
    return PyLong_FromLong(sts);
}


static PyMethodDef SpamMethods[] = {
    {"system",  sample_system, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


/*
 * Module definitions 
 * */
static struct PyModuleDef samplemodule = {
   PyModuleDef_HEAD_INIT,
   "sample",   /* name of module */
   "doc of this sample module", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   SpamMethods
};

PyMODINIT_FUNC
PyInit_sample(void)
{
    return PyModule_Create(&samplemodule);
}

