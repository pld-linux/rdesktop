#
# Conditional build:
%bcond_with	alsa	# ALSA for sound (instead of pulseaudio)
%bcond_with	libao	# libao for sound (instead of pulseaudio)

%if %{without alsa} && %{without libao}
%define	with_pulse	1
%endif
Summary:	RDP client for accessing Windows NT Terminal Server
Summary(pl.UTF-8):	Klient RDP umożliwiający dostęp do Terminal Serwera WinNT
Name:		rdesktop
Version:	1.9.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Networking
Source0:	https://github.com/rdesktop/rdesktop/releases/download/v%{version}/rdesktop-%{version}.tar.gz
# Source0-md5:	c67767f5a329f902291a56d22ae4303a
Patch0:		%{name}-xinerama.patch
Patch1:		no-strip.patch
Patch2:		%{name}-ssl-exp-mod.patch
Patch3:		%{name}-credssp-linux.patch
Patch4:		%{name}-nettle4.patch
URL:		https://github.com/rdesktop/rdesktop
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gmp-devel
BuildRequires:	gnutls-devel >= 3.2.0
BuildRequires:	heimdal-devel
%{?with_libao:BuildRequires:	libao-devel}
BuildRequires:	libsamplerate-devel
BuildRequires:	libtasn1-devel
BuildRequires:	nettle-devel
BuildRequires:	pcsc-lite-devel >= 1.6.0
BuildRequires:	pkgconfig
%{?with_pulse:BuildRequires:	pulseaudio-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
Requires:	gnutls-libs%{?_isa} >= 3.2.0
Requires:	pcsc-lite-libs%{?_isa} >= 1.6.0
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
%patch -P3 -p1
%patch -P4 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-credssp \
	--enable-smartcard \
	--with-ipv6 \
	--with-sound=%{?with_alsa:alsa}%{?with_libao:libao}%{?with_pulse:pulse}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md doc/{AUTHORS,ChangeLog,TODO,*.txt}
%attr(755,root,root) %{_bindir}/rdesktop
%{_datadir}/rdesktop
%{_mandir}/man1/rdesktop.1*
