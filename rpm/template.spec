Name:           ros-kinetic-swri-route-util
Version:        0.2.2
Release:        0%{?dist}
Summary:        ROS swri_route_util package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-marti-nav-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-swri-transform-util
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-marti-nav-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-swri-transform-util

%description
This library provides functionality to simplify working with the navigation
messages defined in marti_nav_msgs.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Dec 07 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.2.2-0
- Autogenerated by Bloom

* Sun Oct 23 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.2.1-0
- Autogenerated by Bloom

* Tue Jun 21 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.2.0-1
- Autogenerated by Bloom

* Tue Jun 21 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.2.0-0
- Autogenerated by Bloom

