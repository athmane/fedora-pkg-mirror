Name: thc-ipv6
Version: 3.0
Release: 2%{?dist}
Summary: An toolkit for attacking the IPv6 protocol suite

License: AGPLv3 with exceptions
URL: https://www.thc.org/thc-ipv6/
Source0: http://www.thc.org/releases/thc-ipv6-%{version}.tar.gz

BuildRequires:  libpcap-devel openssl-devel libnetfilter_queue-devel
BuildRequires:  perl-generators

%description
A complete tool set to attack the inherent protocol weaknesses of IPV6
and ICMP6, and includes an easy to use packet factory library.

%prep
%setup -q -n thc-ipv6-%{version}


%build

sed -i "s|^PREFIX=/usr/local|PREFIX=/usr|" Makefile 
sed -i "s/^STRIP=strip/STRIP=echo/" Makefile 
sed -i "/^CFLAGS=-O2/d" Makefile 
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
make install DESTDIR=%{buildroot}


%files
%doc CHANGES LICENSE LICENSE.OPENSSL README HOWTO-INJECT
%{_bindir}/*
%{_mandir}/man8/thc-ipv6*

%changelog
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Athmane Madjoudj <athmane@fedoraproject.org> 3.0-1
- Update to 3.0
- Add new deps
- Do not strip binaries 

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Athmane Madjoudj <athmane@fedoraproject.org> 2.7-1
- Update to 2.7

* Fri Jul 25 2014 Athmane Madjoudj <athmane@fedoraproject.org> 2.5-2
- Rename the package properly

* Wed Apr 16 2014 Athmane Madjoudj <athmane@fedoraproject.org> 2.5-1
- Initial specfile

