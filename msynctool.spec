Name:		msynctool
Version:	0.22
Epoch:		1
Release:	%mkrel 10
Summary:	CLI for synchronization with OpenSync
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.opensync.org
Source0:	%{name}-%{version}.tar.bz2
Obsoletes:	multisync-cli
Obsoletes:	multisync
BuildRequires:	libopensync-devel < 0.30
Requires:	libopensync >= %{epoch}:%{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Command line synchronization tool for the OpenSync framework. To allow
synchronization on machines which lack a X server. It relies on the
OpenSync framework to do the actual synchronization.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/msynctool
%{_bindir}/convcard
%{_bindir}/convtest
%{_mandir}/man1/convcard.1*
%{_mandir}/man1/msynctool.1*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.22-10mdv2011.0
+ Revision: 620413
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1:0.22-9mdv2010.0
+ Revision: 440163
- rebuild

* Thu Feb 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.22-8mdv2009.1
+ Revision: 337861
- keep bash completion in its own package

* Sun Mar 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.22-7mdv2008.1
+ Revision: 189683
- bash completion

* Thu Mar 13 2008 Anne Nicolas <ennael@mandriva.org> 1:0.22-6mdv2008.1
+ Revision: 187419
- bump release

  + Adam Williamson <awilliamson@mandriva.org>
    - fix buildrequire
    - a few cleanups
    - better description
    - revert to 0.22 based on latest 0.22 spec from SVN

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long

* Mon Jan 28 2008 Funda Wang <fwang@mandriva.org> 0.36-1mdv2008.1
+ Revision: 158962
- update to new version 0.36

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 25 2007 Funda Wang <fwang@mandriva.org> 0.35-1mdv2008.1
+ Revision: 137660
- New version 0.35

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 04 2007 Funda Wang <fwang@mandriva.org> 0.34-1mdv2008.1
+ Revision: 105786
- rm build dir at first
- New version 0.34

* Fri Oct 19 2007 Funda Wang <fwang@mandriva.org> 0.33-1mdv2008.1
+ Revision: 100186
- fix file list
- New version 0.33

* Sat Sep 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-4mdv2008.0
+ Revision: 93834
- don't requires multisync, but obsoletes it
  drop useless patch

* Tue Sep 25 2007 Thierry Vignaud <tv@mandriva.org> 0.22-3mdv2008.0
+ Revision: 92899
- requires multisync (#34083)

* Fri Aug 10 2007 Helio Chissini de Castro <helio@mandriva.com> 0.22-2mdv2008.0
+ Revision: 61018
- Removed explicit libopensync requires, since msync already links against main libopensync library and all base tools was moved to main library

* Tue Apr 24 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2008.0
+ Revision: 17973
- fix build
- new version


* Wed Mar 07 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.20-2mdv2007.1
+ Revision: 134806
- Fix Group

* Fri Dec 01 2006 Olivier Thauvin <nanardon@mandriva.org> 0.20-1mdv2007.1
+ Revision: 89495
- initial mandriva package
- Create msynctool

