Name:           skipfish
Version:        2.10
Release:        0.10.b%{?dist}
Summary:        Web application security scanner

Group:          Applications/Internet

#Whole package licensed with ASL 2.0 license except 
#string-inl.h which has BSD type license
#icons which are licensed under LGPLv3
License:        ASL 2.0 and BSD and LGPLv3

URL:            http://code.google.com/p/skipfish/
Source0:        http://%{name}.googlecode.com/files/%{name}-%{version}b.tgz

#Use common paths and fedora build options and use fedora policy compiler flag
Patch1:         skipfish-2.10b-makefile-format-security.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  openssl-devel
BuildRequires:  libidn-devel
BuildRequires:  zlib-devel
BuildRequires:  pcre-devel

%description
High-performance, easy, and sophisticated Web application security testing
tool. It features a single-threaded multiplexing HTTP stack, heuristic 
detection of obscure Web frameworks, and advanced, differential security
checks capable of detecting blind injection vulnerabilities, stored XSS,
and so forth.

%prep
%setup -q -n %{name}-%{version}b
%patch1 -p1
cp -p assets/COPYING COPYING.icons


%build
sed -i 's|^// #define PROXY_SUPPORT|#define PROXY_SUPPORT|' src/config.h
make %{?_smp_mflags} CFLAGS="%{optflags}"



%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_datadir}/%{name}/assets/COPYING
rm -f doc/skipfish.1

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README 
%doc doc/
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/assets
%dir %{_datadir}/%{name}/dictionaries
%dir %{_datadir}/%{name}/signatures
%{_datadir}/%{name}/dictionaries/*
%{_datadir}/%{name}/signatures/*
%{_datadir}/%{name}/assets/index.html
%{_bindir}/%{name}
%{_bindir}/sfscandiff
%{_mandir}/man1/%{name}.1*



#Icons are licensed as LGPLv3 http://www.everaldo.com/crystal/
%doc COPYING.icons
%{_datadir}/%{name}/assets/*.png


%changelog
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-0.10.b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Athmane Madjoudj <athmane@fedoraproject.org>  2.10-0.9.b
- Enable proxy support

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-0.8.b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-0.7.b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-0.6.b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Athmane Madjoudj <athmane@fedoraproject.org> 2.10-0.5.b
- Fix bogus date

* Sun Dec 08 2013 Athmane Madjoudj <athmane@fedoraproject.org>  2.10-0.4.b
- Use -Werror=format-security flag (rhbz #1037329).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-0.3.b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-0.2.b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 07 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.10-0.1.b
- Update to 2.10b

* Sun Sep 02 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.09-0.1.b
- Update to 2.09b

* Sun Sep 02 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.08-0.2.b
- Add pcre-devel as build requirement.

* Sun Sep 02 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.08-0.1.b
- Update to 2.08b
- Update the patch and spec file to the new upstream source structure.

* Wed Jun 20 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.07-0.1.b
- Update to 2.07b
- Add sfscandiff comparison tool

* Sun Apr 08 2012 Michal Ambroz <rebus AT seznam.cz> - 2.05-0.1.b
- rebuild for version 2.05b
- removed the default skipfish.wl as this version no longer an option
- addedd manpage

* Mon Oct 03 2011 Michal Ambroz <rebus AT seznam.cz> - 2.03-0.1.b
- rebuild for version 2.03b

* Sun Mar 27 2011 Michal Ambroz <rebus AT seznam.cz> - 1.85-0.1.b
- rebuild for version 1.85b

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.84-0.2.b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Michal Ambroz <rebus AT seznam.cz> - 1.84-0.1.b
- rebuild for version 1.84b

* Sun Aug 08 2010 Michal Ambroz <rebus AT seznam.cz> - 1.54-0.1.b
- rebuild for version 1.54b

* Sun May 09 2010 Michal Ambroz <rebus AT seznam.cz> - 1.34-0.1.b
- update to new version

* Wed Apr 28 2010 Michal Ambroz <rebus AT seznam.cz> - 1.32-0.4.b
- use fixed patch for memory allocation from Tomas Mraz <tmraz at redhat.doc>

* Tue Apr 27 2010 Michal Ambroz <rebus AT seznam.cz> - 1.32-0.3.b
- use new patch for memory allocation from Tomas Mraz <tmraz at redhat.doc>

* Fri Apr 23 2010 Michal Ambroz <rebus AT seznam.cz> - 1.32-0.2.b
- fix memory allocation to be compliant with FORTIFY_SOURCE

* Sun Apr 18 2010 Michal Ambroz <rebus AT seznam.cz> - 1.32-0.1.b
- Update to 1.32b
- merge back to 1 package on request of Tomas Mraz <tmraz AT redhat.com>

* Sun Apr 18 2010 Michal Ambroz <rebus AT seznam.cz> - 1.31-0.3.b
- return explicit dir to files

* Sun Apr 18 2010 Michal Ambroz <rebus AT seznam.cz> - 1.31-0.2.b
- Incorporated comments from  Martin Gieseking <martin.gieseking AT uos.de>

* Sat Apr 17 2010 Michal Ambroz <rebus AT seznam.cz> - 1.31-0.1.b
- Update to 1.31b

* Sat Apr 10 2010 Michal Ambroz <rebus AT seznam.cz> - 1.30-0.1.b
- Update to 1.30b

* Mon Mar 29 2010 Michal Ambroz <rebus AT seznam.cz> - 1.29-0.1.b
- Update to 1.29b

* Mon Mar 29 2010 Michal Ambroz <rebus AT seznam.cz> - 1.26-0.2.b
- removed attr from the spec
- separate icons package with LGPLv3 license

* Thu Mar 25 2010 Michal Ambroz <rebus AT seznam.cz> - 1.26-0.1.b
- Update to 1.26b
- Incorporated comments from  Martin Gieseking <martin.gieseking AT uos.de>

* Thu Mar 25 2010 Michal Ambroz <rebus AT seznam.cz> - 1.25b-1
- Update to 1.25b

* Tue Mar 23 2010 Michal Ambroz <rebus AT seznam.cz> - 1.16b-1
- Initial build for Fedora 12

