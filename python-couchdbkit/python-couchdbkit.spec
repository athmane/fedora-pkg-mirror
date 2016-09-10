Name:           python-couchdbkit
Version:        0.6.5
Release:        6%{?dist}
Summary:        CouchDB framework in Python
License:        MIT
URL:            http://couchdbkit.org
Source0:        http://pypi.python.org/packages/source/c/couchdbkit/couchdbkit-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# For the tests.
BuildRequires:  couchdb
BuildRequires:  python-nose
BuildRequires:  python-unittest2
# If we don't add this dep I think it will be useless.
Requires:       couchdb
Requires:       python-anyjson
Requires:       python-restkit

%description
Couchdbkit provides you a full featured and easy client to access and manage 
CouchDB. It allows you to manage a CouchDBserver, databases, doc managements 
and view access. All objects mostly reflect python objects for convenience. 
Server and Databases objects could be used for example as easy as using dicts.

%prep
%setup -qn couchdbkit-%{version}
rm -rf couchdbkit.egg-info
chmod 644 LICENSE

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --prefix=%{_prefix} -O1 --skip-build --root=%{buildroot}

%check
# I tried to run counchdb in non-root user and seems not successfully.
# couchdb -b && %%{__python2} setup.py test && couchdb -d
# Otherwise I can't find a way to test.

%files
%doc LICENSE README.rst
%{python2_sitelib}/couchdbkit
%{python2_sitelib}/couchdbkit-%{version}-py%{python2_version}.egg-info

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 31 2013 Christopher Meng <rpm@cicku.me> - 0.6.5-2
- Remove bundled eggs.

* Tue Sep 17 2013 Christopher Meng <rpm@cicku.me> - 0.6.5-1
- Initial Package.
