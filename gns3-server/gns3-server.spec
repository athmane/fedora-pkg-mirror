Name:           gns3-server
Version:        1.5.1
Release:        1%{?dist}
Summary:        Graphical Network Simulator 3

License:        GPLv3
URL:            http://gns3.com
Source0:        https://github.com/GNS3/gns3-server/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        gns3.service
# Upstream PR #630
Patch0:         0001-Move-utils.vmnet-to-gns3-namespace.patch

BuildArch:      noarch
BuildRequires:  python3-devel
%{?systemd_requires}
BuildRequires: systemd
BuildRequires: git-core
BuildRequires: python-sphinx

#Requires: busybox
Requires: qemu-kvm 
Requires: docker 
Requires: python3-jsonschema 
Requires: python3-aiohttp 
Requires: python3-jinja2 
Requires: python3-raven
Requires: python3-psutil 
Requires: python3-zipstream


%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple 
workstations to powerful routers. 

This is the server package which provides an HTTP REST API for the client (GUI).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
%description doc
%{name}-doc package contains documentation.


%prep
%autosetup -S git
sed -i 's/aiohttp==0.21.5/aiohttp>=0.21.5/' requirements.txt

%build
%py3_build

%install
%py3_install

# Remove shebang
find %{buildroot}/%{python3_sitelib}/ -name '*.py' -print \
   -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} \;

# Remove bundled busybox/docker resources
# TODO: fix the code to use system's busybox
rm %{buildroot}/%{python3_sitelib}/gns3server/modules/docker/resources/bin/*
rm %{buildroot}/%{python3_sitelib}/gns3server/modules/docker/resources/init.sh
rm %{buildroot}/%{python3_sitelib}/gns3server/modules/docker/resources/etc/udhcpc/default.script

# Build the docs
%{make_build} -C docs html
/bin/rm -f docs/_build/html/.buildinfo

## Systemd service part
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
mkdir -p  %{buildroot}%{_sharedstatedir}/gns3

%check


%files 
%license LICENSE
%doc README.rst AUTHORS CHANGELOG
%{python3_sitelib}/gns3_server-%{version}-py*.egg-info/
%{python3_sitelib}/gns3server/
%{_bindir}/gns3server
%{_bindir}/gns3vmnet
%{_unitdir}/gns3.service
%dir %attr(2755,gns3,gns3) %{_sharedstatedir}/gns3

%files doc
%license LICENSE
%doc docs/_build/html

%pre 
getent group gns3 >/dev/null || groupadd -r gns3
getent passwd gns3 >/dev/null || \
       useradd -r -g gns3 -d /var/lib/gns3 -s /sbin/nologin \
               -c "gns3 server" gns3
exit 0

%post 
[ -d "/var/lib/gns3" ] && chown -R gns3:gns3 %{_sharedstatedir}/gns3
%systemd_post gns3.service

%preun 
%systemd_preun gns3.service

%postun  
%systemd_postun_with_restart gns3.service

%changelog
* Tue Aug 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-4
- Fix typo in egg dir
- Build/ship the doc
- update BR

* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org>  - 1.5.0-3
- Spec cleanup
- Add patch to move vmnet to gns3 namespace.
- Merge service sub pkg (too small)

* Thu Jul 07 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-2
- Minor spec fixes
- Provide a systemd service

* Tue Jul 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-1
- Initial spec 
