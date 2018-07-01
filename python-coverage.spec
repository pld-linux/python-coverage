#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define 	module	coverage
Summary:	Tool for measuring code coverage of Python programs
Summary(pl.UTF-8):	Narzędzie do szacowania pokrycia kodu programów w Pythonie
Name:		python-%{module}
Version:	4.3.4
Release:	2
License:	Apache v2.0
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/coverage/
Source0:	https://files.pythonhosted.org/packages/source/c/coverage/%{module}-%{version}.tar.gz
# Source0-md5:	89759813309185efcf4af8b9f7762630
URL:		http://coverage.readthedocs.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coverage.py is a tool for measuring code coverage of Python programs.
It monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have
been executed but was not.

%description -l pl.UTF-8
Coverage.py to narzędzie do szacowania pokrycia kodu programów w
Pythonie. Monitoruje program, zapisując, które części kodu zostały
wykonane, a następnie analizuje kod źródłowy w celu zidentyfikowania
kodu, który mógłby zostać wykonany, ale nie był.

%package -n python3-%{module}
Summary:	Tool for measuring code coverage of Python programs
Summary(pl.UTF-8):	Narzędzie do szacowania pokrycia kodu programów w Pythonie
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
Coverage.py is a tool for measuring code coverage of Python programs.
It monitors your program, noting which parts of the code have been
executed, then analyzes the source to identify code that could have
been executed but was not.

%description -n python3-%{module} -l pl.UTF-8
Coverage.py to narzędzie do szacowania pokrycia kodu programów w
Pythonie. Monitoruje program, zapisując, które części kodu zostały
wykonane, a następnie analizuje kod źródłowy w celu zidentyfikowania
kodu, który mógłby zostać wykonany, ale nie był.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py_install

%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst CONTRIBUTORS.txt NOTICE.txt README.rst TODO.txt
%attr(755,root,root) %{_bindir}/coverage
%attr(755,root,root) %{_bindir}/coverage2
%attr(755,root,root) %{_bindir}/coverage-%{py_ver}
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/tracer.so
%{py_sitedir}/%{module}/htmlfiles
%{py_sitedir}/coverage-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst CONTRIBUTORS.txt NOTICE.txt README.rst TODO.txt
%attr(755,root,root) %{_bindir}/coverage3
%attr(755,root,root) %{_bindir}/coverage-%{py3_ver}
%dir %{py3_sitedir}/%{module}
%attr(755,root,root) %{py3_sitedir}/%{module}/tracer.cpython-*.so
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}/htmlfiles
%{py3_sitedir}/coverage-%{version}-py*.egg-info
%endif
