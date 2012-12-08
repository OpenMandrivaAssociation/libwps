%define api     0.2
%define major	2
%define libname		%mklibname wps %{api} %{major}
%define develname	%mklibname -d wps

Summary:	Library for reading and converting Microsoft Works word processor documents
Name:		libwps
Epoch:		1
Version:	0.2.7
Release:	1
Group:		Office
License: 	LGPLv2+
URL: 		http://libwps.sourceforge.net/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/libwps/%{name}-%{version}.tar.xz

BuildRequires: doxygen
BuildRequires: pkgconfig(libwpd-0.9)
BuildRequires: boost-devel

%description
Library that handles Microsoft Works documents.

%package tools
Requires: %{libname} = %{EVRD}
Summary: Tools to transform Works documents into other formats
Group: Publishing

%description tools
Tools to transform Works documents into other formats.
Currently supported: html, raw, text

%package -n %{libname}
Summary: Library for reading and converting Microsoft Works word processor documents
Group: System/Libraries
Obsoletes: %mklibname wps- 0.1 1

%description -n %{libname}
Library that handles Microsoft Works documents.

%package -n %{develname}
Summary: Files for developing with libwps
Group: Development/C++
Requires: %{libname} = %{EVRD}
Provides: libwps-devel = %{EVRD}

%description -n %{develname}
Includes and definitions for developing with libwps.

%package docs
Requires: %{develname} = %{EVRD}
Summary: Documentation of libwps API
Group: Development/C++

%description docs
Documentation of libwps API for developing with libwps

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files tools
%{_bindir}/wps2*

%files -n %{libname}
%{_libdir}/libwps-%{api}.so.%{major}*

%files -n %{develname}
%{_libdir}/libwps*-%{api}.so
%{_libdir}/pkgconfig/libwps*.pc
%{_includedir}/*

%files docs
%{_docdir}/libwps*



%changelog
* Sat May 07 2011 Funda Wang <fwang@mandriva.org> 1:0.2.2-1mdv2011.0
+ Revision: 672218
- new version 0.2.2

* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 1:0.2.0-1
+ Revision: 662209
- update file list
- new verison 0.2.0

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.2-6
+ Revision: 661555
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.2-5mdv2011.0
+ Revision: 602617
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.2-4mdv2010.1
+ Revision: 520952
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:0.1.2-3mdv2010.0
+ Revision: 425880
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.2-2mdv2009.0
+ Revision: 229833
- rebuild

* Sun Jan 06 2008 Funda Wang <fwang@mandriva.org> 1:0.1.2-1mdv2008.1
+ Revision: 145946
- fix doc dir
- New version 0.1.2

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 05 2007 Funda Wang <fwang@mandriva.org> 1:0.1.0-7mdv2008.1
+ Revision: 105960
- adopt to libname policy

* Mon Nov 05 2007 Funda Wang <fwang@mandriva.org> 1:0.1.0-6mdv2008.1
+ Revision: 105958
- fix requires of tools and devel

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Wed Aug 29 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1:0.1.0-5mdv2008.0
+ Revision: 74902
- Fix epoch handling.

* Wed Aug 29 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1:0.1.0-4mdv2008.0
+ Revision: 74859
- New upstream: 0.1.0 final.

* Fri Aug 03 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.1.0.svn20070129-4mdv2008.0
+ Revision: 58625
- Remove ~ from the version tag.

* Fri Jun 29 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.1.0~svn20070129-3mdv2008.0
+ Revision: 45871
- Add provides on -devel due to 64b stuff.

* Tue Jun 26 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.1.0~svn20070129-2mdv2008.0
+ Revision: 44663
- Fix requirest from -devel to lib.

* Tue Jun 26 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.1.0~svn20070129-1mdv2008.0
+ Revision: 44627
- Added missing buildrequires to doxygen.
- Adapted to Mandriva.
- Import libwps



* Sun Sep 24 2006 Andrew Ziem <andrewziem users sourceforge net>
- wpd to wps

* Fri Jan 28 2005 Fridrich Strba <fridrich.strba@bluewin.ch>
- Adapt to the new libwpd-X.Y and libwpd-stream-X.Y modules

* Wed Sep 29 2004 Fridrich Strba <fridrich.strba@bluewin.ch>
- Move files between libwpd and libwpd-devel packages
- Reflect the separation of libwpd-1 and libwpd-stream-1

* Sat May 22 2003 Rui M. Seabra <rms@1407.org>
- Reflect current state of build

* Sat Apr 26 2003 Rui M. Seabra <rms@1407.org>
- Create rpm spec
