Name:           msynctool
Version:        0.33
Release:        %mkrel 1
Summary:        CLI for synchronization with OpenSync
License:        GPL
Group:          Networking/Other
URL:            http://www.opensync.org
Source:         http://www.opensync.org/download/releases/%version/%{name}-%{version}.tar.bz2
Obsoletes:	    multisync-cli
Obsoletes:	    multisync
BuildRequires:  libopensync-devel >= %version
BuildRequires:	scons
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

%build
scons prefix=%{_prefix}

%install
scons install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/man1/*
