%define	modname	File-Copy-Recursive
%define modver	0.38

Summary:	Perl module for recursively copying files and directories
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	11
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/File/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This module copies and moves directories recursively (or single files, well...
singley) to an optional depth and attempts to preserve each file or directory's
mode.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*

