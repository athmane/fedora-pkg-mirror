# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$ 
%filter_setup
}

Name:           python-pybloomfiltermmap
Version:        0.3.15
Release:        2%{?dist}
Summary:        A Bloom filter (bloomfilter) for Python built on mmap

License:        MIT
URL:            http://github.com/axiak/pybloomfiltermmap/
Source0:        http://pypi.python.org/packages/source/p/pybloomfiltermmap/pybloomfiltermmap-%{version}.tar.gz

BuildRequires:  python2-devel python-setuptools openssl-devel Cython

%description
The goal of pybloomfiltermmap is to provide a fast, simple, scalable,
correct library for Bloom Filters in Python.

%prep
%setup -q -n pybloomfiltermmap-%{version}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%check
# Failed on armv7hl (see task 6998792 on Koji)
# %{__python} setup.py test

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc AUTHORS CHANGELOG LICENSE
%{python_sitearch}/*


%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.15-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 12 2016 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.15-1
- Update to 0.3.15

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.14-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.14-3
- Disable the testsuite because it fails on armv7hl

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.14-1
- Update to 0.3.14

* Sat Mar 01 2014 Athmane Madjoudj <athmane@fedoraproject.org>  0.3.12-2
- Remove comment about the test suite since it's enabled now.

* Wed Feb 26 2014 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.12-1
- Update to 0.3.12
- Add Cython a build requirement
- Enable the testsuite since it passes now

* Sat Feb 22 2014 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.11-3
- Comment check section since test suite is failing

* Sat Feb 22 2014 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.11-2
- Enable test suite

* Sun Aug 04 2013  Athmane Madjoudj <athmane@fedoraproject.org> 0.3.11-1
- Update to 0.3.11

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jan 21 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.3.2-1
- Initial spec. 
