%global with_extras 0%{?fedora} || 0%{?rhel} <= 6

%global commit f16e0b1726c843889b9f024e27fd794147594677
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Summary: ModSecurity Rules
Name: mod_security_crs
Version: 2.2.9.20160414git
Release: 1%{?dist}
License: ASL 2.0
URL: https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project
Group: System Environment/Daemons
Source: https://github.com/SpiderLabs/owasp-modsecurity-crs/archive/%{commit}/owasp-modsecurity-crs-%{shortcommit}.tar.gz
BuildArch: noarch
Requires: mod_security >= 2.7.0

%description
This package provides the base rules for mod_security.

%if %with_extras
%package        extras
Summary:        Supplementary mod_security rules 
Group:          System Environment/Daemons
Requires:       %name = %version-%release

%description    extras
This package provides supplementary rules for mod_security.
%endif

%prep
%setup -q -n owasp-modsecurity-crs-%{commit}

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/
install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules

install -d %{buildroot}%{_prefix}/lib/modsecurity.d/base_rules

%if %with_extras
install -d %{buildroot}%{_prefix}/lib/modsecurity.d/optional_rules
install -d %{buildroot}%{_prefix}/lib/modsecurity.d/experimental_rules
install -d %{buildroot}%{_prefix}/lib/modsecurity.d/slr_rules
%endif

install -m0644 modsecurity_crs_10_setup.conf.example %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/modsecurity_crs_10_config.conf
install -m0644 base_rules/* %{buildroot}%{_prefix}/lib/modsecurity.d/base_rules/


%if %with_extras
install -m0644 optional_rules/* %{buildroot}%{_prefix}/lib/modsecurity.d/optional_rules/
install -m0644 experimental_rules/* %{buildroot}%{_prefix}/lib/modsecurity.d/experimental_rules/
install -m0644 slr_rules/* %{buildroot}%{_prefix}/lib/modsecurity.d/slr_rules
%endif

# activate base_rules
for f in `ls %{buildroot}/%{_prefix}/lib/modsecurity.d/base_rules/` ; do 
    ln -s %{_prefix}/lib/modsecurity.d/base_rules/$f %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules/$f; 
done

%clean
rm -rf %{buildroot}


%files
%doc CHANGES INSTALL LICENSE README.md
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/activated_rules/*
%config(noreplace) %{_sysconfdir}/httpd/modsecurity.d/modsecurity_crs_10_config.conf
%{_prefix}/lib/modsecurity.d/base_rules


%if %with_extras
%files extras
%{_prefix}/lib/modsecurity.d/optional_rules
%{_prefix}/lib/modsecurity.d/experimental_rules
%{_prefix}/lib/modsecurity.d/slr_rules
%endif

%changelog
* Fri Apr 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.9.20160414git-1
- Update to 2.9.20160414git

* Tue Mar 08 2016 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.9.20160219git-1
- Update to 2.2.9
- Minor spec cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 02 2013 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.8-1
- Update to 2.2.8
- Adapt the spec file to new github tarball schema.
- Correct bugus date in the spec file.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Peter Vrabec <pvrabec@redhat.com> 2.2.6-4
- "extras" subpackage is not provided on RHEL7

* Wed Oct 17 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.6-3
- Remove the patch since we're requiring mod_security >= 2.7.0
- Require mod_security >= 2.7.0

* Mon Oct 01 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.6-2
- Add a patch to fix incompatible rules.
- Update to new git release

* Sat Sep 15 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.6-1
- Update to 2.2.6
- Update spec file since upstream moved to Github.

* Thu Sep 13 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.5-5
- Enable extra rules sub-package for EPEL.

* Tue Aug 28 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.5-4
- Fix spec for el5

* Tue Aug 28 2012 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.5-3
- Add BuildRoot def for el5 compatibility

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Peter Vrabec <pvrabec@redhat.com> 2.2.5-1
- upgrade

* Wed Jun 20 2012 Peter Vrabec <pvrabec@redhat.com> 2.2.4-3
- "extras" subpackage is not provided on RHEL

* Thu May 03 2012 Peter Vrabec <pvrabec@redhat.com> 2.2.4-2
- fix fedora-review issues (#816975)

* Thu Apr 19 2012 Peter Vrabec <pvrabec@redhat.com> 2.2.4-1
- initial package


