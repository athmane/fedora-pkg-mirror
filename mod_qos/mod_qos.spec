%{!?_httpd_apxs: %{expand: %%global _httpd_apxs %%{_sbindir}/apxs}}
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}


Name:           mod_qos
Version:        11.31
Release:        1%{?dist}
Summary:        Quality of service module for Apache

Group:          System Environment/Daemons
License:        GPLv2
URL:            http://opensource.adnovum.ch/mod_qos/
Source0:        http://downloads.sourceforge.net/project/mod-qos/%{name}-%{version}.tar.gz
Source1:        10-mod_qos.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  httpd-devel >= 2.0.0 
BuildRequires:  pcre-devel, openssl-devel, libpng-devel

BuildRequires:  automake
Requires:       httpd-mmn = %{_httpd_mmn}

%description
The mod_qos module may be used to determine which requests should be served and 
which shouldn't in order to avoid resource over-subscription. The module 
collects different attributes such as the request URL, HTTP request and response
headers, the IP source address, the HTTP response code, history data (based on 
user session and source IP address), the number of concurrent requests to the 
server (total or requests having similar attributes), the number of concurrent 
TCP connections (total or from a single source IP), and so forth.

Counteractive measures to enforce the defined rules are: request blocking, 
dynamic timeout adjustment, request delay, response throttling, and dropping of 
TCP connections. 


%prep
%setup -q -n %{name}-%{version}

%build
%{_httpd_apxs} -Wc,"%{optflags}" -c apache2/mod_qos.c -lcrypto -lpcre

# Tools building
# Need to fix the binaries

pushd .
cd tools/
aclocal
automake --add-missing
%configure
make %{?_smp_mflags}
popd


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 apache2/.libs/mod_qos.so \
    $RPM_BUILD_ROOT%{_libdir}/httpd/modules/mod_qos.so

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
    # 2.4-style
    install -Dpm 644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}/10-mod_qos.conf
%else
    # 2.2-style
    install -Dpm 644 %{SOURCE1} %{buildroot}%{_httpd_confdir}/mod_qos.conf
%endif

cd tools/
%make_install
install -d %{buildroot}%{_mandir}/man1/
install -Dpm 644 man1/*  %{buildroot}%{_mandir}/man1/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%doc doc README.TXT
%{_libdir}/httpd/modules/mod_qos.so
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
    # 2.4-style
    %config(noreplace)  %{_httpd_modconfdir}/10-mod_qos.conf
%else
    # 2.2-style
    %config(noreplace) %{_httpd_confdir}/mod_qos.conf
%endif


%changelog
* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.31-1
- Update to 11.31

* Sat Jun 25 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.30-1
- Update to 11.30

* Fri Jun 10 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.29-1
- Update to 11.29

* Fri Apr 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 11.26-1
- Update to 11.26

* Tue Apr 12 2016 Athmane Madjoudj <athmane@fedoraproject.org> 11.24-1
- Update to 11.24

* Fri Feb 26 2016 Athmane Madjoudj <athmane@fedoraproject.org> 11.22-1
- Update to 11.22

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Athmane Madjoudj <athmane@fedoraproject.org> 11.21-1
- Update to 11.21

* Sat Jan 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> 11.19-1
- Update to 11.19

* Fri Nov 20 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.18-1
- Update to 11.18
- Enable all tools

* Fri Oct 02 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.17-1
- Update to 11.17

* Sat Aug 15 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.16-1
- Update to 11.16

* Mon Jul 20 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.15-1
- Update to 11.15

* Sat Jun 20 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.14-1
- Update to 11.14

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.13-1
- Update to 11.13

* Thu Mar 05 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.12-1
- Update to 11.12

* Sat Feb 21 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.11-1
- Update to 11.11

* Fri Jan 30 2015 Athmane Madjoudj <athmane@fedoraproject.org> 11.9-1
- Update to 11.9

* Thu Nov 27 2014 Athmane Madjoudj <athmane@fedoraproject.org> 11.7-1
- Update to 11.7

* Fri Nov 14 2014  Athmane Madjoudj <athmane@fedoraproject.org> 11.6-1
- Update to 11.6

* Fri Oct 10 2014 Athmane Madjoudj <athmane@fedoraproject.org> 11.5-1
- Update to 11.5
- Include the tools
- Exclude some utilities util they get audited because of suid/guid related calls
- Follow the new httpd 2.4.x module packaging guidelines.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 10.24-2
- fix _httpd_mmn expansion in absence of httpd-devel

* Sat Nov  2 2013 Christof Damian <christof@damian.net> - 10.24-1
- upstream 10.24

* Thu Jul 25 2013 Christof Damian <christof@damian.net> - 10.16-1
- upstream 10.16

* Sat Apr 27 2013 Christof Damian <christof@damian.net> - 10.15-1
- upstream 10.15

* Sat Feb 23 2013 Christof Damian <christof@damian.net> - 10.13-4
- add crypto requirement

* Tue Jan  8 2013 Christof Damian <christof@damian.net> - 10.13-3
- update build requires

* Tue Jan  8 2013 Christof Damian <christof@damian.net> - 10.13-2
- add conf file

* Tue Jan  8 2013 Christof Damian <christof@damian.net> - 10.13-1
- initial package

