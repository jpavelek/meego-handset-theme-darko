Name:		darko-lite
Version:	0.1
Release:	1%{?dist}
Summary:	Darko-lite is a theme for MeeGo Handset
Group:		User Interface/Desktops
License:	Creative Commons Attribution-NonCommercial 3.0 Unported License
URL:		https://github.com/jpavelek/meego-handset-theme-darko
Source0:	file://darko-lite.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Darko-lite is a theme for MeeGo Handset. 

%prep
%setup -q

%build
%configure

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/themes/darko/meegotouch/icons
install -m 755 meegotouch/icons/* %{buildroot}/usr/share/themes/darko/meegotouch/icons/
install -m 755 index.theme %{buildroot}/usr/share/themes/darko/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc

%changelog
* Sat Sep 24 2011 Jakub Pavelek <jpavelek@live.com> 0.1
- first RPM packaging release

