%define api	0.2
%define major	2
%define libname	%mklibname wps %{api} %{major}
%define devname	%mklibname -d wps

Summary:	Library for reading and converting Microsoft Works word processor documents
Name:		libwps
Epoch:		1
Version:	0.2.9
Release:	6
Group:		Office
License:	LGPLv2+
Url:		http://libwps.sourceforge.net/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/libwps/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libwpd-0.9)

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
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files tools
%{_bindir}/wps2*

%files -n %{libname}
%{_libdir}/libwps-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/libwps-%{api}.so
%{_libdir}/pkgconfig/libwps*.pc
%{_includedir}/*
%doc %{_docdir}/libwps*

