%define		_name		weather
Summary:	Infocom text game - Weather
Summary(pl):	Tekstówka Infocomu - Weather
Name:		infocom-weather
Version:	960613
Release:	1
License:	free
Group:		Applications/Games
Source0:	ftp://ftp.ifarchive.org/if-archive/games/zcode/%{_name}.z5
# Source0-md5:	cc322af1a8ca3d8c943b24b84bda3f98
URL:		http://www.ifarchive.org/
Requires:	frotz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Walking away from a picknick, you are suddenly couhgt in a country
storm. You must protect a bridge from being destroyed.

An ultra-linear game.

Competition 1995: 1st place.

%description -l pl
Opuszczaj±c piknik wpad³e¶ nagle w burzê na prowincji. Musisz uchroniæ
od zniszczenia most.

Skrajnie liniowa gra.

Konkurs 1995: pierwsze miejsce.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/zcode}

cp %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/games/zcode
ln -s %{_datadir}/games/zcode/wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/zcode/*.z5
