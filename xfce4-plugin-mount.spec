%define		rname	xfce4-mount-plugin

Summary:	mount/umount utility for Xfce panel
Name:		xfce4-plugin-mount
Version:	0.6.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-mount-plugin/0.6/%{rname}-%{version}.tar.bz2
# Source0-md5:	f5917e9aa2a06bc6a872cc10d2ee4f6f
# https://bugzilla.xfce.org/show_bug.cgi?id=9127
Patch0:		%{name}-label-mount.patch
# https://bugzilla.xfce.org/show_bug.cgi?id=9399
Patch1:		%{name}-position-the-popup-menu-nicely.patch
# https://bugzilla.xfce.org/show_bug.cgi?id=9400
PAtch2:		%{name}-exclude-multiple-mount-points.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-mount-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkg-config
BuildRequires:	xfce4-panel-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin let's you easy mount/umount and check space uvailable on
destdevice.

%prep
%setup -qn %{rname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{rname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{rname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libmount.so
%{_datadir}/xfce4/panel/plugins/xfce4-mount-plugin.desktop
%{_iconsdir}/hicolor/*/apps/*.*

