%define rel             1
%define name            libwps
%define ups_version     0.1.2
%define version         0.1.2
%define release         %mkrel %{rel}
%define api_version     0.1
%define lib_major       1
%define lib_name        %mklibname wps %{api_version} %{lib_major}
%define lib_name_devel  %mklibname -d wps

Name: %{name}
Summary: Library for reading and converting Microsoft Works word processor documents
Epoch: 1
Version: %{version}
Release: %{release}
Source: http://nchc.dl.sourceforge.net/sourceforge/libwps/%{name}-%{version}.tar.gz
Group: Office
URL: http://libwps.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: LGPLv2+
BuildRequires: doxygen
BuildRequires: libwpd-devel >= 0.8.8
BuildRequires: glibc-devel

%description
Library that handles Microsoft Works documents.

%package tools
Requires: %{lib_name} = %{epoch}:%{version}-%{release}
Summary: Tools to transform Works documents into other formats
Group: Publishing

%description tools
Tools to transform Works documents into other formats.
Currently supported: html, raw, text

%package -n %{lib_name}
Summary: Library for reading and converting Microsoft Works word processor documents
Group: System/Libraries
Obsoletes: %mklibname wps- 0.1 1

%description -n %{lib_name}
Library that handles Microsoft Works documents.

%package -n %{lib_name_devel}
Summary: Files for developing with libwps
Group: Development/C++
Requires: %{lib_name} = %{epoch}:%{version}-%{release}
Provides: libwps-devel = %{epoch}:%{version}-%{release}

%description -n %{lib_name_devel}
Includes and definitions for developing with libwps.

%package docs
Requires: %{lib_name_devel} = %{epoch}:%{version}-%{release}
Summary: Documentation of libwps API
Group: Development/C++

%description docs
Documentation of libwps API for developing with libwps

%prep
%setup -q -n %{name}-%{ups_version}

%build
%configure2_5x
%make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files tools
%defattr(755,root,root,755)
%{_bindir}/wps2*

%files -n %{lib_name}
%defattr(644,root,root,755)
%{_libdir}/libwps*-0.1.so.*

%files -n %{lib_name_devel}
%defattr(644,root,root,755)
%{_libdir}/libwps*-0.1.so
%{_libdir}/libwps*-0.1.*a
%{_libdir}/pkgconfig/libwps*-0.1.pc
%{_includedir}/libwps-0.1/libwps

%files docs
%{_docdir}/libwps-0.1.0/*
