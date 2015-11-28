Summary:	Python bindings for the libsmbclient API from Samba
Name:		python-smbc
Version:	1.0.13
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://cyberelk.net/tim/data/pysmbc/pysmbc-%{version}.tar.bz2
# Source0-md5:	019dbb3bc6ee217f7389a2330cda9fe0
Patch0:		%{name}-memory_leak.patch
URL:		http://cyberelk.net/tim/data/pysmbc/
BuildRequires:	libsmbclient-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for the libsmbclient API from Samba.

%prep
%setup -q -n pysmbc-%{version}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/smbc*.so
%{py_sitedir}/pysmbc-*.egg-info
