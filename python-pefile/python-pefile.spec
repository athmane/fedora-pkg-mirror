Name:           python-pefile
# upstream version embeds a dash, we replace this with an underscore:
Version:        1.2.10_139
Release:        5%{?dist}
Summary:        Python module for working with Portable Executable files
License:        MIT
URL:            http://code.google.com/p/pefile/

%global realver $(echo %{version} | tr "_" "-")

Source0:        http://pefile.googlecode.com/files/pefile-%{realver}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
pefile is a multi-platform Python module to read and work with Portable 
Executable (aka PE) files. Most of the information in the PE Header is 
accessible, as well as all the sections, section's information and data.

pefile requires some basic understanding of the layout of a PE file. Armed 
with it it's possible to explore nearly every single feature of the file.

Some of the tasks that pefile makes possible are:

* Modifying and writing back to the PE image
* Header Inspection
* Sections analysis
* Retrieving data
* Warnings for suspicious and malformed values
* Packer detection with PEiD’s signatures
* PEiD signature generation

%prep
%setup -qn pefile-%{realver}

# Fix end-of-line encoding of the license file:
sed -i 's/\r//' COPYING

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc COPYING README
%{python2_sitelib}/*

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_139-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10_139-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_139-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_139-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 07 2014 Christopher Meng <rpm@cicku.me> - 1.2.10_139-1
- Update to 1.2.10_139

* Thu Aug 08 2013 Christopher Meng <rpm@cicku.me> - 1.2.10_123-1
- Update to 1.2.10_123

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.10_63-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  8 2009 David Malcolm <dmalcolm@redhat.com> - 1.2.10_63-1
- initial packaging

