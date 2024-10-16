Summary:	System tray application for accessing Zotero references
Name:		qnotero
Version:	2.3.1
Release:	1
Source0:	https://github.com/ealbiter/qnotero/archive/refs/tags/v%{version}.tar.gz
License:	GPLv3+ 
Group:		Publishing
Url:		https://www.cogsci.nl/software/qnotero/
BuildArch:	noarch
Requires:	python-qt5
BuildRequires:	python-qt5, python-devel

%description
Qnotero provides lightning quick access to your Zotero
references. Zotero is an excellent open source reference manager, but
it lacks a simple and direct way to access your references at the
click of a button. That is why I created this simple program, which
lives in the system tray and allows you to search through your
references by Author and/ or Year of Publication. If a PDF file is
attached to a reference you can open it directly from within Qnotero.

%prep
%autosetup -p1

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files -f FILE_LIST
%defattr(-,root,root)
