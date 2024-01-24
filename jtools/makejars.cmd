@setlocal

PATH="D:\java\jdk-21\bin"
           
@set source=D:\vlab\python\jtools\out\production\jtools
@set build=D:\vlab\python\jtools\build

@pushd %source%
jar cfe %build%\jportal.jar vlab/jportal/Compiler vlab/jportal/*.class vlab/jportal/code/*.class vlab/jportal/ddl/*.class
@popd

@pushd %source%
jar cfe %build%\crackle.jar vlab/crackle/Compiler vlab/crackle/*.class vlab/crackle/http/*.class
@popd

rem @PATH="D:\java\jdk-11\bin"
rem 
rem @pushd %source%
rem jar cfe %build%\jportal-11.jar vlab/jportal/Compiler vlab/jportal/*.class vlab/jportal/code/*.class vlab/jportal/ddl/*.class
rem @popd

@pause
