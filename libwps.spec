%define rel             1
%define name            libwps
%define ups_version     0.2.0
%define version         0.2.0
%define release         %mkrel %{rel}
%define api_version     0.2
%define lib_major       2
%define lib_name        %mklibname wps %{api_version} %{lib_major}
%define lib_name_devel  %mklibname -d wps

Name: %{name}
Summary: Library for reading and converting Microsoft Works word processor documents
Epoch: 1
Version: %{version}
Release: %{release}
Source: http://nchc.dl.sourceforge.net/sourceforge/libwps/%{name}-%{version}.tar.bz2
Group: Office
URL: http://libwps.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: LGPLv2+
BuildRequires: doxygen
BuildRequires: libwpd-devel >= 0.9.0

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
sed -i -e 's: -Wall -Werror -pedantic::' configure.in

%build
./autogen.sh
%configure2_5x --disable-static
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -rf %{buildroot}

%files tools
%defattr(755,root,root,755)
%{_bindir}/wps2*

%files -n %{lib_name}
%defattr(644,root,root,755)
%{_libdir}/libwps*-%{api_version}.so.%{lib_major}*

%files -n %{lib_name_devel}
%defattr(644,root,root,755)
%{_libdir}/libwps*-%{api_version}.so
%{_libdir}/libwps*-%{api_version}.la
%{_libdir}/pkgconfig/libwps*.pc
%{_includedir}/*

%files docs
%defattr(644,root,root,755)
%{_docdir}/libwps*
