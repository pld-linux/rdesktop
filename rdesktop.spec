Summary:	RDP client for accessing Windows NT Terminal Server
Summary(pl):	Klient RDP umo¿liwiaj±cy dostêp do Terminal Serwera WinNT
Name:		rdesktop
Version:	1.0.0
Release:	0.pl19
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://prdownloads.sourceforge.net/rdesktop/%{name}-%{version}.tar.gz
Patch0:		http://bibl4.oru.se/projects/rdesktop/%{name}-unified-patch19-6.bz2
Patch1:		%{name}-opt.patch
URL:		http://www.rdesktop.org/
BuildRequires:	gmp-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
rdesktop is an open source client for Windows NT Terminal Server,
capable of natively speaking its Remote Desktop Protocol (RDP) in
order to present the user's NT desktop. Unlike Citrix ICA, no server
extensions are required. Support for Windows 2000 Terminal Services is
planned, although not implemented at this time.

%description -l pl
rdesktop jest klientem natywnie u¿ywaj±cym protoko³u RDP (Remote
Desktop Protocol) umo¿liwiaj±cego dostêp do Terminal Servera Windows
NT. W przeciwieñstwie do rozwi±zañ typu Citrix nie s± wymagane ¿adne
rozszerzenia po stronie serwera. Wsparcie dla Windows 2000 Terminal
Services jest planowane.

%prep
%setup -q
%patch0 -p2
%patch1 -p1

%build
%{__make} \
	CFLAGSOPT="%{rpmcflags}" \
	LDFLAGSOPT="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install	%{name}		$RPM_BUILD_ROOT%{_bindir}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf CHANGES readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
