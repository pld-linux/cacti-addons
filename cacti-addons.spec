# TODO
# - add more scripts,addons 
# - patches for path to files (bin,includes)
# - %%post - add template to cacti
# - instead of using %{__php} macro, make scripts executable with #!/usr/bin/php !
%define		namesrc	cacti_templates
%include	/usr/lib/rpm/macros.perl
Summary:	Add-ons for Cacti
Summary(pl.UTF-8):	Dodatki do Cacti
Name:		cacti-addons
Version:	0.1
Release:	0.3
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
# MySQL Host Template - http://www.faemalia.net/mysqlUtils/ , http://forums.cacti.net/viewtopic.php?t=11010
Source7:	http://www.faemalia.net/mysqlUtils/teMySQLcacti-20060810.tar.gz
# Source5-md5:	
Patch0:		%{name}-add_template.patch
URL:		http://www.debianhelp.co.uk/cactitemplates.htm
BR:	 - instead of using %{__php} macro, make scripts executable with #!/usr/bin/php !
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.322
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactiroot		/usr/share/cacti
%define		webcactiscriptdir	%{webcactiroot}/scripts
%define		webcactiscrptserverdir	%{webcactiroot}/resource/script_server
%define		webcactiscriptqueriesdir %{webcactiroot}/resource/script_queries
%define		webcactisnmpqueriesdir	%{webcactiroot}/resource/snmp_queries
%define		__php			%{_bindir}/php

%description
Templates and scripts for Cacti.

%description -l pl.UTF-8
Skrypty i szablony dla Cacti.

%package Cacti_Poller_Statistics
Summary:	Statistics for Cacti Poller
Summary(pl.UTF-8):	Statystyki działania Pollera Cacti
Group:		Applications/WWW
Requires:	%{name}-cmd_line_add_template

%description Cacti_Poller_Statistics
Statistics for Cacti Poller, works with localhost only.

%description Cacti_Poller_Statistics -l pl.UTF-8
Statystyki działania Pollera Cacti; działają tylko lokalnie.

%package cmd_line_add_template
Summary:	Adding template for Cacti from command line
Summary(pl.UTF-8):	Dodawanie szablonów dla Cacti z linii poleceń
Group:		Applications/WWW

%description cmd_line_add_template
Adding template for Cacti from command line. Usage :
/usr/share/cacti/cacti/add_template.php your_template.xml

%description cmd_line_add_template -l pl.UTF-8
Dodawanie szablonu dla Cacti z linii poleceń. Wywołanie:
/usr/share/cacti/cacti/add_template.php your_template.xml

%package DNS_Server_Response_Time
Summary:	Cacti - Measure the response times of multiple internal and external DNS Resolver
Summary(pl.UTF-8):	Cacti - określanie czasu odpowiedzi wielu wewnętrznych lub zewnętrznych DNS-ów
Group:		Applications/WWW
Requires:	%{name}-cmd_line_add_template

%description DNS_Server_Response_Time
Measure the response times of multiple internal and external DNS
Resolvers. The Perl script launches queries repeatedly (after holdoff
delay between queries) during Cacti default sample interval of 300
seconds and the returns minimum, median, average and maximum response
times.

%description DNS_Server_Response_Time -l pl.UTF-8
Określanie czasu odpowiedzi wielu wewnętrznych lub zewnętrznych
DNS-ów. Skrypt w perlu powtarza zapytania (z określonym odstępem
między nimi) w czasie domyślnych 300-sekundowych interwałów czasowych
Cacti i zwraca czasy odpowiedzi minimalne, średnie, maksymalne oraz
ich mediany.

%package Samba_locked_machine
Summary:	Graphs the locked machines, shares and files from a Samba server
Summary(pl.UTF-8):	Wykresy zablokowanych stacji, udziałów i plików z serwera Samby
Group:		Applications/WWW
Requires:	%{name}-cmd_line_add_template

%description Samba_locked_machine
Add-on for Cacti: graphs the locked machines, shares and files from a
Samba server in gauge mode.

%description Samba_locked_machine -l pl.UTF-8
Dodatek do cacti: wykresy zablokowanych stacji, udziałów i plików z
serwera Samby.

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
gzip -dNc %{SOURCE1} > ss_poller.php
%patch0 -p1
# undos the source
find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{webcactiroot}/cacti,%{webcactiscriptdir},%{webcactiscriptqueriesdir},%{webcactisnmpqueriesdir},%{webcactiscrptserverdir},%{_bindir}}

install samba/cacti_graph_template_snmp_samba.xml $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}
install samba/samba.pl $RPM_BUILD_ROOT%{webcactiscriptdir}

install ss_poller.php $RPM_BUILD_ROOT%{webcactiscriptdir}/ss_poller.php
install %{SOURCE2} $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}/cacti_host_template_local_cacti_polling_host.xml

install cacti/add_template.php $RPM_BUILD_ROOT%{webcactiroot}/add_template.php

install %{SOURCE4} $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}/cacti_graph_template_dnsresponsetime.xml
install %{SOURCE5} $RPM_BUILD_ROOT%{webcactiscriptdir}/dnsResponseTime.pl

install cacti-linux-hddtemp-1.0/hddtemp.xml $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}
install cacti-linux-hddtemp-1.0/hddtemp.php $RPM_BUILD_ROOT%{webcactiscriptdir}
install cacti-linux-hddtemp-1.0/cacti_graph_template_linux_hddtemp*.xml $RPM_BUILD_ROOT%{webcactiscriptqueriesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post Cacti_Poller_Statistics 
%{__php} %{webcactiroot}/add_template.php  %{webcactiscriptqueriesdir}/cacti_host_template_local_cacti_polling_host.xml

%post DNS_Server_Response_Time
%{__php} %{webcactiroot}/add_template.php %{webcactiscriptqueriesdir}/cacti_graph_template_dnsresponsetime.xml

%post Samba_locked_machine
%{__php} %{webcactiroot}/add_template.php %{webcactiscriptqueriesdir}/cacti_graph_template_snmp_samba.xml

%post hddtemp
%{__php} %{webcactiroot}/add_template.php %{webcactiscriptqueriesdir}/cacti_graph_template_linux_hddtemp_disk_temperature*.xml

%files Cacti_Poller_Statistics
%defattr(644,root,root,755)
%attr(755,root,root) %{webcactiscriptdir}/ss_poller.php
%{webcactiscriptqueriesdir}/cacti_host_template_local_cacti_polling_host.xml

%files cmd_line_add_template
%defattr(644,root,root,755)
%attr(755,root,root) %{webcactiroot}/add_template.php

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
