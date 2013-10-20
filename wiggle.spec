Summary:	Wiggle - apply conflicting patches
Summary(pl.UTF-8):	Wiggle - nakładanie konfliktujących patchy
Name:		wiggle
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://neil.brown.name/wiggle/%{name}-%{version}.tar.gz
# Source0-md5:	777d8d4c718220063511e82e16275d1b
URL:		http://neil.brown.name/wiggle/
BuildRequires:	groff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wiggle is a program for applying patches that patch cannot apply
because of conflicting changes.

%description -l pl.UTF-8
Wiggle jest programem do aplikowania patchy, których nałożenia odmówi
patch z powodu konfliktów.

%prep
%setup -q

%build
%{__make} wiggle wiggle.man \
	CC="%{__cc}" CFLAGS="-I. %{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/wiggle.1*
