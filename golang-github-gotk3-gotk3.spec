# Run tests in check section
%bcond_with check

# https://github.com/gotk3/gotk3
%global goipath		github.com/gotk3/gotk3
%global forgeurl	https://github.com/gotk3/gotk3
Version:		0.6.4.1

%gometa

Summary:	Go bindings for GTK3
Name:		golang-github-gotk3-gotk3

Release:	1
Source0:	https://github.com/gotk3/gotk3/archive/v%{version}/gotk3-%{version}.tar.gz
URL:		https://github.com/gotk3/gotk3
License:	ISC
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	x11-server-xvfb
BuildRequires:	xauth
BuildArch:	noarch

%description
The gotk3 project provides Go bindings for GTK 3 and dependent
projects.  Partial binding support for the following libraries
is currently implemented:

- GTK 3 (3.12 and later)
- GDK 3 (3.12 and later)
- GLib 2 (2.36 and later)
- Cairo (1.10 and later)

Care has been taken for memory management to work seamlessly with
Go's garbage collector without the need to use or understand
GObject's floating references.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	xauth
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n gotk3-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

