Summary:	RDP client for accessing Windows NT Terminal Server
Summary(pl):	Klient RDP umo¿liwiaj±cy dostêp do Terminal Serwera WinNT
Name:		rdesktop
Version:	1.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/rdesktop/%{name}-%{version}.tar.gz
# Source0-md5:	542cb9d9b4dd1ecaf3ed4ff753fea7b8
URL:		http://www.rdesktop.org/
BuildRequires:	XFree86-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdesktop is an open source client for Windows NT or Windows 2000
Terminal Server, capable of natively speaking its Remote Desktop
Protocol (RDP) in order to present the user's NT desktop. Unlike
Citrix ICA, no server extensions are required.

%description -l pl
rdesktop jest klientem natywnie u¿ywaj±cym protoko³u RDP (Remote
Desktop Protocol) umo¿liwiaj±cego dostêp do Terminal Servera Windows
NT lub Windows 2000. W przeciwieñstwie do rozwi±zañ typu Citrix nie s±
wymagane ¿adne rozszerzenia po stronie serwera.

%prep
%setup -q

%build
./configure \
	--mandir=%{_mandir} \
	--prefix=%{_prefix}

cat >>Makeconf <<EOF
CFLAGS+=%{rpmcflags}
LDFLAGS+=%{rpmldflags} -L/usr/X11R6/%{_lib}
EOF

%{__make} \
	CC="%{__cc}"

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
