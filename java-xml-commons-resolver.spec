%include	/usr/lib/rpm/macros.java
#
%define	srcname	xml-commons-resolver
Summary:	Apache XML Commons Resolver classes
Summary(pl.UTF-8):	Klasy Apache XML Commons Resolver
Name:		java-xml-commons-resolver
Version:	1.2
Release:	3
License:	Apache v1.1
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/xml/commons/%{srcname}-%{version}.tar.gz
# Source0-md5:	46d52acdb67ba60f0156043f30108766
URL:		http://xml.apache.org/commons/
BuildRequires:	ant
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Provides:	xml-commons-resolver
Obsoletes:	xml-commons-resolver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache XML Commons Resolver classes implement Catalog-based entity
and URI resolution.

%description -l pl.UTF-8
Klasy Apache XML Commons Resolver są implementacją rozwiązywania encji
i URI na podstawie katalogu.

%package javadoc
Summary:	javadoc documentation for Apache XML Commons Resolver
Summary(pl.UTF-8):	Dokumentacja javadoc dla pakietu Apache XML Commons Resolver
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	xml-commons-resolver-javadoc

%description javadoc
javadoc documentation for Apache XML Commons Resolver.

%description javadoc -l pl.UTF-8
Dokumentacja javadoc dla pakietu Apache XML Commons Resolver.

%prep
%setup -q -n %{srcname}-%{version}

find -name "*.jar" | xargs rm -v
mv resolver.xml build.xml

%build
%ant jar javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/resolver.jar $RPM_BUILD_ROOT%{_javadir}/resolver-%{version}.jar
ln -sf resolver-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/resolver.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a build/apidocs/resolver/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc KEYS LICENSE.resolver.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
