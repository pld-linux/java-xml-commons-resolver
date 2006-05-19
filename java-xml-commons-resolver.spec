Summary:	Apache XML Commons Resolver classes
Summary(pl):	Klasy Apache XML Commons Resolver
Name:		xml-commons-resolver
Version:	1.1
Release:	1
License:	Apache v1.1
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/xml/commons/%{name}-%{version}.tar.gz
# Source0-md5:	deb95bdf88687430445d34e8c11d475e
Patch0:		%{name}-source1.4.patch
URL:		http://xml.apache.org/commons/
BuildRequires:	ant
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
The Apache XML Commons Resolver classes implement Catalog-based entity
and URI resolution.

%description -l pl
Klasy Apache XML Commons Resolver s± implementacj± rozwi±zywania encji
i URI na podstawie katalogu.

%prep
%setup -q
%patch0 -p1

rm -rf `find . -name "*.jar"`
mv -f resolver.xml build.xml

%build
ant jar javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install build/resolver.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf resolver.jar $RPM_BUILD_ROOT%{_javalibdir}/resolver-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KEYS LICENSE.resolver.txt build/apidocs
%{_javalibdir}/*.jar
