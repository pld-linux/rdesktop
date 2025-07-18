Summary:	RDP client for accessing Windows NT Terminal Server
Summary(pl.UTF-8):	Klient RDP umożliwiający dostęp do Terminal Serwera WinNT
Name:		rdesktop
Version:	1.8.4
Release:	2
License:	GPL v3+
Group:		X11/Applications/Networking
Source0:	https://github.com/rdesktop/rdesktop/releases/download/v1.8.4/rdesktop-1.8.4.tar.gz
# Source0-md5:	7273f9dad833f6899a3e5b39d7fdd6f2
Patch0:		%{name}-xinerama.patch
Patch1:		%{name}-heimdal.patch
Patch2:		no-strip.patch
URL:		http://www.rdesktop.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	heimdal-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcsc-lite-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdesktop is an open source client for Windows NT or Windows 2000
Terminal Server, capable of natively speaking its Remote Desktop
Protocol (RDP) in order to present the user's NT desktop. Unlike
Citrix ICA, no server extensions are required.

%description -l pl.UTF-8
rdesktop jest klientem natywnie używającym protokołu RDP (Remote
Desktop Protocol) umożliwiającego dostęp do Terminal Servera Windows
NT lub Windows 2000. W przeciwieństwie do rozwiązań typu Citrix nie są
wymagane żadne rozszerzenia po stronie serwera.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-credssp \
	--enable-smartcard \
	--with-ipv6 \
	--with-sound=alsa
# note: --with-libvncserver requires vnc/ code, which don't exist

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/
%attr(755,root,root) %{_bindir}/rdesktop
%{_datadir}/rdesktop
%{_mandir}/man1/rdesktop.1*
