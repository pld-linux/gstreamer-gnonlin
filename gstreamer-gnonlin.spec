%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.29
%define		gstpb_req_ver	0.10.29
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	GStreamer extension library for non-linear editing
Summary(pl.UTF-8):	Biblioteka rozszerzenia GStreamera do edycji nieliniowej
Name:		gstreamer-gnonlin
Version:	0.10.16
Release:	1
License:	LGPL v2+
Group:		Applications/Multimedia
Source0:	http://gstreamer.freedesktop.org/src/gnonlin/gnonlin-%{version}.tar.bz2
# Source0-md5:	824619ce357c0a61e333c3cc745a63bd
URL:		http://gnonlin.sourceforge.net/
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_req_ver}
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
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

%description apidocs
Gnonlin API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Gnonlin.

%prep
%setup -q -n gnonlin-%{version}

%build
%configure \
	--disable-static \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_major_ver}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgnl.so

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnonlin-0.10
%endif
