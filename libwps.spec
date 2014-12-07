%define api	0.3
%define major	3
%define libname	%mklibname wps %{api} %{major}
%define devname	%mklibname -d wps

Summary:	Library for reading and converting Microsoft Works word processor documents
Name:		libwps
Epoch:		1
Version:	0.3.0
Release:	2
Group:		Office
License:	LGPLv2+
Url:		http://libwps.sourceforge.net/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/libwps/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(librevenge-0.0)

%description
Library that handles Microsoft Works documents.

%package tools
Requires:	%{libname} = %{EVRD}
Summary:	Tools to transform Works documents into other formats
Group:		Publishing

%description tools
Tools to transform Works documents into other formats.
Currently supported: html, raw, text

%package -n %{libname}
Summary:	Library for reading and converting Microsoft Works word processor documents
Group:		System/Libraries

%description -n %{libname}
Library that handles Microsoft Works documents.

%package -n %{devname}
Summary:	Files for developing with libwps
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	libwps-devel = %{EVRD}

%description -n %{devname}
Includes and definitions for developing with libwps.

%prep
%setup -q

%build
CFLAGS="%{optflags} -Qunused-arguments" \
CXXFLAGS="%{optflags} -Qunused-arguments" \
%configure
%make

%install
%makeinstall_std

%files tools
%{_bindir}/wps2*
%{_bindir}/wks2*

%files -n %{libname}
%{_libdir}/libwps-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/libwps-%{api}.so
%{_libdir}/pkgconfig/libwps*.pc
%{_includedir}/*
%doc %{_docdir}/libwps*

