Summary:	Kibble - a knowledge base program
Summary(pl):	Kibble - podr�czna baza fakt�w
Name:		kibble
Version:	0.7.3
Release:	2
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Copyright:	GPL
URL:		http://wish.student.harvard.edu/kibble/
Source0:	ftp://wish.student.harvard.edu/pub/kibble/packages/%{name}-%{version}.tar.bz2
Source1:	kibble.desktop
Patch:		kibble-CFLAGS.patch
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is Kibble, a knowledge base program. It is used to organize seemingly
discursive thoughts into a cohesive engine. Basically, it is used it to keep
track of random ideas that may prove useful.

%description -l pl
Kibble jest programem do organizowania podr�cznej bazy fakt�w,
przechowywanych w hierarchicznym drzewku. Podstawowym zastosowaniem, z my�l�
o kt�rym by� robiony ten program, jest przechowywanie informacji o pomys�ach.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kibble
%{_datadir}/applnk/Utilities/kibble.desktop
