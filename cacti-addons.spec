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
Source0:	http://forums.cacti.net/files/ss_poller.php.gz
# Source0-md5:	5de3f1cfeb5803a9c76a6e1472dd2478
Source1:	http://forums.cacti.net/files/cacti_host_template_local_cacti_polling_host_171.xml
# Source1-md5:	3f54a6579f06745426163685facac558
# Adding template from command line - http://forums.cacti.net/about8827.html
Source2:	http://forums.cacti.net/files/add_template.zip
# Source2-md5:	a38f01091cb4bf1dbd86db29d6c4c966
URL:		http://www.debianhelp.co.uk/cactitemplates.htm
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactiroot		/usr/share/cacti
%define		webcactiscriptdir	%{webcactiroot}/scripts
%define		webcactiscrptserverdir	%{webcactiroot}/resource/script_server
%define		webcactiscriptqueriesdir %{webcactiroot}/resource/script_queries
%define		webcactisnmpqueriesdir	%{webcactiroot}/resource/snmp_queries

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

%package cmd_line_add_template
Summary:	Adding template for Cacti from command line
Summary(pl.UTF-8):	Dodawanie template dla cacti z lini poleceń
Group:		Applications/WWW

%description cmd_line_add_template
Adding template for Cacti from command line.
Usage : /usr/share/cacti/cacti/add_template.php your_template.xml 

%description cmd_line_add_template -l pl.UTF-8
Dodawanie template dla cacti z lini poleceń.
Usage : /usr/share/cacti/cacti/add_template.php your_template.xml

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{webcactiscriptdir},%{webcactiscriptqueriesdir},%{webcactisnmpqueriesdir},%{webcactiscrptserverdir}}
gzip -dc %{SOURCE0} > $RPM_BUILD_ROOT%{webcactiscriptdir}/ss_poller.php
install %{SOURCE1} $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}/cacti_host_template_local_cacti_polling_host.xml

unzip -x -d $RPM_BUILD_ROOT%{webcactiroot} %{SOURCE2}

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files Cacti_Poller_Statistics
%defattr(644,root,root,755)
%{webcactiscriptdir}/ss_poller.php
%{webcactiscriptqueriesdir}/cacti_host_template_local_cacti_polling_host.xml

%files cmd_line_add_template
%defattr(644,root,root,755)
%attr(755,root,root) %{webcactiroot}/cacti/add_template.php
