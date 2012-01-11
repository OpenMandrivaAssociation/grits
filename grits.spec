%define libgrits	%mklibname grits 2
%define libgrits_devel	%mklibname -d grits

Name:		grits
Version:	0.6.3
Release:	1
Summary:	Virtual Globe library that handles coordinates and the OpenGL viewport
URL:		http://lug.rose-hulman.edu/code/projects/grits
Group:		System/Libraries
License:	GPLv3
Source0:	http://lug.rose-hulman.edu/proj/grits/%{name}-%{version}.tar.gz
Patch0:		grits-0.6-dynamic.patch
Patch1:		grits-0.6.2-link.patch
BuildRequires:	GL-devel
BuildRequires:	libglu-devel
BuildRequires:	cairo-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libsoup-devel
BuildRequires:	libxml2-devel

%description
libgis is a Virtual Globe library that handles coordinates and the OpenGL
viewport. Also provides some generic functionality and a plugin API. It is
used by AWeather.

#------------------------------------------------------------------------------

%package -n %{libgrits}

Summary:	Virtual Globe library that handles coordinates and the OpenGL viewport

%description -n %{libgrits}
libgrits is a Virtual Globe library that handles coordinates and the OpenGL
viewport. Also provides some generic functionality and a plugin API. It is
used by AWeather.

%files -n %{libgrits}
%{_libdir}/*.so.*
%{_libdir}/grits2/*.so
%doc ChangeLog README TODO

#------------------------------------------------------------------------------

%package -n %{libgrits_devel}

Group:		Development/C
Summary:	Development files for %libgrits Virtual Globe library
Requires:	%libgrits == %{version}-%{release}
Provides:	grits-devel == %{version}
Provides:	grits2-devel == %{version}

%description -n %{libgrits_devel}
libgrits is a Virtual Globe library that handles coordinates and the OpenGL
viewport. Also provides some generic functionality and a plugin API. It is
used by AWeather.

This package contains files needed only for development.

%files -n %{libgrits_devel}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/grits.pc
%doc ChangeLog README TODO

#------------------------------------------------------------------------------

%package doc
Requires:	%{libgrits_devel} == %{version}
Summary:	Documentation for %libgrits Virtual Globe library

%description doc
libgrits is a Virtual Globe library that handles coordinates and the OpenGL
viewport. Also provides some generic functionality and a plugin API. It is
used by AWeather.

This package contains API documentation.

%files doc
%doc %{_datadir}/gtk-doc/html/grits/

#------------------------------------------------------------------------------

%package demo
Summary:	Demo program for %{libgrits} Virtual Globe library
Group:		Sciences/Geosciences

%files demo
%{_bindir}/grits-demo
%{_mandir}/man1/grits-demo.1*
%doc ChangeLog README TODO

%description demo
libgrits is a Virtual Globe library that handles coordinates and the OpenGL
viewport. Also provides some generic functionality and a plugin API. It is
used by AWeather.

This package contains demo program using %{libgrits}

#------------------------------------------------------------------------------

%prep
%setup -q
#patch0 -p1
%patch1 -p1

%build
autoreconf
%configure2_5x	--enable-shared=yes \
		--enable-static=no
%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -delete
