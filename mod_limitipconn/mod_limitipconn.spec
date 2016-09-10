%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}

Summary: Simultaneous connection limiting module for Apache
Name: mod_limitipconn
Version: 0.23
Release: 17%{?dist}
Group: System Environment/Daemons
License: ASL 2.0
URL: http://dominia.org/djao/limitipconn2.html
Source0: http://dominia.org/djao/limit/mod_limitipconn-%{version}.tar.bz2
Source1: mod_limitipconn.conf
Patch0: mod_limitipconn-0.23-httpd24.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: httpd-mmn = %{_httpd_mmn}
BuildRequires: httpd-devel

%description
Apache module which allows web server administrators to limit the number of
simultaneous downloads permitted from a single IP address. 

%prep
%setup -q

%patch0 -p1 -b .httpd24

%build
%{_httpd_apxs} -Wc,"%{optflags}" -c mod_limitipconn.c


%install
rm -rf %{buildroot}

%if "%{_httpd_modconfdir}" == "%{_httpd_confdir}"
# httpd <= 2.2.x
install -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_httpd_modconfdir}/limitipconn.conf
%else
# httpd >= 2.4.x
install -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_httpd_modconfdir}/10-limitipconn.conf
%endif
install -D -p -m 0755 .libs/mod_limitipconn.so \
    %{buildroot}%{_httpd_moddir}/mod_limitipconn.so


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README INSTALL LICENSE
%config(noreplace) %{_httpd_modconfdir}/*.conf
%{_httpd_moddir}/mod_limitipconn.so


%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 0.23-13
- fix _httpd_mmn expansion in absence of httpd-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Joe Orton <jorton@redhat.com> - 0.23-9
- add _httpd_moddir compat macro as well (#809730)

* Tue Apr 17 2012 Joe Orton <jorton@redhat.com> - 0.23-8
- improve handling of absent content-type w/2.4

* Tue Apr 17 2012 Joe Orton <jorton@redhat.com> - 0.23-7
- update for 2.4 (patch from Jan Kaluza, #809730)

* Thu Mar 29 2012 Matthias Saou <http://freshrpms.net/> 0.23-6
- Rebuild for new apache httpd... not, we will require patching.
- Use rpm macros provided by the httpd-devel package, with sane fallbacks.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  1 2008 Matthias Saou <http://freshrpms.net/> 0.23-1
- Initial RPM release.

