%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.9
%define		gstpb_req_ver	0.10.4
Summary:	GStreamer extension library for non-linear editing
Summary(pl.UTF-8):	Biblioteka rozszerzenia GStreamera do edycji nieliniowej
Name:		gstreamer-gnonlin
Version:	0.10.7
Release:	1
License:	LGPL
Group:		Applications/Multimedia
Source0:	http://gstreamer.freedesktop.org/src/gnonlin/gnonlin-%{version}.tar.bz2
# Source0-md5:	81f683b7fca9a035635977d1235a1bf5
URL:		http://gnonlin.sourceforge.net/
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_req_ver}
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

%prep
%setup -q -n gnonlin-%{version}

%build
%configure \
	--disable-static

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
