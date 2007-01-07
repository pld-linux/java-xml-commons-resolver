Summary:	Apache XML Commons Resolver classes
Summary(pl):	Klasy Apache XML Commons Resolver
Name:		xml-commons-resolver
Version:	1.2
Release:	1
License:	Apache v1.1
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/xml/commons/%{name}-%{version}.tar.gz
# Source0-md5:	46d52acdb67ba60f0156043f30108766
URL:		http://xml.apache.org/commons/
BuildRequires:	ant
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache XML Commons Resolver classes implement Catalog-based entity
and URI resolution.

%description -l pl
Klasy Apache XML Commons Resolver s± implementacj± rozwi±zywania encji
i URI na podstawie katalogu.

%package javadoc
Summary:	javadoc documentation for Apache XML Commons Resolver
Summary(pl):	Dokumentacja javadoc dla pakietu Apache XML Commons Resolver
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
javadoc documentation for Apache XML Commons Resolver.

%description javadoc -l pl
Dokumentacja javadoc dla pakietu Apache XML Commons Resolver.

%prep
%setup -q

rm -rf `find . -name "*.jar"`
mv -f resolver.xml build.xml

%build
export JAVA_HOME="%{java_home}"

%ant jar javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/resolver.jar $RPM_BUILD_ROOT%{_javadir}/resolver-%{version}.jar
ln -sf resolver-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/resolver.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/apidocs/resolver/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
	rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%doc KEYS LICENSE.resolver.txt
%{_javadir}/resolver*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
