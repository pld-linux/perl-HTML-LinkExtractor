#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	LinkExtractor
Summary:	HTML::LinkExtractor - extract links from an HTML document
Summary(pl):	HTML::LinkExtractor - wyodrêbnianie odno¶ników z dokumentów HTML
Name:		perl-HTML-LinkExtractor
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe32961a48dc313080be0f1bbf039b6d
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-TokeParser-Simple >= 2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::LinkExtractor Perl module is used for extracting links from
HTML.  It is very similar to HTML::LinkExtor, except that besides
getting the URL, you also get the link-text.

%description -l pl
Modu³ Perla HTML::LinkExtractor s³u¿y do wyodrêbniania ³±cz z kodu
HTML. Jest on bardzo podobny do modu³u HTML::LinkExtor z tym
wyj±tkiem, ¿e otrzymuje siê URL razem z tekstem stanowi±cym tre¶æ
³±cza.

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
