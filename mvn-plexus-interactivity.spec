#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plexus-interactivity
Version  : 1.0.alpha.4
Release  : 2
URL      : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4/plexus-interactivity-api-1.0-alpha-4.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4/plexus-interactivity-api-1.0-alpha-4.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4/plexus-interactivity-api-1.0-alpha-4.pom
Source2  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-6/plexus-interactivity-api-1.0-alpha-6.jar
Source3  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-6/plexus-interactivity-api-1.0-alpha-6.pom
Source4  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-interactivity/1.0-alpha-6/plexus-interactivity-1.0-alpha-6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: mvn-plexus-interactivity-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-plexus-interactivity package.
Group: Data

%description data
data components for the mvn-plexus-interactivity package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-6
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-6
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-6

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity/1.0-alpha-6
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity/1.0-alpha-6


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4/plexus-interactivity-api-1.0-alpha-4.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4/plexus-interactivity-api-1.0-alpha-4.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-6/plexus-interactivity-api-1.0-alpha-6.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-6/plexus-interactivity-api-1.0-alpha-6.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-interactivity/1.0-alpha-6/plexus-interactivity-1.0-alpha-6.pom
