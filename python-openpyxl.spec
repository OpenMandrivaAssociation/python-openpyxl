Name:		python-openpyxl
Version:	3.1.5
Release:	2
Summary:	A Python library to read/write Excel 2010 xlsx/xlsm files
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/openpyxl/
Source0:	openpyxl-3.1.5.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(et-xmlfile)
BuildArch:	noarch
%description
A Python library to read/write Excel 2010 xlsx/xlsm files.

%files
%{py_sitedir}/*
