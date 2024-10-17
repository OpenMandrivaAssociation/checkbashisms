Summary:	Check shell scripts for common bash-specific contructs
Name:		checkbashisms
Version:	2.23.7
Epoch:		1
Release:	1
Url:		https://sourceforge.net/projects/checkbaskisms/
Source0:	http://downloads.sourceforge.net/project/checkbaskisms/%{version}/%{name}
# svn export svn://svn.debian.org/svn/devscripts/trunk/scripts/checkbashisms.1
Source1:	checkbashisms.1
License:	GPLv2+
Group:		Development/Other
BuildArch:	noarch

%description
Performs basic checks on shell scripts for 
the presence of non portable syntax.

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

