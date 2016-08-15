Name:           ros-indigo-swri-roscpp
Version:        0.0.12
Release:        0%{?dist}
Summary:        ROS swri_roscpp package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs

%description
swri_roscpp

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Aug 14 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.12-0
- Autogenerated by Bloom

* Fri May 13 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.11-0
- Autogenerated by Bloom

* Thu May 12 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.10-3
- Autogenerated by Bloom

* Thu May 12 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.10-2
- Autogenerated by Bloom

* Thu May 12 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.10-1
- Autogenerated by Bloom

* Thu May 12 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.10-0
- Autogenerated by Bloom

