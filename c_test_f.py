import ctypes
import os

c_lib = CDLL('./test_f.so')

c_fun = c_lib.foo1
c_fun.restype = c_double
c_fun.argtypes = (c_short,)
return_foo = c_fun(1)
print('foo1 has returned %d' % return_foo)

c_fun = c_lib.foo2
c_fun.restype = c_wchar_p
c_fun.argtypes = (c_wchar_p,)
return_foo = c_fun("foo2")
print("foo2 has returned %s" % return_foo)

c_fun = c_lib.foo3
c_fun.restype = c_void_p
c_fun.argtypes = (c_double, c_int, c_wchar_p)
return_foo = c_fun(2.71828, -987654321, "foo3")
print("foo3 has returned %s" % return_foo)

my_list = [0, 1, 2]
my_list_c = (c_int * len(my_list))(*my_list)
c_fun = c_lib.foo4
c_fun.argtypes = [c_int, POINTER(c_int)]
c_fun(len(my_list), my_list_c)
print("foo4 has ended")

