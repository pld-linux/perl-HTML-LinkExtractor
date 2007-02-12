#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	LinkExtractor
Summary:	HTML::LinkExtractor - extract links from an HTML document
Summary(pl.UTF-8):   HTML::LinkExtractor - wyodrębnianie odnośników z dokumentów HTML
Name:		perl-HTML-LinkExtractor
Version:	0.13
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a30143b35ef76576fb984696746776de
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-TokeParser-Simple >= 2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::LinkExtractor Perl module is used for extracting links from
HTML. It is very similar to HTML::LinkExtor, except that besides
getting the URL, you also get the link-text.

%description -l pl.UTF-8
Moduł Perla HTML::LinkExtractor służy do wyodrębniania odnośników z
kodu HTML. Jest on bardzo podobny do modułu HTML::LinkExtor z tym
wyjątkiem, że otrzymuje się URL razem z tekstem stanowiącym treść
odnośników.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
