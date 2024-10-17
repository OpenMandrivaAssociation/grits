%define major 4
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Virtual Globe library that handles coordinates and the OpenGL viewport
Name:		grits
Version:	0.7
Release:	3
License:	GPLv3+
Group:		System/Libraries
Url:		https://lug.rose-hulman.edu/code/projects/grits
Source0:	http://lug.rose-hulman.edu/proj/grits/%{name}-%{version}.tar.gz
Patch1:		grits-0.6.2-link.patch
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)

%description
libgis is a Virtual Globe library that handles coordinates and the OpenGL
viewport. Also provides some generic functionality and a plugin API. It is
used by AWeather.

#------------------------------------------------------------------------------

%package -n %{libname}
Summary:	Virtual Globe library that handles coordinates and the OpenGL viewport
Group:		System/Libraries

%description -n %{libname}
libname is a Virtual Globe library that handles coordinates and the OpenGL
viewport. Also provides some generic functionality and a plugin API. It is
used by AWeather.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*
%{_libdir}/grits%{major}/*.so

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for the Virtual Globe library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
libname is a Virtual Globe library that handles coordinates and the OpenGL
viewport. Also provides some generic functionality and a plugin API. It is
used by AWeather.

This package contains files needed only for development.

%files -n %{devname}
%doc ChangeLog README TODO
%{_libdir}/lib%{name}.so
%{_includedir}/*
%{_libdir}/pkgconfig/grits.pc

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for the Virtual Globe library
Group:		Books/Computer books

%description doc
libname is a Virtual Globe library that handles coordinates and the OpenGL
viewport. Also provides some generic functionality and a plugin API. It is
used by AWeather.

This package contains API documentation.

%files doc
%doc %{_datadir}/gtk-doc/html/grits/

#----------------------------------------------------------------------------

%package demo
Summary:	Demo program for the Virtual Globe library
Group:		Sciences/Geosciences

%description demo
libname is a Virtual Globe library that handles coordinates and the OpenGL
viewport. Also provides some generic functionality and a plugin API. It is
used by AWeather.

This package contains demo program using %{libname}

%files demo
%doc ChangeLog README TODO
%{_bindir}/grits-demo
%{_mandir}/man1/grits-demo.1*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch1 -p1

%build
autoreconf
%configure2_5x \
	--enable-shared=yes \
	--enable-static=no
%make

%install
%makeinstall_std

install -d -m 755 %{buildroot}%{_docdir}/%{devname}

