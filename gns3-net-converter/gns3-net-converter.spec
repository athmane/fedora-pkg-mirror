Name:           gns3-net-converter
Version:        1.3.0
Release:        2%{?dist}
Summary:        Convert old ini-style GNS3 topologies to v1+ JSON format

License:        GPLv3
URL:            http://gns3.com
Source0:        https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires: python3-configobj

%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple 
workstations to powerful routers. 

GNS3 Converter is designed to convert old ini-style GNS3 topologies (<=0.8.7)
to the newer version v1+ JSON format for use in GNS3 v1+.

%prep
%autosetup 

%build
%py3_build

%install
%py3_install


%check
# Does not have one


%files 
%license COPYING
%doc README.rst ChangeLog
%{python3_sitelib}/gns3converter
%{python3_sitelib}/gns3_net_converter-*.egg-info
%{_bindir}/gns3-converter


%changelog
* Fri Jul 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.3.0-2
- Fix copy-paste issues
- Use pyhosted urls (more clean)

* Tue Jul 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.3.0-1
- Initial spec 
