Name:           msynctool
Version:        0.22
Release:        %mkrel 3
Summary:        CLI for synchronization with OpenSync
License:        GPL
Group:          Networking/Other
URL:            http://www.opensync.org
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-0.22-cflags.patch
Obsoletes:	    multisync-cli
BuildRequires:  libopensync-devel
Requires:		multisync
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Command line version of MultiSync for the OpenSync-package. To allow
synchronization on machines which lack a X server. It relies on the OpenSync
framework to do the actual synchronization. You need to install the libopensync
package and the plugins for it, too. This package is independent from the various
multisync-* packages which will be obsoleted once OpenSync has left the beta
phase.

%prep
%setup -q
%patch -p 0

%build
autoreconf -if
%configure2_5x
%make

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README
%{_bindir}/msynctool
%{_bindir}/convcard
%{_bindir}/convtest
%{_mandir}/man1/convcard.1*
%{_mandir}/man1/msynctool.1*


