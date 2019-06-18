package_training is used to test how to build a package using
conda.
It has been built using:
    conda build package_training
in the shell at the level of the directory PycharmProjects.

necessary files:
    **meta.yaml**.
    **setup.py.** using the setuptools package.
        The find_packages() function searches the directory where setup.py resides and 
        returns a list of all subdirectories that have an __init__.py file.
        Add packages = find_packages() as an argument to setup.py.
    **__init__.py** in the source directory. This file defines what gets imported 
        from the directory. this file is executed when there 
        is an import statement.
    **Licensing** see comments in alternative method.
    **build.sh/bld.bat** for mac/linux there is an additional file: build.sh (bld.bat for windows).
        This file is used to detail the script that needs to be executed 
        in the building process ex: python setup.py install --single-version-externally-managed --record=record.txt
        this file can be omitted and the script in that case is written in meta.yaml
        in the 
        build:
            script:
        section. 

to update to a new version change version in __init__.py,
 this will impact directly setup.py and meta.yaml,
then use conda build.

to install the package in a selected environment:
conda install --use-local package_training

to update:
conda update --use-local package_training

to upload to anaconda cloud:
go to conda-bld folder.
activate base env to use anaconda package
run anaconda upload noarch/<file name>
(in case it's a noarch conda package, see below comment)
<file-name> example: 
    package_training-0.1.3-py_0.tar.bz2

The general practice is to run conda build separately 
on Windows, Mac, and Linux and with the popular minor 
revisions of Python (2.7, 3.5, 3.6, etc.). This step 
is necessary if you have architecture-specific build steps, 
like compiling Python C/C++ extensions, 
or incompatibility between Python 2 and Python 3 
in both the build and run steps.
If your project is cross-architecture and it works 
on Python 2 and Python 3 you'll convert it to a 
noarch Conda package. it is done by specifying
"noarch : python" in meta.yaml under the "build: section"

*************

Alternative method with conda:
set up the __init__.py file, to define what gets imported 
from the directory. this file is executed when there 
is an import statement.

create the setup.py file using the setuptools package.
The find_packages() function searches the directory where setup.py resides and 
returns a list of all subdirectories that have an __init__.py file.
Add packages = find_packages() as an argument to setup.py

Licensing: Since our goal is to share our code with others 
we need to be aware of copyright laws and the legal 
rights we wish to retain about how that software can 
be used. Copyright protections are guaranteed to 
the person who owns the software. When someone else 
downloads and uses the program we built we would not 
want to transfer ownership to them, thereby forfeiting 
our rights. Instead, we wish license usage of the 
program under certain restrictions. The full text of 
the license needs to be placed in the 
package/LICENSE file and it must remain in 
the package directory for the license to be valid 
and enforceable. Further, license="..." need to be added 
in setup.py.

run python setup.py install

It's important to note that setup.py does not contain 
information about dependent packages. While the 
setup.py file can define these packages you need to 
use Conda Build as in the previous method to define 
and install dependent packages. With this method, in order to 
use the package we must have dependant packages 
installed. 

the other point is that you need to have downloaded 
the source code to use this method.

Further, when using setuptools to install packages 
there are no uninstall or update commands. That means 
you would have to manually remove the installed files
if you want to install a newer version of the package.