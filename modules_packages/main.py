'''main.py'''
import a_package
from a_package import test1

# A function declared in the package
a_package.func_test1_f1()

# A function declared only in the module
test1.func_test1_f2()
