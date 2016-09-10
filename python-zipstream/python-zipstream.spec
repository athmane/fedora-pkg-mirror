%global srcname zipstream
%global desc zipstream.py is a zip archive generator based on python 3.3's zipfile.py.\
It was created to generate a zip file generator for streaming (ie web apps).

Name:           python-%{srcname}
Version:        1.1.4
Release:        5%{?dist}
Summary:        ZIP archive generator for Python

License:        GPLv3+
URL:            https://github.com/allanlei/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch


%description
%{desc}

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires:  python2-setuptools python2-devel python2-nose 

%description -n python2-%{srcname}
%{desc}
Python 2 version.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-setuptools python3-devel python3-nose

%description -n python3-%{srcname}
%{desc}
Python 3 version.

%prep
%autosetup

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test



%files -n python2-%{srcname}
%license LICENSE
%doc README.* 
%{python2_sitelib}/*

%files -n python3-%{srcname}
%license LICENSE
%doc README.* 
%{python3_sitelib}/*


%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 07 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.4-4
- Move BR into the sub pkg
- Fix prep section 

* Thu Jul 07 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.4-3
- Use more macros
- Fix BR
- Simplify testsuite invocation

* Thu Jul 07 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.4-2
- Fix typos
- Enable check section

* Tue Jul 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.4-1
- Initial spec 
