%define	upstream_name	 File-Copy-Recursive
%define upstream_version 0.38

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	11

Summary:	Perl module for recursively copying files and directories
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module copies and moves directories recursively (or single files, well...
singley) to an optional depth and attempts to preserve each file or directory's
mode.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.380.0-8mdv2012.0
+ Revision: 765237
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.380.0-7
+ Revision: 763747
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.380.0-6
+ Revision: 667137
- mass rebuild

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.380.0-5mdv2010.1
+ Revision: 543264
- rebuild
- rebuild
- rebuild
- rebuild

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.0
+ Revision: 407687
- rebuild using %%perl_convert_version

* Mon Dec 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2009.1
+ Revision: 311975
- update to new version 0.38

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-1mdv2009.1
+ Revision: 292138
- update to new version 0.37

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.36-2mdv2009.0
+ Revision: 265363
- rebuild early 2009.0 package (before pixel changes)

* Fri Apr 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2009.0
+ Revision: 195554
- update to new version 0.36

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.35-2mdv2008.1
+ Revision: 180396
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2008.0
+ Revision: 75220
- update to new version 0.35

* Wed May 16 2007 Olivier Thauvin <nanardon@mandriva.org> 0.33-1mdv2008.0
+ Revision: 27149
- 0.33


* Sat Mar 10 2007 Olivier Thauvin <nanardon@mandriva.org> 0.31-1mdv2007.1
+ Revision: 141048
- 0.31

* Tue Dec 12 2006 Olivier Thauvin <nanardon@mandriva.org> 0.30-1mdv2007.1
+ Revision: 95137
- 0.30
- 0.25
- Import perl-File-Copy-Recursive

* Sat Jun 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2007.0
- New version 0.24

* Fri Jun 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2007.0
- New release 0.23
- HTTP source URL

* Thu Jun 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdk
- New release 0.22

* Fri May 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.21-1mdk
- New release 0.21

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdk
- new version
- fix directory ownership
- rpmbuildupdate aware

* Thu Mar 02 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.19-1mdk
- 0.19

* Thu Feb 02 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.18-1mdk
- 0.18

* Fri Dec 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.16-1mdk
- Initial MDV package

