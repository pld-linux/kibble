Summary:	Kibble - a knowledge base program
Summary(pl):	Kibble - podrêczna baza faktów
Name:		kibble
Version:	0.7.3
Release:	2
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Copyright:	GPL
URL:		http://wish.student.harvard.edu/kibble/
Source:		ftp://wish.student.harvard.edu/pub/kibble/packages/%{name}-%{version}.tar.bz2
Patch:		kibble-CFLAGS.patch
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is Kibble, a knowledge base program. It is used to organize seemingly
discursive thoughts into a cohesive engine. Basically, it is used it to keep
track of random ideas that may prove useful.

%description -l pl
Kibble jest programem do organizowania podrêcznej bazy faktów,
przechowywanych w hierarchicznym drzewku. Podstawowym zastosowaniem, z my¶l±
o którym by³ robiony ten program, jest przechowywanie informacji o pomys³ach.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/kibble <<EOF
xfig name "kibble"
xfig description "Kibble - a knowledge base program"
xfig group Applications
xfig exec "/usr/X11R6/bin/kibble &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/etc/X11/wmconfig/kibble
%attr(755,root,root) /usr/X11R6/bin/kibble
