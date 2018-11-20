/* Generated code for Python source for module 'PyPse.parser'
 * created by Nuitka version 0.6.0.6
 *
 * This code is in part copyright 2018 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "__helpers.h"

/* The _module_PyPse$parser is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_PyPse$parser;
PyDictObject *moduledict_PyPse$parser;

/* The module constants used, if any. */
static PyObject *const_dict_5ad418cbcefcc35faafb0546f0413c37;
static PyObject *const_tuple_str_plain_file_str_plain_file_text_str_plain_tree_tuple;
static PyObject *const_str_digest_cf929a79ea3bfc426949a12e1cc6d691;
extern PyObject *const_str_plain___file__;
extern PyObject *const_str_plain___cached__;
extern PyObject *const_str_plain_parse_file_to_token;
extern PyObject *const_str_plain_tree;
extern PyObject *const_int_0;
extern PyObject *const_str_plain_lark;
static PyObject *const_str_digest_7f9c9eea1f41db3e6074404eca987729;
static PyObject *const_tuple_str_digest_83bce1bac4082b0fcde264be3cc4c001_tuple;
extern PyObject *const_tuple_str_plain_Lark_tuple;
extern PyObject *const_str_plain_parse;
static PyObject *const_str_plain_pse_parser;
static PyObject *const_str_digest_83bce1bac4082b0fcde264be3cc4c001;
static PyObject *const_str_plain_file_text;
extern PyObject *const_str_plain_blocks;
extern PyObject *const_tuple_empty;
static PyObject *const_str_digest_67f6a5b95450101e1a1522e82b8fa0b6;
extern PyObject *const_str_plain_read;
extern PyObject *const_str_plain_start;
extern PyObject *const_str_plain_file;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_Lark;
static PyObject *module_filename_obj;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_dict_5ad418cbcefcc35faafb0546f0413c37 = _PyDict_NewPresized( 1 );
    PyDict_SetItem( const_dict_5ad418cbcefcc35faafb0546f0413c37, const_str_plain_start, const_str_plain_blocks );
    assert( PyDict_Size( const_dict_5ad418cbcefcc35faafb0546f0413c37 ) == 1 );
    const_tuple_str_plain_file_str_plain_file_text_str_plain_tree_tuple = PyTuple_New( 3 );
    PyTuple_SET_ITEM( const_tuple_str_plain_file_str_plain_file_text_str_plain_tree_tuple, 0, const_str_plain_file ); Py_INCREF( const_str_plain_file );
    const_str_plain_file_text = UNSTREAM_STRING( &constant_bin[ 4422 ], 9, 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_file_str_plain_file_text_str_plain_tree_tuple, 1, const_str_plain_file_text ); Py_INCREF( const_str_plain_file_text );
    PyTuple_SET_ITEM( const_tuple_str_plain_file_str_plain_file_text_str_plain_tree_tuple, 2, const_str_plain_tree ); Py_INCREF( const_str_plain_tree );
    const_str_digest_cf929a79ea3bfc426949a12e1cc6d691 = UNSTREAM_STRING( &constant_bin[ 4431 ], 50, 0 );
    const_str_digest_7f9c9eea1f41db3e6074404eca987729 = UNSTREAM_STRING( &constant_bin[ 4481 ], 21, 0 );
    const_tuple_str_digest_83bce1bac4082b0fcde264be3cc4c001_tuple = PyTuple_New( 1 );
    const_str_digest_83bce1bac4082b0fcde264be3cc4c001 = UNSTREAM_STRING( &constant_bin[ 4502 ], 3247, 0 );
    PyTuple_SET_ITEM( const_tuple_str_digest_83bce1bac4082b0fcde264be3cc4c001_tuple, 0, const_str_digest_83bce1bac4082b0fcde264be3cc4c001 ); Py_INCREF( const_str_digest_83bce1bac4082b0fcde264be3cc4c001 );
    const_str_plain_pse_parser = UNSTREAM_STRING( &constant_bin[ 7749 ], 10, 1 );
    const_str_digest_67f6a5b95450101e1a1522e82b8fa0b6 = UNSTREAM_STRING( &constant_bin[ 4489 ], 12, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_PyPse$parser( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_61b21cafc25f22bbfbab06c21a1b6112;
static PyCodeObject *codeobj_2452f2af5cef26a75daa30fe34de1399;

static void createModuleCodeObjects(void)
{
    module_filename_obj = const_str_digest_cf929a79ea3bfc426949a12e1cc6d691;
    codeobj_61b21cafc25f22bbfbab06c21a1b6112 = MAKE_CODEOBJ( module_filename_obj, const_str_digest_7f9c9eea1f41db3e6074404eca987729, 1, const_tuple_empty, 0, 0, CO_NOFREE );
    codeobj_2452f2af5cef26a75daa30fe34de1399 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_parse_file_to_token, 119, const_tuple_str_plain_file_str_plain_file_text_str_plain_tree_tuple, 1, 0, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
}

// The module function declarations.
static PyObject *MAKE_FUNCTION_PyPse$parser$$$function_1_parse_file_to_token(  );


// The module function definitions.
static PyObject *impl_PyPse$parser$$$function_1_parse_file_to_token( struct Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_file = python_pars[ 0 ];
    PyObject *var_file_text = NULL;
    PyObject *var_tree = NULL;
    struct Nuitka_FrameObject *frame_2452f2af5cef26a75daa30fe34de1399;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_2452f2af5cef26a75daa30fe34de1399 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function code.
    {
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_2452f2af5cef26a75daa30fe34de1399, codeobj_2452f2af5cef26a75daa30fe34de1399, module_PyPse$parser, sizeof(void *)+sizeof(void *)+sizeof(void *) );
    frame_2452f2af5cef26a75daa30fe34de1399 = cache_frame_2452f2af5cef26a75daa30fe34de1399;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_2452f2af5cef26a75daa30fe34de1399 );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert( Py_REFCNT( frame_2452f2af5cef26a75daa30fe34de1399 ) == 2 ); // Frame stack

    // Framed code:
    {
    PyObject *tmp_assign_source_1;
    PyObject *tmp_called_instance_1;
    CHECK_OBJECT( par_file );
    tmp_called_instance_1 = par_file;
    frame_2452f2af5cef26a75daa30fe34de1399->m_frame.f_lineno = 120;
    tmp_assign_source_1 = CALL_METHOD_NO_ARGS( tmp_called_instance_1, const_str_plain_read );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 120;
        type_description_1 = "ooo";
        goto frame_exception_exit_1;
    }
    assert( var_file_text == NULL );
    var_file_text = tmp_assign_source_1;

    }
    {
    PyObject *tmp_assign_source_2;
    PyObject *tmp_called_name_1;
    PyObject *tmp_source_name_1;
    PyObject *tmp_mvar_value_1;
    PyObject *tmp_args_element_name_1;
    tmp_mvar_value_1 = GET_STRING_DICT_VALUE( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain_pse_parser );

    if (unlikely( tmp_mvar_value_1 == NULL ))
    {
        tmp_mvar_value_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_pse_parser );
    }

    if ( tmp_mvar_value_1 == NULL )
    {

        exception_type = PyExc_NameError;
        Py_INCREF( exception_type );
        exception_value = PyUnicode_FromFormat( "name '%s' is not defined", "pse_parser" );
        exception_tb = NULL;
        NORMALIZE_EXCEPTION( &exception_type, &exception_value, &exception_tb );
        CHAIN_EXCEPTION( exception_value );

        exception_lineno = 121;
        type_description_1 = "ooo";
        goto frame_exception_exit_1;
    }

    tmp_source_name_1 = tmp_mvar_value_1;
    tmp_called_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_parse );
    if ( tmp_called_name_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 121;
        type_description_1 = "ooo";
        goto frame_exception_exit_1;
    }
    if ( var_file_text == NULL )
    {
        Py_DECREF( tmp_called_name_1 );
        exception_type = PyExc_UnboundLocalError;
        Py_INCREF( exception_type );
        exception_value = PyUnicode_FromFormat( "local variable '%s' referenced before assignment", "file_text" );
        exception_tb = NULL;
        NORMALIZE_EXCEPTION( &exception_type, &exception_value, &exception_tb );
        CHAIN_EXCEPTION( exception_value );

        exception_lineno = 121;
        type_description_1 = "ooo";
        goto frame_exception_exit_1;
    }

    tmp_args_element_name_1 = var_file_text;
    frame_2452f2af5cef26a75daa30fe34de1399->m_frame.f_lineno = 121;
    {
        PyObject *call_args[] = { tmp_args_element_name_1 };
        tmp_assign_source_2 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
    }

    Py_DECREF( tmp_called_name_1 );
    if ( tmp_assign_source_2 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 121;
        type_description_1 = "ooo";
        goto frame_exception_exit_1;
    }
    assert( var_tree == NULL );
    var_tree = tmp_assign_source_2;

    }

#if 0
    RESTORE_FRAME_EXCEPTION( frame_2452f2af5cef26a75daa30fe34de1399 );
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION( frame_2452f2af5cef26a75daa30fe34de1399 );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_2452f2af5cef26a75daa30fe34de1399, exception_lineno );
    }
    else if ( exception_tb->tb_frame != &frame_2452f2af5cef26a75daa30fe34de1399->m_frame )
    {
        exception_tb = ADD_TRACEBACK( exception_tb, frame_2452f2af5cef26a75daa30fe34de1399, exception_lineno );
    }

    // Attachs locals to frame if any.
    Nuitka_Frame_AttachLocals(
        (struct Nuitka_FrameObject *)frame_2452f2af5cef26a75daa30fe34de1399,
        type_description_1,
        par_file,
        var_file_text,
        var_tree
    );


    // Release cached frame.
    if ( frame_2452f2af5cef26a75daa30fe34de1399 == cache_frame_2452f2af5cef26a75daa30fe34de1399 )
    {
        Py_DECREF( frame_2452f2af5cef26a75daa30fe34de1399 );
    }
    cache_frame_2452f2af5cef26a75daa30fe34de1399 = NULL;

    assertFrameObject( frame_2452f2af5cef26a75daa30fe34de1399 );

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    {
    CHECK_OBJECT( var_tree );
    tmp_return_value = var_tree;
    Py_INCREF( tmp_return_value );
    goto try_return_handler_1;
    }
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( PyPse$parser$$$function_1_parse_file_to_token );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    {
    Py_XDECREF( par_file );
    par_file = NULL;

    }
    {
    Py_XDECREF( var_file_text );
    var_file_text = NULL;

    }
    {
    Py_XDECREF( var_tree );
    var_tree = NULL;

    }
    {
    goto function_return_exit;
    }
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    {
    Py_XDECREF( par_file );
    par_file = NULL;

    }
    {
    Py_XDECREF( var_file_text );
    var_file_text = NULL;

    }
    {
    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    }
    // End of try:
    }

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( PyPse$parser$$$function_1_parse_file_to_token );
    return NULL;

function_exception_exit:
    assert( exception_type );
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );

    return NULL;
function_return_exit:

CHECK_OBJECT( tmp_return_value );
assert( had_error || !ERROR_OCCURRED() );
return tmp_return_value;

}



static PyObject *MAKE_FUNCTION_PyPse$parser$$$function_1_parse_file_to_token(  )
{
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl_PyPse$parser$$$function_1_parse_file_to_token,
        const_str_plain_parse_file_to_token,
#if PYTHON_VERSION >= 300
        NULL,
#endif
        codeobj_2452f2af5cef26a75daa30fe34de1399,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        NULL,
#endif
        module_PyPse$parser,
        NULL,
        0
    );

    return (PyObject *)result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_PyPse$parser =
{
    PyModuleDef_HEAD_INIT,
    "PyPse.parser",   /* m_name */
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

extern PyObject *const_str_plain___package__;

#if PYTHON_VERSION >= 300
extern PyObject *const_str_dot;

extern PyObject *const_str_plain___loader__;
extern PyObject *metapath_based_loader;
#endif

#if PYTHON_VERSION >= 340
extern PyObject *const_str_plain___spec__;
extern PyObject *const_str_plain__initializing;
#endif

extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();
#if PYTHON_VERSION >= 350
extern void _initCompiledCoroutineTypes();
#endif
#if PYTHON_VERSION >= 360
extern void _initCompiledAsyncgenTypes();
#endif

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( PyPse$parser )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_PyPse$parser );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    /* Initialize the compiled types of Nuitka. */
    _initCompiledCellType();
    _initCompiledGeneratorType();
    _initCompiledFunctionType();
    _initCompiledMethodType();
    _initCompiledFrameType();
#if PYTHON_VERSION >= 350
    _initCompiledCoroutineTypes();
#endif
#if PYTHON_VERSION >= 360
    _initCompiledAsyncgenTypes();
#endif

#if PYTHON_VERSION < 300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
#ifdef _NUITKA_TRACE
    puts("PyPse.parser: Calling setupMetaPathBasedLoader().");
#endif
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 300
    patchInspectModule();
#endif

#endif

    /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("PyPse.parser: Calling createModuleConstants().");
#endif
    createModuleConstants();

    /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("PyPse.parser: Calling createModuleCodeObjects().");
#endif
    createModuleCodeObjects();

    // puts( "in initPyPse$parser" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_PyPse$parser = Py_InitModule4(
        "PyPse.parser",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No "__doc__" is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else

    module_PyPse$parser = PyModule_Create( &mdef_PyPse$parser );
#endif

    moduledict_PyPse$parser = MODULE_DICT( module_PyPse$parser );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        PyObject *module_name = GET_STRING_DICT_VALUE( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___name__ );

        UPDATE_STRING_DICT1(
            moduledict_PyPse$parser,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );

#else

#if PYTHON_VERSION < 300
        PyObject *module_name = GET_STRING_DICT_VALUE( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___name__ );
        char const *module_name_cstr = PyString_AS_STRING( module_name );

        char const *last_dot = strrchr( module_name_cstr, '.' );

        if ( last_dot != NULL )
        {
            UPDATE_STRING_DICT1(
                moduledict_PyPse$parser,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize( module_name_cstr, last_dot - module_name_cstr )
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___name__ );
        Py_ssize_t dot_index = PyUnicode_Find( module_name, const_str_dot, 0, PyUnicode_GetLength( module_name ), -1 );

        if ( dot_index != -1 )
        {
            UPDATE_STRING_DICT1(
                moduledict_PyPse$parser,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring( module_name, 0, dot_index )
            );
        }
#endif
#endif
    }

    CHECK_OBJECT( module_PyPse$parser );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_67f6a5b95450101e1a1522e82b8fa0b6, module_PyPse$parser );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if ( GET_STRING_DICT_VALUE( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if !defined(_NUITKA_EXE) || !0
        value = PyModule_GetDict( value );
#endif

        UPDATE_STRING_DICT0( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___builtins__, value );
    }

#if PYTHON_VERSION >= 300
    UPDATE_STRING_DICT0( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___loader__, metapath_based_loader );
#endif

#if PYTHON_VERSION >= 340
#if 0
    UPDATE_STRING_DICT0( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___spec__, Py_None );
#else
    {
        PyObject *bootstrap_module = PyImport_ImportModule("importlib._bootstrap");
        CHECK_OBJECT( bootstrap_module );
        PyObject *module_spec_class = PyObject_GetAttrString( bootstrap_module, "ModuleSpec" );
        Py_DECREF( bootstrap_module );

        PyObject *args[] = {
            GET_STRING_DICT_VALUE( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___name__ ),
            metapath_based_loader
        };

        PyObject *spec_value = CALL_FUNCTION_WITH_ARGS2(
            module_spec_class,
            args
        );

        SET_ATTRIBUTE( spec_value, const_str_plain__initializing, Py_True );

        UPDATE_STRING_DICT1( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___spec__, spec_value );

        Py_DECREF( module_spec_class );
    }
#endif
#endif


    // Temp variables if any
    struct Nuitka_FrameObject *frame_61b21cafc25f22bbfbab06c21a1b6112;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;

    // Module code.
    {
    PyObject *tmp_assign_source_1;
    tmp_assign_source_1 = Py_None;
    UPDATE_STRING_DICT0( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    }
    {
    PyObject *tmp_assign_source_2;
    tmp_assign_source_2 = const_str_digest_cf929a79ea3bfc426949a12e1cc6d691;
    UPDATE_STRING_DICT0( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    }
    {
    PyObject *tmp_assign_source_3;
    tmp_assign_source_3 = Py_None;
    UPDATE_STRING_DICT0( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain___cached__, tmp_assign_source_3 );
    }
    // Frame without reuse.
    frame_61b21cafc25f22bbfbab06c21a1b6112 = MAKE_MODULE_FRAME( codeobj_61b21cafc25f22bbfbab06c21a1b6112, module_PyPse$parser );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_61b21cafc25f22bbfbab06c21a1b6112 );
    assert( Py_REFCNT( frame_61b21cafc25f22bbfbab06c21a1b6112 ) == 2 );

    // Framed code:
    {
    PyObject *tmp_assign_source_4;
    PyObject *tmp_import_name_from_1;
    PyObject *tmp_name_name_1;
    PyObject *tmp_globals_name_1;
    PyObject *tmp_locals_name_1;
    PyObject *tmp_fromlist_name_1;
    PyObject *tmp_level_name_1;
    tmp_name_name_1 = const_str_plain_lark;
    tmp_globals_name_1 = (PyObject *)moduledict_PyPse$parser;
    tmp_locals_name_1 = Py_None;
    tmp_fromlist_name_1 = const_tuple_str_plain_Lark_tuple;
    tmp_level_name_1 = const_int_0;
    frame_61b21cafc25f22bbfbab06c21a1b6112->m_frame.f_lineno = 1;
    tmp_import_name_from_1 = IMPORT_MODULE5( tmp_name_name_1, tmp_globals_name_1, tmp_locals_name_1, tmp_fromlist_name_1, tmp_level_name_1 );
    if ( tmp_import_name_from_1 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    tmp_assign_source_4 = IMPORT_NAME( tmp_import_name_from_1, const_str_plain_Lark );
    Py_DECREF( tmp_import_name_from_1 );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 1;

        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain_Lark, tmp_assign_source_4 );
    }
    {
    PyObject *tmp_assign_source_5;
    PyObject *tmp_called_name_1;
    PyObject *tmp_mvar_value_1;
    PyObject *tmp_args_name_1;
    PyObject *tmp_kw_name_1;
    tmp_mvar_value_1 = GET_STRING_DICT_VALUE( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain_Lark );

    if (unlikely( tmp_mvar_value_1 == NULL ))
    {
        tmp_mvar_value_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_Lark );
    }

    CHECK_OBJECT( tmp_mvar_value_1 );
    tmp_called_name_1 = tmp_mvar_value_1;
    tmp_args_name_1 = const_tuple_str_digest_83bce1bac4082b0fcde264be3cc4c001_tuple;
    tmp_kw_name_1 = PyDict_Copy( const_dict_5ad418cbcefcc35faafb0546f0413c37 );
    frame_61b21cafc25f22bbfbab06c21a1b6112->m_frame.f_lineno = 3;
    tmp_assign_source_5 = CALL_FUNCTION( tmp_called_name_1, tmp_args_name_1, tmp_kw_name_1 );
    Py_DECREF( tmp_kw_name_1 );
    if ( tmp_assign_source_5 == NULL )
    {
        assert( ERROR_OCCURRED() );

        FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


        exception_lineno = 3;

        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain_pse_parser, tmp_assign_source_5 );
    }

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION( frame_61b21cafc25f22bbfbab06c21a1b6112 );
#endif
    popFrameStack();

    assertFrameObject( frame_61b21cafc25f22bbfbab06c21a1b6112 );

    goto frame_no_exception_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_61b21cafc25f22bbfbab06c21a1b6112 );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_61b21cafc25f22bbfbab06c21a1b6112, exception_lineno );
    }
    else if ( exception_tb->tb_frame != &frame_61b21cafc25f22bbfbab06c21a1b6112->m_frame )
    {
        exception_tb = ADD_TRACEBACK( exception_tb, frame_61b21cafc25f22bbfbab06c21a1b6112, exception_lineno );
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;

    frame_no_exception_1:;
    {
    PyObject *tmp_assign_source_6;
    tmp_assign_source_6 = MAKE_FUNCTION_PyPse$parser$$$function_1_parse_file_to_token(  );



    UPDATE_STRING_DICT1( moduledict_PyPse$parser, (Nuitka_StringObject *)const_str_plain_parse_file_to_token, tmp_assign_source_6 );
    }

    return MOD_RETURN_VALUE( module_PyPse$parser );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
