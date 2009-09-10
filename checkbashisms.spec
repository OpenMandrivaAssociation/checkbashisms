%define name checkbashisms
%define version 2.10.39
%define release %mkrel 2

Summary: Check shell scripts for common bash-specific contructs
Name: %{name}
Version: %{version}
Release: %{release}
# svn export svn://svn.debian.org/svn/devscripts/trunk/scripts/checkbashisms.pl
Source0: checkbashisms.pl
# svn export svn://svn.debian.org/svn/devscripts/trunk/scripts/checkbashisms.1
Source1: checkbashisms.1
License: GPLv2+
Group: Development/Other
Url: http://packages.debian.org/sid/devscripts
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
checkbashisms checks whether a /bin/sh script contains any common
bash-specific contructs.
It is extracted from the Debian devscripts package.

%prep
%setup -q -T -c

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}.pl
install -d %{buildroot}%{_mandir}/man1
install -m644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}.pl
%{_mandir}/man1/%{name}.1*
