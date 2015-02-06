%define name	qnotero
%define version	0.48
%define release 2

Summary:	System tray application for accessing Zotero references
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.cogsci.nl/software/qnotero/%{name}_%{version}.tar.gz
License:	GPLv3+ 
Group:		Publishing
Url:		http://www.cogsci.nl/software/qnotero/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-qt4
BuildRequires:	python-qt4, python-devel

%description
Qnotero provides lightning quick access to your Zotero
references. Zotero is an excellent open source reference manager, but
it lacks a simple and direct way to access your references at the
click of a button. That is why I created this simple program, which
lives in the system tray and allows you to search through your
references by Author and/ or Year of Publication. If a PDF file is
attached to a reference you can open it directly from within Qnotero.

%prep
%setup -q -n %{name}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc COPYING README


%changelog
* Tue Mar 06 2012 Lev Givon <lev@mandriva.org> 0.48-1mdv2011.0
+ Revision: 782520
- Update to 0.48.

* Thu Feb 02 2012 Lev Givon <lev@mandriva.org> 0.47-1
+ Revision: 770786
- imported package qnotero

