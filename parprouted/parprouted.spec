%define real_version 0.7

Name:    parprouted
Version: 0.70
Release: 14%{dist}
License: GPLv2
Summary: Proxy ARP IP bridging daemon
Group:   Applications/Internet
URL:     http://www.hazard.maks.net/
Source0: http://www.hazard.maks.net/parprouted/%{name}-%{real_version}.tar.gz
Source1: scripts.tar.gz
Patch:   makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: iproute procps tunctl

%description
parprouted is a daemon for transparent IP (Layer 3) proxy ARP bridging.
Unlike standard bridging, proxy ARP bridging allows to bridge Ethernet
networks behind wireless nodes. Normal L2 bridging does not work between
wireless nodes because wireless does not know about MAC addresses used
in the wired Ethernet networks. Also this daemon is useful for making
transparent firewalls.

%prep
%setup -q -n %{name}-%{real_version}
%patch -p1 -b .makefile

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__tar} -zxf %{SOURCE1} -C %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README
%{_bindir}/%{name}*
%{_mandir}/man8/%{name}.8*

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 25 2008 Paulo Roma <roma@lcg.ufrj.br> - 0.70-3
- Added Requires: procps tunctl
- Created scripits parprouted-up.sh and parprouted-down.sh

* Tue Aug 05 2008 Paulo Roma <roma@lcg.ufrj.br> - 0.70-2
- Rebuilt for Fedora 8.
- Made setup quiet.
- Patched Makefile for installing on appropriate directories.
- Added Requires: iproute
- Upstream: Vladimir Ivaschenko <vi$maks,net>

* Mon Jan 28 2008 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.7.

* Sun Nov 27 2005 Dag Wieers <dag@wieers.com> - 0.63-1
- Initial package. (using DAR)
