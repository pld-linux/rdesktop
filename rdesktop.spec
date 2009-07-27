#
# Conditional build:
%bcond_with	vnc	# build rdp2vnc
#
Summary:	RDP client for accessing Windows NT Terminal Server
Summary(pl.UTF-8):	Klient RDP umożliwiający dostęp do Terminal Serwera WinNT
Name:		rdesktop
Version:	1.6.0
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/rdesktop/%{name}-%{version}.tar.gz
# Source0-md5:	c6fcbed7f0ad7e60ac5fcb2d324d8b16
Patch0:		%{name}-vnc.patch
Patch1:		%{name}-xinerama.patch
URL:		http://www.rdesktop.org/
BuildRequires:	alsa-lib-devel
%{?with_vnc:BuildRequires:	libvncserver-devel}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcsc-lite-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xineramaproto-devel
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
%patch0 -p1
%patch1 -p0

%build
%{__aclocal}
%{__autoconf}
%configure \
	%{?with_vnc:--with-libvncserver} \
	--enable-smartcard \
	--with-sound=alsa \
	--with-ipv6

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/
%attr(755,root,root) %{_bindir}/rdesktop
%{_datadir}/rdesktop
%{_mandir}/man1/rdesktop.1*
