Summary:	RDP client for accessing Windows NT Terminal Server
Summary(pl.UTF-8):	Klient RDP umożliwiający dostęp do Terminal Serwera WinNT
Name:		rdesktop
Version:	1.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/rdesktop/%{name}-%{version}.tar.gz
# Source0-md5:	c4b39115951c4a6d74f511c99b18fcf9
Patch0:		%{name}-xinerama.patch
URL:		http://www.rdesktop.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pcsc-lite-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
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

%build
%{__aclocal}
%{__autoconf}
%configure \
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
