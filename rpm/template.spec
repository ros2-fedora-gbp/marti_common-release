Name:           ros-indigo-swri-transform-util
Version:        0.0.12
Release:        0%{?dist}
Summary:        ROS swri_transform_util package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       geos-devel
Requires:       opencv-devel
Requires:       proj-devel
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-geographic-msgs
Requires:       ros-indigo-gps-common
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-swri-math-util
Requires:       ros-indigo-swri-yaml-util
Requires:       ros-indigo-tf
Requires:       ros-indigo-topic-tools
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  geos-devel
BuildRequires:  opencv-devel
BuildRequires:  proj-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-geographic-msgs
BuildRequires:  ros-indigo-gps-common
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-swri-math-util
BuildRequires:  ros-indigo-swri-yaml-util
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-topic-tools
BuildRequires:  yaml-cpp-devel

%description
The swri_transform_util package contains utility functions and classes for
transforming between coordinate frames.

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
* Sun Aug 14 2016 Marc Alban <malban@swri.org> - 0.0.12-0
- Autogenerated by Bloom

* Fri May 13 2016 Marc Alban <malban@swri.org> - 0.0.11-0
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-3
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-2
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-1
- Autogenerated by Bloom

* Thu May 12 2016 Marc Alban <malban@swri.org> - 0.0.10-0
- Autogenerated by Bloom

