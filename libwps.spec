%define name libwps
%define version 0.1.0~svn20070129
%define  RELEASE 1
%define  release     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Name: %{name}
Summary: Library for reading and converting Microsoft Works word processor documents
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.gz
Group: System Environment/Libraries
URL: http://libwps.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: LGPL
BuildRequires: libwpd-devel >= 0.8, glibc-devel

%description
Library that handles Microsoft Works documents.

%if %{!?_without_stream:1}%{?_without_stream:0}
%package tools
Requires: %{name} = %{version}-%{release}
Summary: Tools to transform Works documents into other formats
Group: Applications/Publishing

%description tools
Tools to transform Works documents into other formats.
Currently supported: html, raw, text
%endif

%package devel
Requires: %{name} = %{version}-%{release}
Summary: Files for developing with libwps.
Group: Development/Libraries

%description devel
Includes and definitions for developing with libwps.

%if %{!?_without_docs:1}%{?_without_docs:0}
%package docs
Requires: %{name}
Summary: Documentation of libwps API
Group: Development/Documentation

%description docs
Documentation of libwps API for developing with libwps
%endif

%prep
%__rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} --exec-prefix=%{_prefix} \
	%{?_without_stream:--without-stream} \
	%{?_with_debug:--enable-debug}  \
	%{?_without_docs:--without-docs}

%__make

%install
umask 022

%__make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name}

%files
%defattr(644,root,root,755)
%{_libdir}/libwps*-0.1.so.*

%if %{!?_without_stream:1}%{?_without_stream:0}
%files tools
%defattr(755,root,root,755)
%{_bindir}/wps2*
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/libwps*-0.1.so
%{_libdir}/libwps*-0.1.*a
%{_libdir}/pkgconfig/libwps*-0.1.pc
%{_includedir}/libwps-0.1/libwps

%if %{!?_without_docs:1}%{?_without_docs:0}
%files docs
%{_datadir}/doc/libwps-0.1.0~svn20070129/*
%endif
