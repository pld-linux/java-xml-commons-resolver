Summary:        xml-commons-resolver
Name:           xml-commons-resolver
Version:        1.0
Release:       	0.1
License:        Apache Software License
Group:		Development/Languages/Java
Source0:        http://xml.apache.org/dist/commons/%{name}-1.0.tar.gz
# Source0-md5:	4f54cf02d211abd95513699d088ae968
URL:            http://xml.apache.org/commons/
BuildRequires:  jakarta-ant
BuildArch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
xml-commons-resolver

%prep
%setup -q
rm -rf `find . -name "*.jar"`
mv resolver.xml build.xml

%build
ant jar docs

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_javalibdir}

cp build/resolver.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf resolver.jar $RPM_BUILD_ROOT/%{_javalibdir}/resolver-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KEYS README.* build/docs/javadocs
%{_javalibdir}/*.jar
