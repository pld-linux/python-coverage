%define 	module	coverage
Summary:	Tool for measuring code coverage of Python programs
Name:		python-%{module}
Version:	3.7.1
Release:	4
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/c/coverage/%{module}-%{version}.tar.gz
# Source0-md5:	c47b36ceb17eaff3ecfab3bcd347d0df
URL:		http://nedbatchelder.com/code/coverage
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coverage.py is a tool for measuring code coverage of Python programs.
It monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have
been executed but was not.

%package -n python3-%{module}
Summary:	Tool for measuring code coverage of Python programs
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-%{module}
Coverage.py is a tool for measuring code coverage of Python programs.
It monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have
been executed but was not.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build --build-base py2
%{__python3} setup.py build --build-base py3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build \
    --build-base py2 \
    install \
    --root=$RPM_BUILD_ROOT \
    --optimize=2

%{__python3} setup.py build \
    --build-base py3 \
    install \
    --root=$RPM_BUILD_ROOT \
    --optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%attr(755,root,root) %{_bindir}/coverage-2.7
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}/htmlfiles
%if "%{py_ver}" > "2.4"
%{py_sitedir}/coverage-%{version}*.egg-info
%endif

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%attr(755,root,root) %{_bindir}/coverage-3.4
%dir %{py3_sitedir}/%{module}
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}/htmlfiles
%{py3_sitedir}/*.egg-info
