Summary:	RDP client for accessing Windows NT Terminal Server
Summary(pl):	Klient RDP umo¿liwiaj±cy dostêp do Terminal Serwera WinNT
Name:		rdesktop
Version:	1.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/rdesktop/%{name}-%{version}.tar.gz
Patch0:		http://bibl4.oru.se/projects/rdesktop/%{name}-unified-patch19-8-5.bz2
Patch1:		%{name}-opt+DESTDIR.patch
Patch2:		%{name}-srvr-fix.patch
URL:		http://www.rdesktop.org/
BuildRequires:	XFree86-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
rdesktop is an open source client for Windows NT or Windows 2000 Terminal
Server, capable of natively speaking its Remote Desktop Protocol (RDP) in
order to present the user's NT desktop. Unlike Citrix ICA, no server
extensions are required. 

%description -l pl
rdesktop jest klientem natywnie u¿ywaj±cym protoko³u RDP (Remote Desktop
Protocol) umo¿liwiaj±cego dostêp do Terminal Servera Windows NT lub
Windows 2000. W przeciwieñstwie do rozwi±zañ typu Citrix nie s± wymagane
¿adne rozszerzenia po stronie serwera.

%package srvr
Summary:	RDP server (for testing purposes)
Summary(pl):	Serwer RDP (do testów)
Group:		X11/Applications/Networking

%description srvr
RDP server for rdesktop testing. It currently connects as viewer to
VNC server.

%description srvr -l pl
Serwer RDP do testowania rdesktop. Na razie umo¿liwia ³±czenie siê jako
klient z serwerem VNC.

%prep
%setup -q
%patch0 -p2
%patch1 -p1
%patch2 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--with-openssl \
	--with-ssl-includes=/usr/include/openssl \
	--with-ssl-libs=/usr/lib

%{__make} \
	CC="%{__cc}" \
	CFLAGSOPT="%{rpmcflags}" \
	LDFLAGSOPT="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES readme.txt
%attr(755,root,root) %{_bindir}/rdesktop
%{_mandir}/man?/*

%files srvr
%defattr(644,root,root,755)
%doc rdp-srvr-readme.txt
%attr(755,root,root) %{_bindir}/rdp-srvr
