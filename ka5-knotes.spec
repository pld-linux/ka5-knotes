%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		knotes
Summary:	knotes
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a3cc030d0ccdf73329122bb9e9db1403
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt5-devel >= 5.1
BuildRequires:	ka5-akonadi-devel >= 18.12.0
BuildRequires:	ka5-akonadi-notes-devel >= 18.12.0
BuildRequires:	ka5-akonadi-search-devel >= 18.12.0
BuildRequires:	ka5-kcalutils-devel >= 18.12.0
BuildRequires:	ka5-kmime-devel >= 18.12.0
BuildRequires:	ka5-kontactinterface-devel >= 18.12.0
BuildRequires:	ka5-kpimtextedit-devel >= 18.12.0
BuildRequires:	ka5-libkdepim-devel >= 18.12.0
BuildRequires:	ka5-pimcommon-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-kcmutils-devel >= 5.51.0
BuildRequires:	kf5-kcompletion-devel >= 5.51.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.51.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.51.0
BuildRequires:	kf5-kcrash-devel >= 5.51.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.51.0
BuildRequires:	kf5-kdelibs4support-devel >= 5.51.0
BuildRequires:	kf5-kdnssd-devel >= 5.51.0
BuildRequires:	kf5-kdoctools-devel >= 5.51.0
BuildRequires:	kf5-kglobalaccel-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kitemmodels-devel >= 5.51.0
BuildRequires:	kf5-kitemviews-devel >= 5.51.0
BuildRequires:	kf5-knewstuff-devel >= 5.51.0
BuildRequires:	kf5-knotifications-devel >= 5.51.0
BuildRequires:	kf5-knotifyconfig-devel >= 5.51.0
BuildRequires:	kf5-kparts-devel >= 5.51.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.51.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.51.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.51.0
BuildRequires:	kf5-kxmlgui-devel >= 5.51.0
BuildRequires:	libxslt-progs
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNotes is a program that lets you write the computer equivalent of
sticky notes. The notes are saved automatically when you exit the
program, and they display when you open the program. Features. Write
notes in your choice of font and background color.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/knotes.categories
/etc/xdg/knotes.renamecategories
/etc/xdg/knotes_printing_theme.knsrc
%attr(755,root,root) %{_bindir}/akonadi_notes_agent
%attr(755,root,root) %{_bindir}/knotes
%attr(755,root,root) %ghost %{_libdir}/libknotesprivate.so.5
%attr(755,root,root) %{_libdir}/libknotesprivate.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libnotesharedprivate.so.5
%attr(755,root,root) %{_libdir}/libnotesharedprivate.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_knote.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_knotessummary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact_knotesplugin.so
%{_datadir}/akonadi/agents/notesagent.desktop
%{_desktopdir}/org.kde.knotes.desktop
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_datadir}/config.kcfg/notesagentsettings.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KNotes.xml
%{_datadir}/dbus-1/interfaces/org.kde.kontact.KNotes.xml
%{_iconsdir}/hicolor/128x128/apps/knotes.png
%{_iconsdir}/hicolor/16x16/actions/knotes_alarm.png
%{_iconsdir}/hicolor/16x16/actions/knotes_close.png
%{_iconsdir}/hicolor/16x16/actions/knotes_date.png
%{_iconsdir}/hicolor/16x16/actions/knotes_delete.png
%{_iconsdir}/hicolor/16x16/apps/knotes.png
%{_iconsdir}/hicolor/22x22/apps/knotes.png
%{_iconsdir}/hicolor/32x32/apps/knotes.png
%{_iconsdir}/hicolor/48x48/apps/knotes.png
%{_iconsdir}/hicolor/64x64/apps/knotes.png
%{_iconsdir}/hicolor/scalable/apps/knotes.svg
%{_datadir}/kconf_update/knotes-15.08-kickoff.sh
%{_datadir}/kconf_update/knotes.upd
%{_datadir}/knotes
%{_datadir}/knotifications5/akonadi_notes_agent.notifyrc
%dir %{_datadir}/kontact/ksettingsdialog
%{_datadir}/kontact/ksettingsdialog/knotes.setdlg
%{_datadir}/kservices5/kcmknotessummary.desktop
%{_datadir}/kservices5/knote_config_action.desktop
%{_datadir}/kservices5/knote_config_collection.desktop
%{_datadir}/kservices5/knote_config_display.desktop
%{_datadir}/kservices5/knote_config_editor.desktop
%{_datadir}/kservices5/knote_config_misc.desktop
%{_datadir}/kservices5/knote_config_network.desktop
%{_datadir}/kservices5/knote_config_print.desktop
%{_datadir}/kservices5/kontact/knotesplugin.desktop
%{_datadir}/kxmlgui5/knotes
%{_datadir}/metainfo/org.kde.knotes.appdata.xml
