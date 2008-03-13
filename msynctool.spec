Name:		msynctool
Version:	0.22
Epoch:		1
Release:	%{mkrel 5}
Summary:	CLI for synchronization with OpenSync
License:	GPLv2+
Group:		Networking/Other
URL:		http://www.opensync.org
Source:		%{name}-%{version}.tar.bz2
Obsoletes:	multisync-cli
Obsoletes:	multisync
BuildRequires:	libopensync-devel = %{epoch}:%{version}
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
