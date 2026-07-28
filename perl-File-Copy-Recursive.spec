%define	modname	File-Copy-Recursive
%define modver	0.45

Summary:	Perl module for recursively copying files and directories
Name:		perl-%{modname}
Version:	%{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/drmuey/p5-File-Copy-Recursive
Source0:	https://cpan.metacpan.org/authors/id/D/DM/DMUEY/File-Copy-Recursive-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Warnings)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Path::Tiny)

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
make test || :

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*

