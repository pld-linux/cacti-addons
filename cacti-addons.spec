# TODO	- add another
#	- patches for path to files
#	- %post - add template to cacti
%define		namesrc	cacti_templates
%include	/usr/lib/rpm/macros.perl
Summary:	Add-ons for Cacti
Summary(pl.UTF-8):	Dodatki do Cacti
Name:		cacti-addons
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#Show locked Machines, Shares and Files from a Samba Server - http://forums.cacti.net/about7516.html
Source0:	http://forums.cacti.net/files/samba.tar.gz
# Source0-md5:	b8fc04a74b8ab297fd39fb6fb02d80f4
# Cacti Poller Statistics - http://forums.cacti.net/about18057-0-asc-0.html
Source1:	http://forums.cacti.net/files/ss_poller.php.gz
# Source1-md5:	5de3f1cfeb5803a9c76a6e1472dd2478
Source2:	http://forums.cacti.net/files/cacti_host_template_local_cacti_polling_host_171.xml
# Source2-md5:	3f54a6579f06745426163685facac558
# Adding template from command line - http://forums.cacti.net/about8827.html
Source3:	http://forums.cacti.net/files/add_template.zip
# Source3-md5:	a38f01091cb4bf1dbd86db29d6c4c966
# DNS Server Response Time - http://forums.cacti.net/about6332.html
Source4:	http://forums.cacti.net/files/cacti_graph_template_dnsresponsetime_204__fixed_timeout_and_interval_161.xml
# Source4-md5:	abf46930508377099b37d696648ce7de
Source5:	http://forums.cacti.net/files/dnsresponsetimeloop_115.txt
# Source5-md5:	0844f7d58ff77904416dee5b120c31cf
# hddtemp - http://forums.cacti.net/about15020.html , http://forums.cacti.net/about15743.html
#URL:	http://www.pawelko.net/Cacti/3-Hddtemp-Template-For-Cacti
Source6:	http://www.pawelko.net/xmedia/cacti/cacti-linux-hddtemp-1.0.tar.gz
# Source6-md5:	d08898b43978ccbd863076c4b3124987
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
Requires:	%{name}-cmd_line_add_template

%description Cacti_Poller_Statistics
Statistics for Cacti Poller, works with localhost only.

%description Cacti_Poller_Statistics -l pl.UTF-8
Statystyki działania Pollera Cacti, działa tylko lokalnie.

%package cmd_line_add_template
Summary:	Adding template for Cacti from command line
Summary(pl.UTF-8):	Dodawanie template dla cacti z lini poleceń
Group:		Applications/WWW

%description cmd_line_add_template
Adding template for Cacti from command line. Usage :
/usr/share/cacti/cacti/add_template.php your_template.xml

%description cmd_line_add_template -l pl.UTF-8
Dodawanie template dla cacti z lini poleceń. Usage :
/usr/share/cacti/cacti/add_template.php your_template.xml

%package DNS_Server_Response_Time
Summary:	Cacti - Measure the response times of multiple internal and external DNS Resolver
Summary(pl.UTF-8):	Cacti -
Group:		Applications/WWW
Requires:	%{name}-cmd_line_add_template

%description DNS_Server_Response_Time
Measure the response times of multiple internal and external DNS
Resolvers. The Perl script launches queries repeatedly (after holdoff
delay between queries) during Cacti default sample intervall of 300
seconds and the returns minimum, median, average and maximum response
times.

%package Samba_locked_machine
Summary:	Graphs the locked machines, shares and files from a samba server
Summary(pl.UTF-8):	Samba - wykresy przyłączonych stacji, udziałów i plików w Cacti
Group:		Applications/WWW
Requires:	%{name}-cmd_line_add_template

%description Samba_locked_machine
Add-on for Cacti - graphs the locked machines, shares and files from a
samba server in gauge mode.

%description Samba_locked_machine -l pl.UTF-8
Dodatek do cacti - Samba - wykresy przyłączonych stacji, udziałów
i plików.

%package hddtemp
Summary:	Template to query hddtemp deamon and graph disks temperature
Summary(pl.UTF-8):	Wykresy temperatury dysków - dane pobierane z hddtemp
Group:		Applications/WWW
Requires:	%{name}-cmd_line_add_template

%description hddtemp
Template to query hddtemp deamon and graph disks temperature.

%description hddtemp -l pl.UTF-8
Wykresy temperatury dysków - dane pobierane z hddtemp.

%prep
%setup -q -c -a3 -a6
gzip -dNc %{SOURCE1} > ./ss_poller.php

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{webcactiroot}/cacti,%{webcactiscriptdir},%{webcactiscriptqueriesdir},%{webcactisnmpqueriesdir},%{webcactiscrptserverdir},%{_bindir}}

install samba/cacti_graph_template_snmp_samba.xml $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}
install samba/samba.pl $RPM_BUILD_ROOT%{webcactiscriptdir}

install ss_poller.php $RPM_BUILD_ROOT%{webcactiscriptdir}/ss_poller.php
install %{SOURCE2} $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}/cacti_host_template_local_cacti_polling_host.xml

install cacti/add_template.php $RPM_BUILD_ROOT%{webcactiroot}/cacti/add_template.php

install %{SOURCE4} $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}/cacti_graph_template_dnsresponsetime.xml
install %{SOURCE5} $RPM_BUILD_ROOT%{webcactiscriptdir}/dnsResponseTime.pl

install cacti-linux-hddtemp-1.0/hddtemp.xml $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}
install cacti-linux-hddtemp-1.0/hddtemp.php $RPM_BUILD_ROOT%{webcactiscriptdir}
install cacti-linux-hddtemp-1.0/cacti_graph_template_linux_hddtemp*.xml $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post Cacti_Poller_Statistics 
%{webcactiroot}/cacti/add_template.php  %{webcactiscriptqueriesdir}/cacti_host_template_local_cacti_polling_host.xml

%post DNS_Server_Response_Time
%{webcactiroot}/cacti/add_template.php %{webcactiscriptqueriesdir}/cacti_graph_template_dnsresponsetime.xml

%post Samba_locked_machine
%{webcactiroot}/cacti/add_template.php %{webcactiscriptqueriesdir}/cacti_graph_template_snmp_samba.xml

%post hddtemp
%{webcactiroot}/cacti/add_template.php %{webcactiscriptqueriesdir}/cacti_graph_template_linux_hddtemp_disk_temperature*.xml

%files Cacti_Poller_Statistics
%defattr(644,root,root,755)
%attr(755,root,root) %{webcactiscriptdir}/ss_poller.php
%{webcactiscriptqueriesdir}/cacti_host_template_local_cacti_polling_host.xml

%files cmd_line_add_template
%defattr(644,root,root,755)
%attr(755,root,root) %{webcactiroot}/cacti/add_template.php

%files DNS_Server_Response_Time
%defattr(644,root,root,755)
%attr(755,root,root) %{webcactiscriptdir}/dnsResponseTime.pl
%{webcactiscriptqueriesdir}/cacti_graph_template_dnsresponsetime.xml

%files Samba_locked_machine
%defattr(644,root,root,755)
%attr(755,root,root) %{webcactiscriptdir}/samba.pl
%{webcactiscriptqueriesdir}/cacti_graph_template_snmp_samba.xml

%files hddtemp 
%defattr(644,root,root,755)
%doc cacti-linux-hddtemp-1.0/{CHANGELOG.txt,INSTALL.txt}
%attr(755,root,root) %{webcactiscriptdir}/hddtemp.php
%{webcactiscriptqueriesdir}/cacti_graph_template_linux_hddtemp_disk_temperature*.xml
%{webcactiscriptqueriesdir}/hddtemp.xml
