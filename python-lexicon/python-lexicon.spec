%if 0%{?fedora}
    %global with_python3 1
%endif

%global pypi_name lexicon

Name: python-%{pypi_name}
Version: 0.2.0
Release: 5%{?dist}
Summary: A powerful dict sub-classes for Python

License: BSD
URL: https://github.com/bitprophet/lexicon
Source0: https://pypi.python.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch: noarch
Requires: python-six
BuildRequires: python-devel python-setuptools 

%global common_desc \
Lexicon is a simple Python 2.6+ and 3.3+ compatible collection of dict\
sub-classes providing extra power.

%description 
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary: A powerful dict sub-classes for Python
Requires: python3-six
BuildRequires: python3-devel python3-setuptools

%description -n python3-%{pypi_name}
%{common_desc}

This package contains python3 build.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
rm -fr %{pypi_name}.egg-info/


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

%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
    pushd %{py3dir}
    %{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
    popd
%endif


%files
%doc LICENSE README.*
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}-*.egg-info/

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc LICENSE README.*
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-*.egg-info/
%endif

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 01 2014 Athmane Madjoudj <athmane@fedoraproject.org> 0.2.0-1
- Initial spec

