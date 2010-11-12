Name: xrefresh
Version: 1.0.4
Release: %mkrel 1
Summary: Refresh all or part of an X screen
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1: xrefresh.xpm
Source2: xrefresh.xpm.large
Source3: xrefresh.xpm.mini
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xrefresh is a simple X program that causes all or part of your screen to be
repainted. This is useful when system messages have messed up your screen.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# install icons
mkdir -p %{buildroot}%{_datadir}/icons/large
mkdir -p %{buildroot}%{_datadir}/icons/mini

install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/xrefresh.xpm
install -m0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/large/xrefresh.xpm
install -m0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/mini/xrefresh.xpm

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xrefresh
%{_mandir}/man1/xrefresh.1*
%{_datadir}/icons/xrefresh.xpm
%{_datadir}/icons/*/xrefresh.xpm
