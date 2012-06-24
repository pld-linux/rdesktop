%bcond_with	vnc
#
Summary:	RDP client for accessing Windows NT Terminal Server
Summary(pl):	Klient RDP umo�liwiaj�cy dost�p do Terminal Serwera WinNT
Name:		rdesktop
Version:	1.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/rdesktop/%{name}-%{version}.tar.gz
# Source0-md5:	433546f60fc0f201e99307ba188369ed
Patch0:		%{name}-vnc.patch
URL:		http://www.rdesktop.org/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	libao-devel
%{?with_vnc:BuildRequires:	libvncserver-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdesktop is an open source client for Windows NT or Windows 2000
Terminal Server, capable of natively speaking its Remote Desktop
Protocol (RDP) in order to present the user's NT desktop. Unlike
Citrix ICA, no server extensions are required.

%description -l pl
rdesktop jest klientem natywnie u�ywaj�cym protoko�u RDP (Remote
Desktop Protocol) umo�liwiaj�cego dost�p do Terminal Servera Windows
NT lub Windows 2000. W przeciwie�stwie do rozwi�za� typu Citrix nie s�
wymagane �adne rozszerzenia po stronie serwera.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	%{?with_vnc:--with-libvncserver} \
	--with-libao \
	--with-sound=libao \
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
%attr(755,root,root) %{_datadir}/rdesktop
%{_mandir}/man?/*
