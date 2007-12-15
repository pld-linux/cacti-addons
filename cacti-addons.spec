# TODO - add another
%define		namesrc	cacti_templates
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Links
Summary(pl.UTF-8):	Wtyczka do Cacti - Links
Name:		cacti-addons
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
# Cacti Poller Statistics - http://forums.cacti.net/about18057-0-asc-0.html
Source0:	http://forums.cacti.net//files/ss_poller.php.gz
# Source0-md5:	5de3f1cfeb5803a9c76a6e1472dd2478
Source1:	http://forums.cacti.net//files/cacti_host_template_local_cacti_polling_host_171.xml
# Source1-md5:	3f54a6579f06745426163685facac558
#
URL:		http://www.debianhelp.co.uk/cactitemplates.htm
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactiscriptdir /usr/share/cacti/scripts
%define		webcactiscrptserverdir /usr/share/cacti/resource/script_server
%define		webcactiscriptqueriesdir /usr/share/cacti/resource/script_queries
%define		webcactisnmpqueriesdir /usr/share/cacti/resource/snmp_queries

%description
Templates and scripts for Cacti.

%description -l pl.UTF-8
Skrypty i templaty dla Cacti.

%package Cacti_Poller_Statistics
Summary:	Statistics for Cacti Poller
Summary(pl.UTF-8):	Statystyki działania Pollera Cacti
Group:		Applications/WWW

%description Cacti_Poller_Statistics
Statistics for Cacti Poller, works with localhost only.

%description Cacti_Poller_Statistics -l pl.UTF-8
Statystyki działania Pollera Cacti, działa tylko lokalnie.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{webcactiscriptdir},%{webcactiscriptqueriesdir},%{webcactisnmpqueriesdir},%{webcactiscrptserverdir}}
gzip -dc %{SOURCE0} > $RPM_BUILD_ROOT%{webcactiscriptdir}/ss_poller.php
install %{SOURCE1} $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}/cacti_host_template_local_cacti_polling_host.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files Cacti_Poller_Statistics
%defattr(644,root,root,755)
%{webcactiscriptdir}/ss_poller.php
%{webcactiscriptqueriesdir}/cacti_host_template_local_cacti_polling_host.xml
