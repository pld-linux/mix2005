# TODO: build guicast as separate, shared library to use in
#       xmovie, mix2005 and cinelerra
Summary:	Mix2005 - a mixer with GUI
Summary(pl.UTF-8):	Mix2005 - mikser z graficznym interfejsem
Name:		mix2005
Version:	1.2
Release:	2
# no license information in mix2005 itself, but it includes GPL libraries
# and is part of GPLed Heroine Virtual software
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/heroines/%{name}-%{version}-src.tar.bz2
# Source0-md5:	71ff79eca9e065881100334b84ae3094
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-fix.patch
URL:		http://heroinewarrior.com/mix2000.php3
BuildRequires:	alsa-lib-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	quicktime4linux-devel >= 2.2
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	alsa-lib >= 1.0.8
Requires:	quicktime4linux >= 2.2
Obsoletes:	mix2000
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mix2005 - a mixer with GUI.

%description -l pl.UTF-8
Mix2005 - mikser z graficznym interfejsem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -rf alsa-lib-* libmpeg3 quicktime

%build
CFLAGS="%{rpmcflags} -fno-rtti"; export CFLAGS
%{__make} -C guicast

%{__make} -C mix2005 \
	LXLIBDIR=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mix2005/*/mix2005 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mix2005
