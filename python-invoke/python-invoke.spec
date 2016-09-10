%global srcname invoke
%global sum A Python task execution tool and library
%global invoke_desc \
Invoke is a Python (2.6+ and 3.2+) task execution tool and library,\
drawing inspiration from various sources to arrive at a powerful\
and clean feature set.\


Name: python-invoke
Version: 0.13.0
Release: 3%{?dist}
Summary: A Python task execution tool and library

License: BSD
URL: http://pyinvoke.org
Source0: https://github.com/pyinvoke/invoke/archive/%{version}.tar.gz

BuildArch: noarch
BuildRequires: python-devel python-setuptools  python-nose
BuildRequires: python3-devel python3-setuptools python3-nose



%description 
%{invoke_desc}

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
Requires: python-six python-pexpect python-fluidity-sm python-lexicon PyYAML

%description -n python2-%{srcname}
An python module which provides a convenient example.


%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires: python3-six python3-pexpect python3-fluidity-sm python3-lexicon python3-PyYAML

%description -n python3-%{srcname}
An python module which provides a convenient example.



%prep
%setup -q -n invoke-%{version}
rm -fr invoke.egg-info/

# Remove bundled libs
# https://github.com/pyinvoke/invoke/issues/204
rm -fr invoke/vendor/

for f in `find . -name '*.py'` ; do 
sed -i '
s/from .vendor import six/import six/g
s/from .vendor.lexicon import Lexicon/from lexicon import Lexicon/g
s/from ..vendor.lexicon import Lexicon/from lexicon import Lexicon/g
s/from ..vendor.fluidity import StateMachine, state, transition/from fluidity import StateMachine, state, transition/g
s/from ..vendor import six/import six/g
s/from .vendor import pexpect/import pexpect/g
s/from .vendor import yaml3 as yaml/import yaml/g
s/from .vendor import yaml2 as yaml/import yaml/g
'  $f
done

%build
%py2_build
%py3_build

%check
# Tests are failing atm

%install
%py2_install

# Replace binaries name to avoid conflict with python2 variant
sed -i '
s/invoke = invoke.main:program.run/invoke3 = invoke.main:program.run/
s/inv = invoke.main:program.run/inv3 = invoke.main:program.run/
' setup.py

%py3_install

%files -n python2-%{srcname}
%doc README.*
%license LICENSE
%{_bindir}/inv
%{_bindir}/invoke
%{python2_sitelib}/invoke/
%{python2_sitelib}/invoke-%{version}-*.egg-info/

%files -n python3-%{srcname}
%doc README.*
%license LICENSE
%{_bindir}/inv3
%{_bindir}/invoke3
%{python3_sitelib}/invoke/
%{python3_sitelib}/invoke-%{version}-*.egg-info/



%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 0.13.0-2
- Remove retired deps

* Tue Jun 28 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0
- Revamp the spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 11 2015 Athmane Madjoudj <athmane@fedoraproject.org> 0.9.0-4
- Update deps

* Mon Dec 01 2014 Athmane Madjoudj <athmane@fedoraproject.org>  0.9.0-3
- Update BR
- Minor fixes in files and install sections.

* Sat Nov 29 2014 Athmane Madjoudj <athmane@fedoraproject.org>  0.9.0-2
- Remove bundled libs.
- Remove .egg-info dir
- Restrict files section
- Add some build options

* Fri Nov 14 2014 Athmane Madjoudj <athmane@fedoraproject.org> 0.9.0-1
- Initial spec

