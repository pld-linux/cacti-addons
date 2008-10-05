# TODO
# - add more scripts,addons, but as separate packages
# - patches for path to files (bin,includes)
# - instead of using /usr/bin/php macro, make scripts executable with #!/usr/bin/php !
%include	/usr/lib/rpm/macros.perl
Summary:	Add-ons for Cacti
Summary(pl.UTF-8):	Dodatki do Cacti
Name:		cacti-addons
Version:	0.1
Release:	0.13
License:	GPL v2
Group:		Applications/WWW
# Show locked Machines, Shares and Files from a Samba Server - http://forums.cacti.net/about7516.html
Source0:	http://forums.cacti.net/files/samba.tar.gz
# Source0-md5:	b8fc04a74b8ab297fd39fb6fb02d80f4
# Cacti Poller Statistics - http://forums.cacti.net/about18057-0-asc-0.html
Source1:	http://forums.cacti.net/files/ss_poller.php.gz
# Source1-md5:	5de3f1cfeb5803a9c76a6e1472dd2478
Source2:	http://forums.cacti.net/files/cacti_host_template_local_cacti_polling_host_171.xml
# Source2-md5:	3f54a6579f06745426163685facac558
# Adding template from command line - http://forums.cacti.net/about8827.html
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
# Source7-md5:	9fa929206625d0824dff77168c85e6f8
URL:		http://www.debianhelp.co.uk/cactitemplates.htm
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.322
BuildRequires:	unzip
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti

%description
Templates and scripts for Cacti.

%description -l pl.UTF-8
Skrypty i szablony dla Cacti.

%package Cacti_Poller_Statistics
Summary:	Statistics for Cacti Poller
Summary(pl.UTF-8):	Statystyki działania Pollera Cacti
Group:		Applications/WWW
Requires:	cacti
Requires:	cacti-add_template

%description Cacti_Poller_Statistics
Statistics for Cacti Poller, works with localhost only.

%description Cacti_Poller_Statistics -l pl.UTF-8
Statystyki działania Pollera Cacti; działają tylko lokalnie.

%package DNS_Server_Response_Time
Summary:	Cacti - Measure the response times of multiple internal and external DNS Resolver
Summary(pl.UTF-8):	Cacti - określanie czasu odpowiedzi wielu wewnętrznych lub zewnętrznych DNS-ów
Group:		Applications/WWW
Requires:	cacti
Requires:	cacti-add_template

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
Requires:	cacti
Requires:	cacti-add_template

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
Requires:	cacti
Requires:	cacti-add_template

%description hddtemp
Template to query hddtemp deamon and graph disks temperature.

%description hddtemp -l pl.UTF-8
Wykresy temperatury dysków - dane pobierane z hddtemp.

%prep
%setup -q -c -a6
gzip -dNc %{SOURCE1} > ss_poller.php

# undos the source
find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{cactidir}/cacti,%{cactidir}/scripts,%{cactidir}/resource/script_queries,%{cactidir}/resource/snmp_queries,%{cactidir}/resource/script_server,%{_bindir}}

install samba/cacti_graph_template_snmp_samba.xml $RPM_BUILD_ROOT%{cactidir}/resource
install samba/samba.pl $RPM_BUILD_ROOT%{cactidir}/scripts

install ss_poller.php $RPM_BUILD_ROOT%{cactidir}/scripts/ss_poller.php
install %{SOURCE2} $RPM_BUILD_ROOT%{cactidir}/resource/cacti_host_template_local_cacti_polling_host.xml

install %{SOURCE4} $RPM_BUILD_ROOT%{cactidir}/resource/cacti_graph_template_dnsresponsetime.xml
install %{SOURCE5} $RPM_BUILD_ROOT%{cactidir}/scripts/dnsResponseTime.pl

install cacti-linux-hddtemp-1.0/hddtemp.xml $RPM_BUILD_ROOT%{cactidir}/resource/script_queries
install cacti-linux-hddtemp-1.0/hddtemp.php $RPM_BUILD_ROOT%{cactidir}/scripts
install cacti-linux-hddtemp-1.0/cacti_graph_template_linux_hddtemp*.xml $RPM_BUILD_ROOT%{cactidir}/resource

%clean
rm -rf $RPM_BUILD_ROOT

%post Cacti_Poller_Statistics
%{_sbindir}/cacti-add_template %{cactidir}/resource/cacti_host_template_local_cacti_polling_host.xml

%post DNS_Server_Response_Time
%{_sbindir}/cacti-add_template %{cactidir}/resource/cacti_graph_template_dnsresponsetime.xml

%post Samba_locked_machine
%{_sbindir}/cacti-add_template %{cactidir}/resource/cacti_graph_template_snmp_samba.xml

%post hddtemp
%{_sbindir}/cacti-add_template %{cactidir}/resource/cacti_graph_template_linux_hddtemp_disk_temperature*.xml

%files Cacti_Poller_Statistics
%defattr(644,root,root,755)
%attr(755,root,root) %{cactidir}/scripts/ss_poller.php
%{cactidir}/resource/cacti_host_template_local_cacti_polling_host.xml

%files DNS_Server_Response_Time
%defattr(644,root,root,755)
%attr(755,root,root) %{cactidir}/scripts/dnsResponseTime.pl
%{cactidir}/resource/cacti_graph_template_dnsresponsetime.xml

%files Samba_locked_machine
%defattr(644,root,root,755)
%attr(755,root,root) %{cactidir}/scripts/samba.pl
%{cactidir}/resource/cacti_graph_template_snmp_samba.xml

%files hddtemp
%defattr(644,root,root,755)
%doc cacti-linux-hddtemp-1.0/{CHANGELOG.txt,INSTALL.txt}
%attr(755,root,root) %{cactidir}/scripts/hddtemp.php
%{cactidir}/resource/cacti_graph_template_linux_hddtemp_disk_temperature*.xml
%{cactidir}/resource/script_queries/hddtemp.xml
