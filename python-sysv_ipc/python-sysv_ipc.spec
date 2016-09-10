%global srcname sysv_ipc
%global sum System V IPC for Python - Semaphores, Shared Memory and Message Queues
%global desc The sysv_ipc module which gives Python access to System V inter-process\
semaphores, shared memory and message queues on systems that support them.

Name:           python-%{srcname}
Version:        0.7.0
Release:        2%{?dist}
Summary:        %{sum}
License:        GPLv3+
URL:            http://semanchuk.com/philip/%{srcname}/
Source0:        https://pypi.python.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildRequires:  python2-devel python3-devel

%description
%{desc}

%package examples
Summary:    Examples for Python sysv_ipc module
Requires:   %{name} = %{version}-%{release}

%description examples
This module comes with two demonstration apps. 

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{desc}


%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%prep
%setup -q -n sysv_ipc-%{version}

%build
%{__python2} setup.py build
%{__python3} setup.py build


%install
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
chmod -x demo*/*.{py,sh}
#sed -i -e '/^#!\//, 1d'  demo/mk.sh 



%files -n python2-%{srcname}
%license LICENSE 
%doc LICENSE README ReadMe.html VERSION
%{python2_sitearch}/*
%{python2_sitearch}/%{srcname}-%{version}-*.egg-info

%files -n python3-%{srcname}
%license LICENSE 
%doc LICENSE README ReadMe.html VERSION
%{python3_sitearch}/*
%{python3_sitearch}/%{srcname}-%{version}-*.egg-info


%files examples
%doc demo/ demo2/

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 18 2016 Athmane Madjoudj <athmane@fedoraproject.org> 0.7.0-1
- Update to 0.7.0
- Revamp the spec file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 10 2015 Athmane Madjoudj <athmane@fedoraproject.org> 0.4.2-13
- Use unversioned docdir  (RHBZ #994063)
- Fix some packaging issues

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.2-4
- further generalize the egginfo manifest so it works with any python 2 minor
version

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Sep 25 2009 Steven Fernandez <lonetwin@fedoraproject.org> - 0.4.2-2
- Spec file fix. Use correct python version for egg-info file

* Sat Aug 29 2009 Steven Fernandez <lonetwin@fedoraproject.org> - 0.4.2-1
- Initial build
