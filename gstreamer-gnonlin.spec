#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc

%define		gst_req_ver	1.4.0
%define		gstpb_req_ver	1.4.0
Summary:	GStreamer extension library for non-linear editing
Summary(pl.UTF-8):	Biblioteka rozszerzenia GStreamera do edycji nieliniowej
Name:		gstreamer-gnonlin
Version:	1.4.0
Release:	3
License:	LGPL v2+
Group:		Applications/Multimedia
Source0:	http://gstreamer.freedesktop.org/src/gnonlin/gnonlin-%{version}.tar.xz
# Source0-md5:	106899d1ee36e18f92bb838244d585eb
URL:		http://gnonlin.sourceforge.net/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.34
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_req_ver}
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.1
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.34
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnonlin is a plugin for GStreamer which provides support for writing
non-linear audio and video editing applications. It introduces the
concept of a timeline.

%description -l pl.UTF-8
Gnonlin to wtyczka dla GStreamera pozwalająca na pisanie aplikacji do
nieliniowej edycji dźwięku i obrazu. Wprowadza pojęcia "linii czasu".

%package apidocs
Summary:	Gnonlin API documentation
Summary(pl.UTF-8):	Dokumentacja API Gnonlin
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
Gnonlin API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Gnonlin.

%prep
%setup -q -n gnonlin-%{version}

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--enable-gtk-doc%{!?with_apidocs:=no} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgnl.so

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnonlin-1.0
%endif
