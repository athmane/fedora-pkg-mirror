%global srcname pyuv

%global sum A Python module which provides an interface to libuv
%global common_desc \
pyuv is a Python module which provides an interface to libuv.\
libuv is a high performance asynchronous networking and platform\
abstraction library.libuv is built on top of epoll/kequeue/event \
ports/etc on Unix and IOCP on Windows systems providing a consistent\
API on top of them.

Name: python-pyuv
Version: 1.2.0
Release: 8%{?dist}
Summary: %{sum}

License: MIT     
URL: https://github.com/saghul/pyuv    
Source0: https://github.com/saghul/pyuv/archive/pyuv-%{version}.tar.gz
Requires: libuv >= 1.7.0
BuildRequires:  python2-devel python-tox python-nose 
BuildRequires:  python3-devel python3-tox python3-nose
BuildRequires:  libuv-devel >= 1.7.0
BuildRequires:  python-sphinx

%description
%{common_desc}

%package -n  python2-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_desc}


%package -n  python3-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%package doc
Summary: Documentation for %{srcname}

%description doc
%{common_desc}
This package contains documentation in reST and HTML formats.

%prep
%autosetup -n %{srcname}-%{version}

%build
# Use system-provided libuv
/bin/rm -rf deps/
sed -i 's/self.use_system_libuv = 0/self.use_system_libuv = 1/' setup_libuv.py
%py2_build
%py3_build

pushd docs
make html
mv _build/html/* .
popd


%install
%py2_install
%py3_install


%check
#TODO: Remove hackish commands
# tty test fails inside mock
cd tests/
rm -f test_tty.py
export PYUV_INSIDE_TOX=1
export PYTHONPATH=%{buildroot}/%{python2_sitearch}
#nosetests-%{python2_version} -v 
export PYTHONPATH=%{buildroot}/%{python3_sitearch}
#nosetests-%{python3_version} -v


%files -n python2-%{srcname}
%license LICENSE
%doc AUTHORS ChangeLog README.rst TODO
%{python2_sitearch}/*

%files -n  python3-%{srcname}
%license LICENSE
%doc AUTHORS ChangeLog README.rst TODO
%{python3_sitearch}/*

%files doc
%doc docs


%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 10 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.2.0-7
- Switch URL to github since pypi has md5 in the url
- Disable the testsuite for now (hangs in koji but ok in mock or rpmbuild)

* Fri Apr 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> 1.2.0-6
- Remove bundled libuv (it was not used anyway)
- Run the testsuite
- Build and ship the doc

* Sat Mar 12 2016 Athmane Madjoudj <athmane@fedoraproject.org> 1.2.0-5
- Update spec to use the new Python guidelines

* Tue Feb 09 2016 Athmane Madjoudj <athmanem@fedoraproject.org> 1.2.0-4
- Fix reqs since pyuv uses uv_tcp_init_ex (new in 1.7.0)

* Tue Feb 09 2016 Athmane Madjoudj <athmanem@fedoraproject.org> 1.2.0-3
- Fix build step

* Tue Feb 09 2016 Athmane Madjoudj <athmanem@fedoraproject.org>  1.2.0-2
- Disable the testsuite since it tries to download pkgs

* Tue Feb 09 2016 Athmane Madjoudj <athmanem@fedoraproject.org> 1.2.0-1
- Initial spec release.

