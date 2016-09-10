# Need for EL6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%if 0%{?fedora}
    %global with_python3 1
%endif

Name: python-fudge
Version: 1.0.3
Release: 10%{?dist}
Summary: A Python module for using fake objects (mocks and stubs) to test real ones

License: MIT
URL:     http://farmdev.com/projects/fudge/
Source0: https://pypi.python.org/packages/source/f/fudge/fudge-%{version}.tar.gz
# See check section for details
Source1: tox.ini

BuildArch: noarch
BuildRequires: python2-devel python-setuptools
# Build req. for the test suite
BuildRequires: python-tox python-sphinx
%if 0%{?rhel} && 0%{?rhel} == 6
BuildRequires: python-nose1.1
%else
BuildRequires: python-nose
%endif

%global fudge_desc \
Fudge is a Python module for using fake objects (mocks and stubs) \
to test real ones.\

%description
%{fudge_desc}

%if 0%{?with_python3}
%package -n python3-fudge
Summary: A Python module for using fake objects (mocks and stubs) to test real ones
BuildRequires: python3-devel python3-setuptools
# NOTE: will enable the test suite on python3 once py3 tox pkg is built
# Build req. for the test suite 
# BuildRequires: python3-tox python3-nose python3-sphinx

%description -n python3-fudge
%{fudge_desc}

This is python3 build.

%endif

%prep 
%setup -q -n fudge-%{version}
# We'll use a custom config since we dont have access to the outside 
# in fedora buildsys
cp %{SOURCE1}  %{_builddir}/fudge-%{version}
%if 0%{?rhel} && 0%{?rhel} == 6
# Need newer nose
sed -i -e s/nosetests/nosetests1.1/ tox.ini
# Use different theme
sed -i -e /html_theme/s/nature/default/ docs/conf.py
%endif

%if 0%{?with_python3}
    rm -rf %{py3dir}
    cp -a . %{py3dir}
%endif


%build
%{__python2} setup.py build

%if 0%{?with_python3}
    pushd %{py3dir}
    %{__python3} setup.py build
    popd
%endif

%check
# We'll use a custom config since we dont have access to the outside 
# in fedora buildsys
#./run_tests
tox

%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
    pushd %{py3dir}
    %{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
    popd
%endif

 
%files
%doc LICENSE.txt README.txt
%{python2_sitelib}/*


%if 0%{?with_python3}
%files -n python3-fudge
%doc LICENSE.txt README.txt
%{python3_sitelib}/*
%endif

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 24 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.0.3-6
- Add conditional to exclude EL since does not have py3

* Mon Nov 17 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.0.3-5
- Add python3 support

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.0.3-3
- Use more strict python macros

* Sun Mar 30 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.0.3-2
- Specify python version in the build requirement
- Remove unused macros
- Enable the test suite

* Sat Mar 15 2014 Athmane Madjoudj <athmane@fedoraproject.org>  1.0.3-1
- Initial spec.

