%global srcname Fabric3

Name:           fabric
Version:        1.12.post1
Release:        4%{?dist}
Summary:        A simple Pythonic remote deployment tool

Group:          Applications/System
License:        BSD
URL:            http://www.fabfile.org
Source0:        https://files.pythonhosted.org/packages/source/F/%{srcname}/%{srcname}-%{version}.tar.gz
#Patch0:         fabric-1.12.0-fix-testsuite.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-paramiko >= 1.10.0

# For running test suite
BuildRequires:  python3-nose python3-jinja2
#BuildRequires:  python-fudge 


Requires:       python3-paramiko >= 1.10.0
Requires:       python3-crypto
Requires:       python3-setuptools

%description
Fabric is a simple Pythonic remote deployment tool which is designed to upload
files to, and run shell commands on, a number of servers in parallel or
serially.

%prep
%setup -q -n %{srcname}-%{version}
#%patch0 -p1
sed -i 's/paramiko>=1.17.2,<2.0/paramiko>=1.17.2/g' setup.py
rm -fr Fabric.egg-info

%build
%{__python3} setup.py build

%check
# Still fails
#%{__python3} setup.py test

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%files
%doc AUTHORS LICENSE README.rst
%{_bindir}/fab
%{python3_sitelib}/fabric
%{python3_sitelib}/%{srcname}*%{version}*.egg-info

%changelog
* Fri Aug 26 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.12.post1-4
- Switch to a fork with Py3 support (RHBZ #1370016)

* Mon Aug 15 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.12.0-2
- Fix an issue with paramiko >= 2.0
- Add pycrypto BR

* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org>  - 1.12.0-1
- Update to 1.12.0
- Change Source url since pypi urls include md5.
- Disable check due to many failure

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 12 2016 Athmane Madjoudj <athmane@fedoraproject.org> 1.11.1-1
- Update to 1.11.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 Athmane Madjoudj <athmane@fedoraproject.org> 1.10.2-1
- Update to 1.10.2
- Rebase patch for the test suite

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 23 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.10.1-2
- Enable the test suite.
- Add a patch to disable tests failing with the recent fudge lib

* Tue Dec 23 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.10.1-1
- Update to 1.10.1

* Fri Sep 05 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.10.0-1
- Update to 1.10.0
- Remove macros in comments and changelog

* Fri Aug 08 2014 Athmane Madjoudj <athmane@fedoraproject.org>  1.9.1-1
- Update to 1.9.1

* Wed Jun 11 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.9.0-1
- Update to 1.9.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.8.3-1
- Update to 1.8.3

* Sat Feb 22 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.8.2-3
- Comment check section since test-suite fails

* Sat Feb 22 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.8.2-2
- Add check section to run the test-suite

* Tue Feb 18 2014 Athmane Madjoudj <athmane@fedoraproject.org> 1.8.2-1
- Update to 1.8.2

* Wed Dec 25 2013 Athmane Madjoudj <athmane@fedoraproject.org> 1.8.1-1
- Update to 1.8.1

* Mon Sep 23 2013 Athmane Madjoudj <athmane@fedoraproject.org>  1.8.0-1
- Update to 1.8.0

* Wed Jul 31 2013 Athmane Madjoudj <athmane@fedoraproject.org> 1.7.0-1
- Update to 1.7.0

* Wed Jul 31 2013 Athmane Madjoudj <athmane@fedoraproject.org> 1.6.2-1
- Update to 1.6.2

* Thu May 9 2013 Orion Poplawski <orion@cora.nwra.com> - 1.6.0-1
- Update to 1.6.0
- Use python-paramiko instead of python-ssh
- Remove shipped egg-info
- Misc cleanup

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Silas Sewell <silas@sewell.org> - 1.4.3-2
- Remove check section

* Sun Jul 08 2012 Silas Sewell <silas@sewell.org> - 1.4.3-1
- Update to 1.4.3

* Thu May 17 2012 Silas Sewell <silas@sewell.org> - 1.4.2-3
- Need fudge for tests

* Thu May 17 2012 Silas Sewell <silas@sewell.org> - 1.4.2-2
- Require never version of ssh

* Wed May 09 2012 Silas Sewell <silas@sewell.org> - 1.4.2-1
- Update to 1.4.2

* Thu Apr 19 2012 Silas Sewell <silas@sewell.org> - 1.4.1-1
- Update to 1.4.1

* Sun Mar 18 2012 Silas Sewell <silas@sewell.org> - 1.4.0-1
- Update to 1.4.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Silas Sewell <silas@sewell.org> - 1.2.0-1
- Update to 1.2.0

* Sun Mar 27 2011 Silas Sewell <silas@sewell.ch> - 1.0.1-1
- Update to 1.0.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 19 2010 Silas Sewell <silas@sewell.ch> - 0.9.3-1
- Update to 0.9.3
- Remove old page and man page

* Sat Oct 09 2010 Silas Sewell <silas@sewell.ch> - 0.9.2-1
- Update to 0.9.2
- Import man page from upstream branch
- Apply upstream patch to fix incorrect requirements

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 06 2010 Silas Sewell <silas@sewell.ch> - 0.9.1-1
- Update to 0.9.1
- Add man page

* Mon Nov 09 2009 Silas Sewell <silas@sewell.ch> - 0.9.0-1
- Update to 0.9.0

* Thu Aug 27 2009 Silas Sewell <silas@sewell.ch> - 0.9-0.1.b1
- Update to latest snapshot

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Silas Sewell <silas@sewell.ch> - 0.1.1-2
- Add runtime setuptools requirements
- Re-import source package

* Thu Apr 09 2009 Silas Sewell <silas@sewell.ch> - 0.1.1-1
- Update to 0.1.1
- Up Paramiko version dependency to 1.7
- Remove Python version dependency
- Make sed safer

* Sat Mar 28 2009 Silas Sewell <silas@sewell.ch> - 0.1.0-3
- Fix dependencies
- Fix non-executable-script error

* Thu Mar 26 2009 Silas Sewell <silas@sewell.ch> - 0.1.0-2
- Change define to global

* Sun Feb 22 2009 Silas Sewell <silas@sewell.ch> - 0.1.0-1
- Update to 0.1.0
- Up Python requirement to 2.5 per recommendation on official site

* Thu Nov 20 2008 Silas Sewell <silas@sewell.ch> - 0.0.9-3
- Fix changelog syntax issue

* Thu Nov 20 2008 Silas Sewell <silas@sewell.ch> - 0.0.9-2
- Fix various issues with the spec file

* Wed Nov 19 2008 Silas Sewell <silas@sewell.ch> - 0.0.9-1
- Initial package
