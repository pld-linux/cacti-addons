# TODO
# - separate packages for templates from here
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.perl
%include	/usr/lib/rpm/macros.php
Summary:	Add-ons for Cacti
Summary(pl.UTF-8):	Dodatki do Cacti
Name:		cacti-addons
Version:	0.1
Release:	0.14
License:	GPL v2
Group:		Applications/WWW
# Show locked Machines, Shares and Files from a Samba Server - http://forums.cacti.net/about7516.html
Source0:	http://forums.cacti.net/files/samba.tar.gz
# Source0-md5:	b8fc04a74b8ab297fd39fb6fb02d80f4
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
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.554
BuildRequires:	unzip
Requires:	cacti >= 0.8.7e-8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti

%description
Templates and scripts for Cacti.

%description -l pl.UTF-8
Skrypty i szablony dla Cacti.

%package DNS_Server_Response_Time
Summary:	Cacti - Measure the response times of multiple internal and external DNS Resolver
Summary(pl.UTF-8):	Cacti - określanie czasu odpowiedzi wielu wewnętrznych lub zewnętrznych DNS-ów
Group:		Applications/WWW
Requires:	cacti >= 0.8.7e-8

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
Requires:	cacti >= 0.8.7e-8

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
Requires:	cacti >= 0.8.7e-8
Requires:	php-common >= 4:%{php_min_version}

%description hddtemp
Template to query hddtemp deamon and graph disks temperature.

%description hddtemp -l pl.UTF-8
Wykresy temperatury dysków - dane pobierane z hddtemp.

%prep
%setup -q -c -a6
%undos -f php,inc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{cactidir}/cacti,%{cactidir}/scripts,%{cactidir}/resource/script_queries,%{cactidir}/resource/snmp_queries,%{cactidir}/resource/script_server,%{_bindir}}

cp -p samba/cacti_graph_template_snmp_samba.xml $RPM_BUILD_ROOT%{cactidir}/resource
install -p samba/samba.pl $RPM_BUILD_ROOT%{cactidir}/scripts

cp -p %{SOURCE4} $RPM_BUILD_ROOT%{cactidir}/resource/cacti_graph_template_dnsresponsetime.xml
install -p %{SOURCE5} $RPM_BUILD_ROOT%{cactidir}/scripts/dnsResponseTime.pl

cp -p cacti-linux-hddtemp-1.0/hddtemp.xml $RPM_BUILD_ROOT%{cactidir}/resource/script_queries
cp -p cacti-linux-hddtemp-1.0/hddtemp.php $RPM_BUILD_ROOT%{cactidir}/scripts
cp -p cacti-linux-hddtemp-1.0/cacti_graph_template_linux_hddtemp*.xml $RPM_BUILD_ROOT%{cactidir}/resource

%clean
rm -rf $RPM_BUILD_ROOT

%post DNS_Server_Response_Time
%cacti_import_template %{cactidir}/resource/cacti_graph_template_dnsresponsetime.xml

%post Samba_locked_machine
%cacti_import_template %{cactidir}/resource/cacti_graph_template_snmp_samba.xml

%post hddtemp
%cacti_import_template %{cactidir}/resource/cacti_graph_template_linux_hddtemp_disk_temperature*.xml

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
