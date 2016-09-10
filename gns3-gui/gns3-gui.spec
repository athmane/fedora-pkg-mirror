Name:           gns3-gui
Version:        1.5.1
Release:        2%{?dist}
Summary:        GNS3 graphical user interface

License:        GPLv3+
URL:            http://gns3.com
Source0:        https://github.com/GNS3/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        gns3.png
Source3:        %{name}.appdata.xml

BuildArch:      noarch

BuildRequires:  python3-devel 
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires: telnet 
Requires: cpulimit 
Requires: socat
Requires: python3-jsonschema 
Requires: python3-raven 
Requires: python3-psutil 
Requires: python3-qt5
Requires: gns3-net-converter >= 1.3.0

%description
GNS3 is a graphical network simulator that allows you to design complex network
topologies. You may run simulations or configure devices ranging from simple 
workstations to powerful routers. 

This package contains the client graphical user interface.

%prep
%autosetup 

%build
%py3_build

%install
%py3_install

# Remove shebang
for lib in `find %{buildroot}/%{python3_sitelib}/ -name '*.py'`; do
 echo $lib
 sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done

# Remove empty files
find %{buildroot}/%{python3_sitelib}/ -name '.keep' -type f -delete

# Remove exec perm
find %{buildroot}/%{python3_sitelib}/ -type f -exec chmod -x {} \;

# Desktop file
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/
desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}

# AppData
mkdir -p %{buildroot}/%{_datadir}/appdata/
install -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/appdata/

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml


%files 
%license LICENSE
%doc README.rst AUTHORS CHANGELOG
%{python3_sitelib}/gns3/
%{python3_sitelib}/gns3_gui-*-py*.egg-info/
%{_bindir}/gns3
%{_bindir}/gns3-iouvm-converter
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/gns3.png
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Fri Aug 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.1-2
- Fix appdata

* Tue Aug 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1
- Fix the url

* Tue Aug 02 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-2
- Minor spec fixes
- Provide AppData

* Tue Jul 05 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 1.5.0-1
- Initial spec 
