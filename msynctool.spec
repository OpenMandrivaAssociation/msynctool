Name:           msynctool
BuildRequires:  libopensync-devel
URL:            http://www.opensync.org
Version:        0.22
Release:        %mkrel 1
Summary:        CLI for synchronization with OpenSync
License:        GPL
Group:          Networking/Other
Source:         msynctool-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libopensync >= 0.20
Obsoletes:	multisync-cli

%description
Command line version of MultiSync for the OpenSync-package. To allow
synchronization on machines which lack a X server. It relies on the OpenSync
framework to do the actual synchronization. You need to install the libopensync
package and the plugins for it, too. This package is independent from the various
multisync-* packages which will be obsoleted once OpenSync has left the beta
phase.

%prep
%setup -q

%build
autoreconf -if
%configure
%make

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/msynctool
%{_bindir}/convcard
%{_mandir}/man1/convcard.1*
%{_mandir}/man1/msynctool.1*
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README


