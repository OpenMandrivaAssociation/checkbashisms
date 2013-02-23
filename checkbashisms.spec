Summary:	Check shell scripts for common bash-specific contructs
Name:		checkbashisms
Version:	1.10.39
Release:	4
# svn export svn://svn.debian.org/svn/devscripts/trunk/scripts/checkbashisms.pl
Source0:	checkbashisms.pl
# svn export svn://svn.debian.org/svn/devscripts/trunk/scripts/checkbashisms.1
Source1:	checkbashisms.1
License:	GPLv2+
Group:		Development/Other
Url:		http://packages.debian.org/sid/devscripts
BuildArch:	noarch

%description
checkbashisms checks whether a /bin/sh script contains any common
bash-specific contructs.
It is extracted from the Debian devscripts package.

%prep
%setup -q -T -c

%build

%install
install -d %{buildroot}%{_bindir}
install -m755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}.pl
install -d %{buildroot}%{_mandir}/man1
install -m644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}.pl
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.10.39-3mdv2011.0
+ Revision: 616996
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 2.10.39-2mdv2010.0
+ Revision: 436991
- rebuild

* Mon Oct 13 2008 Olivier Blin <oblin@mandriva.com> 2.10.39-1mdv2009.1
+ Revision: 293329
- initial package (extracted from Debian devscripts package)
- create checkbashisms

