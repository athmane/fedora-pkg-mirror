Name:           ratproxy
Version:        1.58
Release:        11%{?dist}
Summary:        A passive web application security assessment tool
Group:          Applications/Internet
License:        ASL 2.0
URL:            http://code.google.com/p/%{name}/
# URL of actual source containing binary
# generate-tarball.sh removes that binary and makes source0 tarball.
Source0:        ratproxy-1.56-nobinary.tar.gz
Source1:        generate-tarball.sh
Patch0:        ratproxy-report-full-path-to-image.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  openssl-devel

%description
A semi-automated, largely passive web application security audit tool,
optimized for an accurate and sensitive detection, and automatic
annotation, of potential problems and security-relevant design
patterns based on the observation of existing, user-initiated traffic
in complex web 2.0 environments.
             Detects and prioritizes broad classes of security
problems, such as dynamic cross-site trust model considerations,
script inclusion issues, content serving problems, insufficient XSRF
and XSS defenses, and much more.

%prep
%setup -q -n %{name}
%patch0

%build
sed -i -e 's@-O3@-O2@' Makefile
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -Wno-pointer-sign"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
install -p %{name} $RPM_BUILD_ROOT/%{_bindir}/
install -p ratproxy-report.sh $RPM_BUILD_ROOT/%{_bindir}/ratproxy-report
install -Dp ratproxy-back.png $RPM_BUILD_ROOT/%{_datadir}/%{name}/images/ratproxy-back.png
rm doc/Solaris.README
chmod 644 doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/%{name}
%{_bindir}/ratproxy-report
%{_datadir}/%{name}/*

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.58-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 1.58-2
- rebuilt with new openssl

* Thu Aug 27 2009 Rakesh Pandit <rakesh@fedorapeople.org> - 1.58-1
- Adjusted Steve's patch for updateing to 1.58 # 518542

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1.56-1
- Updated to 1.56

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 08 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.51-4
- removed Solaris.README

* Thu Jan 08 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.51-3
- removed non free binary from tar.gz and re-compressed (generate-tarball.sh).

* Sat Nov 08 2008 Rakesh Pandit <rakesh@fedoraproject.org> 1.51-2
- corrected make flags

* Wed Nov 05 2008 Rakesh Pandit <rakesh@fedoraproject.org> 1.51-1
- Initial package
