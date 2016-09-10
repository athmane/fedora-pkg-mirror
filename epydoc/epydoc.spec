Summary: Automatic API documentation generation tool for Python
Name: epydoc
Version: 3.0.1.20090203svn
Release: 4%{?dist}
Group: Development/Tools
License: MIT
URL: http://epydoc.sourceforge.net/
Source0: http://dl.sf.net/epydoc/epydoc-%{version}.tar.gz
Source1: epydocgui.desktop
Patch0: epydoc-3.0.1-nohashbang.patch
Patch1: epydoc-3.0.1svn1812-png-default.patch
Patch2: epydoc-3.0.1-new-docutils.patch
Patch3: epydoc-3.0.1svn1812-make-suppress-timestamp-the-default.patch
Patch4: epydoc-3.0.1svn1812-fix-relative-import.patch
# Needed for some outputs, like --pdf (#522249)
Recommends: tex(dvips)
Recommends: tex(latex)
BuildRequires: python-devel
BuildRequires: desktop-file-utils
BuildArch: noarch

%description
Epydoc  is a tool for generating API documentation for Python modules,
based  on their docstrings. For an example of epydoc's output, see the
API  documentation for epydoc itself (html, pdf). A lightweight markup
language  called  epytext can be used to format docstrings, and to add
information  about  specific  fields,  such as parameters and instance
variables.    Epydoc    also   understands   docstrings   written   in
ReStructuredText, Javadoc, and plaintext.

%package doc
Summary: Documentation for epydoc
Requires: %{name} = %{version}-%{release}
%description doc
epydoc-doc package contains documentation.

%package gui
Summary: Graphical user interfacefor epydoc
Requires: %{name} = %{version}-%{release}
Requires: tkinter
%description gui
epydoc-gui package contains Graphical user interface for epydoc



%prep
%setup -q 
# Clean scm files
rm -rf epydoc/doc/.cvsignore
%patch0 -p1 -d epydoc/src/ -b .nohashbang
%patch1 -p1 -b .default-png
%patch2 -p1 -d epydoc/src/ -b .new-docutils
%patch3 -p1 -b .no-timestamp
%patch4 -p0 -d epydoc/src/ -b .fix-relative-import


%build
cd epydoc/src/
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
cd epydoc/src/
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

desktop-file-install \
    --vendor="" \
    --dir=%{buildroot}%{_datadir}/applications \
    --mode=0644 \
    %{SOURCE1}

# Prevent having *.pyc and *.pyo in _bindir
%{__mv} %{buildroot}%{_bindir}/apirst2html.py %{buildroot}%{_bindir}/apirst2html

# Also install the man pages
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__install} -p -m 0644 ../man/*.1 %{buildroot}%{_mandir}/man1/



%clean
%{__rm} -rf %{buildroot}


%files
%doc epydoc/src/README.txt
%license epydoc/src/LICENSE.txt
%{_bindir}/apirst2html
%{_bindir}/epydoc
%{python_sitelib}/epydoc/
%{python_sitelib}/epydoc-*.egg-info
%{_mandir}/man1/epydoc.1*

%files doc
%doc epydoc/doc

%files gui
%{_bindir}/epydocgui
%{_datadir}/applications/epydocgui.desktop
%{_mandir}/man1/epydocgui.1*


%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1.20090203svn-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 26 2016 Athmane Madjoudj <athmane@fedoraproject.org> 3.0.1.20090203svn-3
- Use Recommends for tex dependencies
- Minor spec fixes
- Split gui sub-pkg

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.20090203svn-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015  Athmane Madjoudj <athmane@fedoraproject.org> 3.0.1.20090203svn-1
- Update to trunk
- Add patch to remove timestamp for reproducible builds (RHBZ #1122654)
- Rebase default img format patch
- Fix bugus date/time in the changelog
- Add patch to fix relative import parsing (RHBZ #1166283)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Rex Dieter <rdieter@fedoraproject.org> 3.0.1-12
- Requires: tex(dvips) tex(latex)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Apr 13 2010 Lubomir Rintel <lkundrak@v3.sk> 3.0.1-7
- Fix crash with newer docutils (#578920)

* Tue Dec  8 2009 Matthias Saou <http://freshrpms.net/> 3.0.1-6
- Add texlive-dvips and texlive-latex requirements (#522249).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 3.0.1-3
- Include patch to use png instead of gif for generated images (#459857).

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.0.1-2
- Rebuild for Python 2.6

* Sat Mar 22 2008 Matthias Saou <http://freshrpms.net/> 3.0.1-1
- Update to 3.0.1.
- Update nohashbang patch.
- Include new apirst2html script, but remove .py extension to avoid .pyc/pyo.
- Include egg-info file.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 2.1-8
- Remove desktop file prefix and X-Fedora category.
- Include patch to remove #! python from files only meant to be included.

* Mon Dec 11 2006 Matthias Saou <http://freshrpms.net/> 2.1-7
- Rebuild against python 2.5.
- Remove no longer needed explicit python-abi requirement.
- Change python build requirement to python-devel, as it's needed now.

* Wed Sep  6 2006 Matthias Saou <http://freshrpms.net/> 2.1-6
- No longer ghost the .pyo files, as per new python guidelines (#205374).

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 2.1-5
- FC6 rebuild.
- Add %%{?dist} tag.
- Update summary line.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Dec 20 2004 Ville Skyttä <ville.skytta at iki.fi> - 2.1-3
- Change to noarch.
- Get Python site-packages dir from distutils, should fix x86_64 build.
- Require python-abi and tkinter.
- %%ghost'ify *.pyo.
- Fix man page permissions.
- Add menu entry for epydocgui.

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 2.1-2
- Bump release to provide Extras upgrade path.

* Thu Oct 21 2004 Matthias Saou <http://freshrpms.net/> 2.1-1
- Picked up and rebuilt.
- Added doc and man pages.

* Fri May 07 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 2.1-0.fdr.1: Initial package

