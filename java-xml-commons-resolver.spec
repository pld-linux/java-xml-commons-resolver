Summary:	Apache XML Commons Resolver classes
Summary(pl):	Klasy Apache XML Commons Resolver
Name:		xml-commons-resolver
Version:	1.0
Release:	0.1
License:	Apache Software License
Group:		Development/Languages/Java
Source0:	http://xml.apache.org/dist/commons/%{name}-1.0.tar.gz
# Source0-md5:	4f54cf02d211abd95513699d088ae968
URL:		http://xml.apache.org/commons/
BuildRequires: 	jakarta-ant
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
The Apache XML Commons Resolver classes implement Catalog-based entity
and URI resolution.

%description -l pl
Klasy Apache XML Commons Resolver s± implementacj± rozwi±zywania encji
i URI na podstawie katalogu.

%prep
%setup -q

rm -rf `find . -name "*.jar"`
mv -f resolver.xml build.xml

%build
ant jar docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install build/resolver.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf resolver.jar $RPM_BUILD_ROOT%{_javalibdir}/resolver-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KEYS README.* build/docs/javadocs
%{_javalibdir}/*.jar
