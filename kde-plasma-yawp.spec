Name:           kde-plasma-yawp
Version:        0.4.3
Release:        1%{?dist}
Summary:        Yet Another Weather Plasmoid

License:        GPLv2
URL:            http://yawp.sourceforge.net/
Source0:        http://downloads.sourceforge.net/yawp/yawp-%{version}.tar.bz2

BuildRequires:  kde-filesystem
BuildRequires:  kde-workspace-devel
BuildRequires:  qt4-devel
BuildRequires:  cmake
BuildRequires:  gettext


%description
There is nothing wrong with the ones that exist, I just wanted something
more colorful.

%prep
%setup -q -n yawp-%{version}


%build
%cmake
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang plasma_applet_yawp

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f plasma_applet_yawp.lang
%doc CHANGELOG COPYRIGHT LICENSE-GPL2 README TODO
%{_kde4_libdir}/kde4/*
%{_kde4_appsdir}/desktoptheme/default/widgets/yawp_theme15.svg
%{_kde4_datadir}/kde4/services/*.desktop


%changelog
* Mon Sep 03 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.4.3-1.R
- Initial release
