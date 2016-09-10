%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_includedir}/httpd/.mmn || echo missing-httpd-devel)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}


Name: mod_ruid2
Version: 0.9.8
Release: 4%{?dist}
Summary: A suexec module for Apache

License: ASL 2.0
URL: http://sourceforge.net/projects/mod-ruid/
Source0: http://downloads.sourceforge.net/project/mod-ruid/mod_ruid2/mod_ruid2-%{version}.tar.bz2
Source1: mod_ruid2.conf
Source2: 10-mod_ruid2.conf

BuildRequires: httpd-devel libcap-devel

Requires: httpd
Requires: httpd-mmn = %{_httpd_mmn}

%description
mod_ruid2 is a suexec module for Apache which takes advantage of 
POSIX.1e capabilities to increase performance.

%prep
%setup -q


%build
apxs -l cap -c %{name}.c


%install
mkdir -p %{buildroot}%{_httpd_confdir}
mkdir -p %{buildroot}%{_libdir}/httpd/modules
install -m 700 -d %{buildroot}%{_localstatedir}/lib/%{name}

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
# 2.4-style
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_httpd_modconfdir}/10-mod_ruid2.conf
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_httpd_confdir}/mod_ruid2.conf
%else
# 2.2-style
install -d -m0755 %{buildroot}%{_httpd_confdir}
cat %{SOURCE2} %{SOURCE1} > %{buildroot}%{_httpd_confdir}/mod_ruid2.conf
%endif
install -m 755 .libs/mod_ruid2.so %{buildroot}%{_httpd_moddir}


%files
%doc README
%{_httpd_moddir}/mod_ruid2.so
%config(noreplace) %{_httpd_confdir}/*.conf

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
    %config(noreplace) %{_httpd_modconfdir}/*.conf
%endif

%{!?_licensedir:%global license %%doc}
%license LICENSE

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Athmane Madjoudj <athmane@fedoraproject.org> 0.9.8-2
- Fix license issue
- Add a workarround for epel 

* Sun Apr 20 2014 Athmane Madjoudj <athmane@fedoraproject.org> 0.9.8-1
- Initial spec.

