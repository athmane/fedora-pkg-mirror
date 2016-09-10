%global srcname pyftpdlib
%global common_desc Python FTP server library provides a high-level portable interface to easily\
write asynchronous FTP servers with Python. Based on asyncore framework\
pyftpdlib is currently the most complete RFC-959 FTP server implementation\
available for Python programming language.\

Name:           pyftpdlib
Version:        1.5.0
Release:        6%{?dist}
Summary:        Python FTP server library

License:        MIT
URL:            https://github.com/giampaolo/pyftpdlib
Source0:        https://github.com/giampaolo/pyftpdlib/archive/release-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-nose 
BuildRequires:  python2-setuptools 
BuildRequires:  python2-pysendfile
BuildRequires:  python3-devel 
BuildRequires:  python3-nose 
BuildRequires:  python3-setuptools

%description
%common_desc

%package -n python2-%{srcname}
Summary:        %{summary}
Requires:       python2-pysendfile 
Requires:       pyOpenSSL
Provides:       pyftpdlib
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%common_desc

This package provides pyftpdlib for Python 2.



%package -n python3-%{srcname}
Summary:        %{summary}
# sendfile is not needed in Python 3, pyftpdlib will use os.sendfile instead
Requires:       python3-pyOpenSSL
Provides:       pyftpdlib
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%common_desc

This package provides pyftpdlib for Python 3.

%prep
%setup -qn %{srcname}-release-%{version}

# Remove exec bit from demo
chmod -x demo/*

# Remove shebang from libs
sed -i '1{\@^#!/usr/bin/env python@d}' %{name}/*.py

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
PYTHONPATH=. %{__python2} setup.py test

# tests on py3 are failing atm
sed -i 's/import mock/from unittest import mock/' pyftpdlib/test/test_functional.py
#PYTHONPATH=. %{__python3} setup.py test

%files -n python2-%{srcname}
%license LICENSE
%doc CREDITS HISTORY.rst README.rst demo/ 
%{python2_sitelib}/pyftpdlib
%{python2_sitelib}/pyftpdlib-%{version}-*.egg-info

%files -n python3-%{srcname}
%license LICENSE
%doc CREDITS HISTORY.rst README.rst demo/
%{python3_sitelib}/pyftpdlib
%{python3_sitelib}/pyftpdlib-%{version}-*.egg-info
%{_bindir}/ftpbench

%changelog
* Sat Jul 30 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-6
- Minor spec fixes

* Sat Jul 30 2016 Petr Viktorin <pviktori@redhat.com> - 1.5.0-5
- Put ftpbench in the python3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Athmane Madjoudj <athmane@fedoraproject.org>	 - 1.5.0-3
- Fix deps on rawhide

* Tue Jun 28 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-2
- Fix deps

* Mon Jun 27 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0
- Revamp the spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 David Shea <dshea@redhat.com> 1.4.0-3
- Add a python3 package.
- Use %%license for the license file

* Wed Dec 24 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.4.0-2
- Add deps on pyOpenSSL

* Wed Dec 24 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.4.0-1
- Update to 1.4.0
- Update spec file
- Enable the test suite

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 10 2012 Silas Sewell <silas@sewell.org> - 0.7.0-1
- Update to 0.7.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Silas Sewell <silas@sewell.org> - 0.6.0-1
- Update to 0.6.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Oct 21 2009 Silas Sewell <silas@sewell.ch> - 0.5.2-1
- Update to 0.5.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar 28 2009 Silas Sewell <silas@sewell.ch> - 0.5.1-4
- Fix various issues reported by rpmlint
- Remove INSTALL file

* Thu Mar 26 2009 Silas Sewell <silas@sewell.ch> - 0.5.1-3
- Update package name to conform to Fedora naming standards
- Remove unneeded requires
- Change define to global

* Thu Mar 12 2009 Silas Sewell <silas@sewell.ch> - 0.5.1-2
- Fix various rpmlint issues

* Tue Feb 24 2009 Silas Sewell <silas@sewell.ch> - 0.5.1-1
- Initial build
