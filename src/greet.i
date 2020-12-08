/* File: greet.i adapted from 'SWIG for the truly lazy'@http://www.swig.org/tutorial.html */
%module greet

%{
#define SWIG_FILE_WITH_INIT
#include "greet.h"
%}

%include <std_string.i>
%include "greet.h"                      
