Name:		darko
Version:	0.1
Release:	1%{?dist}
Summary:	Darko is a theme for MeeGo Handset
Group:		User Interface/Desktops
License:	Creative Commons Attribution-NonCommercial 3.0 Unported License
URL:		https://github.com/jpavelek/meego-handset-theme-darko
Source0:	file://darko-0.1.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch

%description
Darko is a theme for MeeGo Handset.  Besides icon set it brings some small theming changes all over the place.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/themes/darko/
install -m 755 index.theme %{buildroot}/usr/share/themes/darko/
mkdir -p %{buildroot}/usr/share/themes/darko/meegotouch/icons
install -m 755 meegotouch/icons/* %{buildroot}/usr/share/themes/darko/meegotouch/icons/
mkdir -p %{buildroot}/usr/share/themes/darko/meegotouch/libmeegotouchviews/style/
install -m 755 meegotouch/libmeegotouchviews/style/* %{buildroot}/usr/share/themes/darko/meegotouch/libmeegotouchviews/style/
mkdir -p %{buildroot}/usr/share/themes/darko/meegotouch/images/
install -m 755 meegotouch/images/* %{buildroot}/usr/share/themes/darko/meegotouch/images/
mkdir -p %{buildroot}/usr/share/themes/darko/meegotouch/svg/
install -m 755 meegotouch/svg/* %{buildroot}/usr/share/themes/darko/meegotouch/svg/
mkdir -p %{buildroot}/usr/share/themes/darko/meegotouch/libmeegotouchhome/style/
install -m 755 meegotouch/libmeegotouchhome/style/* %{buildroot}/usr/share/themes/darko/meegotouch/libmeegotouchhome/style/
install -m 755 meegotouch/libmeegotouchhome/libmeegotouchhome.conf %{buildroot}/usr/share/themes/darko/meegotouch/libmeegotouchhome/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/themes/darko/*

%changelog
* Sat Sep 24 2011 Jakub Pavelek <jpavelek@live.com> 0.1
- first RPM packaging release

