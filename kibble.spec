Summary:	Kibble - a knowledge base program
Summary(pl.UTF-8):	Kibble - podręczna baza faktów
Name:		kibble
Version:	0.7.3
Release:	2
Group:		X11/Applications
License:	GPL v2
Source0:	ftp://wish.student.harvard.edu/pub/kibble/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	eb479613e7124c46d7905a309cc98845
Source1:	%{name}.desktop
Patch0:		%{name}-CFLAGS.patch
URL:		http://wish.student.harvard.edu/kibble/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is Kibble, a knowledge base program. It is used to organize
seemingly discursive thoughts into a cohesive engine. Basically, it is
used it to keep track of random ideas that may prove useful.

%description -l pl.UTF-8
Kibble jest programem do organizowania podręcznej bazy faktów,
przechowywanych w hierarchicznym drzewku. Podstawowym zastosowaniem, z
myślą o którym był robiony ten program, jest przechowywanie informacji
o pomysłach.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
./configure %{_target_platform} \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/kibble
%{_desktopdir}/kibble.desktop
