# TODO: finish doc and tests (where dependencies available in PLD)
#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_with	doc	# Sphinx documentation
%bcond_with	tests	# unit tests

%define 	module	coverage
Summary:	Tool for measuring code coverage of Python programs
Summary(pl.UTF-8):	Narzędzie do szacowania pokrycia kodu programów w Pythonie
Name:		python-%{module}
Version:	4.5.4
Release:	3
License:	Apache v2.0
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/coverage/
Source0:	https://files.pythonhosted.org/packages/source/c/coverage/%{module}-%{version}.tar.gz
# Source0-md5:	c33cab2aed8780aac32880cb6c7616b7
URL:		http://coverage.readthedocs.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools >= 35.0.2
%if %{with tests}
BuildRequires:	python-eventlet >= 0.22.0
BuildRequires:	python-flaky >= 3.4.0
BuildRequires:	python-gevent >= 1.2.2
BuildRequires:	python-greenlet >= 0.4.13
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-pycontracts >= 1.8.2
BuildRequires:	python-pyparsing >= 2.4.0
BuildRequires:	python-pytest >= 3.2.5
BuildRequires:	python-pytest-xdist >= 1.20.1
BuildRequires:	python-unittest-mixins >= 1.4
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools >= 35.0.2
%if %{with tests}
BuildRequires:	python3-eventlet >= 0.22.0
BuildRequires:	python3-flaky >= 3.4.0
BuildRequires:	python3-greenlet >= 0.4.13
BuildRequires:	python3-pycontracts >= 1.8.2
BuildRequires:	python3-pyparsing >= 2.4.0
BuildRequires:	python3-pytest >= 3.2.5
BuildRequires:	python3-pytest-xdist >= 1.20.1
BuildRequires:	python3-unittest-mixins >= 1.4
%endif
%endif
%if %{with doc}
BuildRequires:	python-doc8 >= 0.8.0
BuildRequires:	python-pyenchant >= 2.0.0
BuildRequires:	python-sphinxcontrib-spelling >= 4.0.1
BuildRequires:	python-sphinx_rtd_theme >= 0.2.4
BuildRequires:	sphinx-pdg-2 >= 1.6.6
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

%if %{with tests}
%{__python} igor.py test_with_tracer py
%{__python} igor.py test_with_tracer c
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} igor.py test_with_tracer py
%{__python3} igor.py test_with_tracer c
%endif
%endif

%if %{with doc}
sphinx-build -b html -aqE doc doc/_build/html
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
%dir %{py_sitedir}/coverage
%{py_sitedir}/coverage/*.py[co]
%attr(755,root,root) %{py_sitedir}/coverage/tracer.so
%{py_sitedir}/coverage/fullcoverage
%{py_sitedir}/coverage/htmlfiles
%{py_sitedir}/coverage-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst CONTRIBUTORS.txt NOTICE.txt README.rst TODO.txt
%attr(755,root,root) %{_bindir}/coverage3
%attr(755,root,root) %{_bindir}/coverage-%{py3_ver}
%dir %{py3_sitedir}/coverage
%attr(755,root,root) %{py3_sitedir}/coverage/tracer.cpython-*.so
%{py3_sitedir}/coverage/*.py
%{py3_sitedir}/coverage/__pycache__
%{py3_sitedir}/coverage/fullcoverage
%{py3_sitedir}/coverage/htmlfiles
%{py3_sitedir}/coverage-%{version}-py*.egg-info
%endif
