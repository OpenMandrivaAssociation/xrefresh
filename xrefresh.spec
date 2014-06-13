Name:		xrefresh
Version:	1.0.5
Release:	6
Summary:	Refresh all or part of an X screen
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:	xrefresh.xpm
Source2:	xrefresh.xpm.large
Source3:	xrefresh.xpm.mini
License:	MIT

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

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
%makeinstall_std

# install icons
mkdir -p %{buildroot}%{_datadir}/icons/large
mkdir -p %{buildroot}%{_datadir}/icons/mini

install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/xrefresh.xpm
install -m0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/large/xrefresh.xpm
install -m0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/mini/xrefresh.xpm

%files
%{_bindir}/xrefresh
%{_mandir}/man1/xrefresh.1*
%{_datadir}/icons/xrefresh.xpm
%{_datadir}/icons/*/xrefresh.xpm


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 671361
- mass rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 464749
- New version: 1.0.3

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-6mdv2009.1
+ Revision: 350796
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-5mdv2009.0
+ Revision: 226075
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-4mdv2008.1
+ Revision: 154357
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2008.1
+ Revision: 130517
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode lzma extension!!!


* Fri Nov 17 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-3mdv2007.0
+ Revision: 85375
- added missing icons
- rebuild to fix cooker uploading
- X11R7.1
- increment release
- Adding X.org 7.0 to the repository

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fill in missing descriptions

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

