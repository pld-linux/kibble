Summary:	Kibble - a knowledge base program
Summary(pl):	Kibble - podrêczna baza faktów
Name:		kibble
Version:	0.7.3
Release:	1
Group:		X11/Applications
Group(p):	X11/Applikacje
Copyright:	GPL
Source0:	ftp://wish.student.harvard.edu/pub/kibble/packages/%{name}-%{version}.tar.bz2
Patch:		kibble-CFLAGS.patch
URL:		http://wish.student.harvard.edu/kibble/
Requires:	gtk+ = 1.2.1
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is Kibble, a knowledge base program. It is used to organize seemingly
discursive thoughts into a cohesive engine. Basically, it is used it to keep
track of random ideas that may prove useful.

%description -l pl
Kibble jest programem do organizowania podrêcznej bazy faktów,
przechowywanych w hierarhicznym drezewku. Podstawowym zastosowaniem z mysl±
o którym by³ robiony ten program jest przechowywanie informacji o pomys³ach.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
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

%changelog
* Thu Mar 25 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.7.3-1]
- added kibble-CFLAGS.patch (fix passing CFLAGS for autoconf).

* Thu Mar 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.7.2-1]
- added pl tranlations.

* Sat Dec 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.7.1-1]
- first release in rpm package.
