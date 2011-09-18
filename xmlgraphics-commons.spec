Name:           xmlgraphics-commons
Version:        1.3.1
Release:        1.1%{?dist}
Epoch:          0
Summary:        XML Graphics Commons

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://xmlgraphics.apache.org/
Source0:        http://apache.skknet.net/xmlgraphics/commons/source/%{name}-%{version}-src.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  java-1.6.0-openjdk-devel >= 1:1.6.0.0-0.7
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit >= 0:1.6
BuildRequires:  junit
BuildRequires:  jakarta-commons-io >= 0:1.1
BuildRequires:  jakarta-commons-logging >= 0:1.0.4
Requires:	jakarta-commons-logging >= 0:1.0.4
Requires:       jakarta-commons-io >= 0:1.1

%description
Apache XML Graphics Commons is a library that consists of 
several reusable components used by Apache Batik and 
Apache FOP. Many of these components can easily be used 
separately outside the domains of SVG and XSL-FO. You will 
find components such as a PDF library, an RTF library, 
Graphics2D implementations that let you generate PDF & 
PostScript files, and much more.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation

%description    javadoc
%{summary}.


%prep
%setup -q %{name}-%{version}
rm -f `find . -name "*.jar"`


%build
export ANT_HOME=/usr/share/ant
export JAVA_HOME=/usr/lib/jvm/java-openjdk
export CLASSPATH=$CLASSPATH:/usr/share/java/commons-logging.jar
export OPT_JAR_LIST="ant/ant-junit junit"
pushd lib
ln -sf $(build-classpath commons-io) .
popd
ant package javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 0644 build/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE README
%{_javadir}/*.jar

%files javadoc
%defattr(-,root,root,-)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Sat Jan 9 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.3.1-1.1
- Update to 1.3.1.
- Fix Source0 url.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr 02 2008 Lillian Angel <langel at redhat.com> - 0:1.3-1
- Added java-1.6.0-openjdk-devel as build requirement.

* Mon Mar 31 2008 Lillian Angel <langel at redhat.com> - 0:1.3-1
- Updated sources to 1.3.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Added epoch.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Added missing BuildRoot line.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Fixed install section.

* Fri Nov 23 2007 Lillian Angel <langel at redhat.com> - 0:1.2-1
- Fixed rpmlint errors.

* Tue Sep 18 2007 Joshua Sumali <jsumali at redhat.com> - 0:1.2-1jpp
- Update to 1.2

* Tue May 23 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.0-1jpp
- First JPP-1.7 release
