#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	PSGI
%include	/usr/lib/rpm/macros.perl
Summary:	PSGI - Perl Web Server Gateway Interface Specification
#Summary(pl.UTF-8):	
Name:		perl-PSGI
Version:	1.09_1
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MI/MIYAGAWA/PSGI-1.09_1.tar.gz
# Source0-md5:	e043571789d55ce06f0066c33b4579c3
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/PSGI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}//*.pm
%{perl_vendorlib}/PSGI/
%{_mandir}/man3/*
