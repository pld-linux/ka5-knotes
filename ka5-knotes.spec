#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		knotes
Summary:	knotes
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	0a3e32cd6f36a7a54054acdf32724b56
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt5-devel >= 5.1
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-notes-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kdnssd-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kglobalaccel-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kitemmodels-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-knewstuff-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	libxslt-progs
BuildRequires:	ninja
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

%description -l pl.UTF-8
KNotes jest programem pozwalającym pisać na komputerze notatki,
odpowiedniki samoprzylepnych karteczek. Notatki są zapisywane
automatycznie przy wyjściu z programu i wyświetlane przy otwieraniu
programu. Właściwości: pisz notatki wybraną czcionką i kolorem
tła.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_notes_agent
%attr(755,root,root) %{_bindir}/knotes
%ghost %{_libdir}/libknotesprivate.so.5
%attr(755,root,root) %{_libdir}/libknotesprivate.so.5.*.*
%ghost %{_libdir}/libnotesharedprivate.so.5
%attr(755,root,root) %{_libdir}/libnotesharedprivate.so.5.*.*
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
%{_datadir}/knotes
%{_datadir}/knotifications5/akonadi_notes_agent.notifyrc
%{_datadir}/kxmlgui5/knotes
%{_datadir}/metainfo/org.kde.knotes.appdata.xml
%{_datadir}/knsrcfiles/knotes_printing_theme.knsrc
%{_datadir}/qlogging-categories5/knotes.categories
%{_datadir}/qlogging-categories5/knotes.renamecategories
%dir %{_libdir}/qt5/plugins/pim5/kcms/knotes
%{_libdir}/qt5/plugins/pim5/kcms/knotes/kcm_knote_action.so
%{_libdir}/qt5/plugins/pim5/kcms/knotes/kcm_knote_collection.so
%{_libdir}/qt5/plugins/pim5/kcms/knotes/kcm_knote_display.so
%{_libdir}/qt5/plugins/pim5/kcms/knotes/kcm_knote_editor.so
%{_libdir}/qt5/plugins/pim5/kcms/knotes/kcm_knote_misc.so
%{_libdir}/qt5/plugins/pim5/kcms/knotes/kcm_knote_network.so
%{_libdir}/qt5/plugins/pim5/kcms/knotes/kcm_knote_print.so
%{_libdir}/qt5/plugins/pim5/kcms/summary/kcmknotessummary.so
%{_libdir}/qt5/plugins/pim5/kontact/kontact_knotesplugin.so
