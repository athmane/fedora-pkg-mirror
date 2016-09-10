Summary:        Very fast network log-on cracker
Name:           hydra
Version:        8.3
Release:        1%{?dist}
License:        AGPLv3 with exceptions
URL:            https://www.thc.org/thc-hydra/
Source0:        https://github.com/vanhauser-thc/thc-hydra/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        xhydra.desktop
# Upstream provides non-transparent jpeg
Source2:        xhydra.png
# Sent upstream via email 20120518
Patch0:         hydra-use-system-libpq-fe.patch
Patch1:         hydra-fix-dpl4hydra-dir.patch


BuildRequires: openssl-devel, apr-devel, libssh-devel, libidn-devel
BuildRequires: subversion-devel, postgresql-devel, pcre-devel, gtk2-devel
BuildRequires: desktop-file-utils, firebird-devel, mysql-devel 

%description
Hydra is a parallelized log-in cracker which supports numerous protocols to 
attack. New modules are easy to add, beside that, it is flexible and very fast.

This tool gives researchers and security consultants the possibility to show 
how easy it would be to gain unauthorized access from remote to a system.

%package frontend
Summary: The GTK+ front end for hydra
Requires: hydra = %{version}-%{release}
BuildRequires: gtk2-devel, pkgconfig
%description frontend
This package includes xhydra, a GTK+ front end for hydra. 

%prep
%setup -qn thc-hydra-%{version}

%patch0 -p0
%patch1 -p0

#fix permissions - already fixed upstream in 8.3-dev
chmod -x *.csv hydra-gtk/src/*.c hydra-gtk/src/*.h


%build
%configure --nostrip
make %{?_smp_mflags}

%install

make install DESTDIR="%{buildroot}" PREFIX="" BINDIR="%{_bindir}" MANDIR="%{_mandir}/man1" DATADIR="%{_datadir}/%{name}"

mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
install -m 644 -p %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1};

# Fix dpl4hydra.sh (w/o buildroot prefix)
sed -i 's|^INSTALLDIR=.*|INSTALLDIR=/usr|' %{buildroot}/%{_bindir}/dpl4hydra.sh


%files
%doc CHANGES LICENSE LICENSE.OPENSSL README
%{_bindir}/hydra
%{_bindir}/pw-inspector
%{_bindir}/hydra-wizard.sh
%{_bindir}/dpl4hydra.sh
%{_mandir}/man1/hydra*
%{_mandir}/man1/pw-inspector*
%{_datadir}/%{name}/dpl4hydra*.csv
%dir %{_datadir}/%{name}

%files frontend
%{_bindir}/xhydra
%{_mandir}/man1/xhydra*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Fri Aug 12 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 8.3-1
- Update to 8.3
- FIx URL since upstream now uses git tags

* Fri Jun 17 2016 Michal Ambroz <rebus _at seznam.cz>  8.2-1
- Update to 8.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 21 2014 Athmane Madjoudj <athmane@fedoraproject.org>  8.1-1
- Update to 8.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Athmane Madjoudj <athmane@fedoraproject.org> 8.0-1
- Update to 8.0

* Mon Dec 30 2013 Athmane Madjoudj <athmane@fedoraproject.org> 7.6-1
- Update to 7.6
- Include hydra-wizard script (new in 7.6) 
- Fix icon filename
- Add a png icon since upstream only provides non-transparent jpeg

* Mon Nov 18 2013 Athmane Madjoudj <athmane@fedoraproject.org> 7.5-2
- Use new source file from upstream (contains minor license file fixes)

* Sun Aug 04 2013 Athmane Madjoudj <athmane@fedoraproject.org> 7.5-1
- Update to 7.5
- Update license tag.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Athmane Madjoudj <athmane@fedoraproject.org> 7.4.2-1
- Update to 7.4.2

* Sun Dec 23 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.4-1
- Update to 7.4
- Remove s390x patch (upstreamed)

* Sat Dec 22 2012 Dan Horák <dan[at]danny.cz> 7.3-13
- s390x is 64-bit arch

* Mon Sep 10 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.3-12
- Remove dep on ncpfs-devel since it's a dead upstream.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.3-10
- Fix binaries striping issue (#825860)

* Tue May 22 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.3-9
- Update to 7.3
- Drop some patches since they're included in 7.3
- Add two patches to fix makefile and dpl4hydra

* Fri May 18 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-8
- Add LICENSE.OPENSSL
- Add /usr/share/hydra
- Add a patch to use system provided libpq-fe headers (provided by 
  postgresql-devel)

* Tue Apr 17 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-7
- Add DESTDIR support
- Include dpl4hydra

* Mon Apr 16 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-6
- Reverse a patch because it breaks brute-forcing NTLM-enabled services 
  (upstream confirmed that it's not necessary)

* Tue Mar 13 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-5
- Add patch to support mysql
- Add patch to fix warnings

* Thu Mar 08 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-4
- Preserve timestamps on install
- Remove extra arg in desktop file install

* Sat Feb 11 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-3
- Add support for CFLAGS

* Sat Feb 11 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-2
- Clean-up the descriptions
- Add Firebird support

* Sat Feb 11 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-1
- Update to 7.2

* Tue Dec 27 2011 Athmane Madjoudj <athmane@fedoraproject.org> 7.1-3
- Remove rm -rf buildroot

* Thu Dec 22 2011 Athmane Madjoudj <athmane@fedoraproject.org> 7.1-2
- Update license to GPLv3 with OpenSSL exception

* Thu Dec 22 2011 Athmane Madjoudj <athmane@fedoraproject.org> 7.1-1
- Update to recent version
- Clean-up the spec file
- Add desktop file for the frontend

* Sun Jul 04 2010 Marcus Haebler <haebler@gmail.com> - 0:5.7-0
- Initial RPM build 
