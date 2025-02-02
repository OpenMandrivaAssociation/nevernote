Name:		nevernote
Version:	0.99
Release:	2
Group:		Networking/Other
Summary:	Evernote-clone. Use with Evernote to remember everything
License:	GPLv2
URL:		https://nevernote.sourceforge.net/
Source:		%{name}-%{version}_i386.tar.gz
Patch:		%{name}.desktop-ru.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
#Requires:	

%description
Evernote-clone. Use with Evernote to remember everything

%prep
%setup -q -n %{name}
%patch -p0

#%build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 usr/bin/%{name}.sh %{buildroot}%{_bindir}/%{name}

install -d -m 755 %{buildroot}%{_datadir}/applications
install -m 644 usr/share/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -a usr/share/%{name}/* %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_docdir}/%{name}
install -m 644 usr/share/doc/%{name}/* %{buildroot}%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_docdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%changelog
* Sat Sep 10 2011 Sergey Zhemoitel <serg@mandriva.org> 0.99-1
+ Revision: 699175
- imported package nevernote

