%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-swri-route-util
Version:        3.5.1
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS swri_route_util package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       ros-humble-marti-common-msgs
Requires:       ros-humble-marti-nav-msgs
Requires:       ros-humble-rclcpp
Requires:       ros-humble-swri-geometry-util
Requires:       ros-humble-swri-math-util
Requires:       ros-humble-swri-roscpp
Requires:       ros-humble-swri-transform-util
Requires:       ros-humble-tf2-geometry-msgs
Requires:       ros-humble-visualization-msgs
Requires:       ros-humble-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-marti-common-msgs
BuildRequires:  ros-humble-marti-nav-msgs
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-swri-geometry-util
BuildRequires:  ros-humble-swri-math-util
BuildRequires:  ros-humble-swri-roscpp
BuildRequires:  ros-humble-swri-transform-util
BuildRequires:  ros-humble-tf2-geometry-msgs
BuildRequires:  ros-humble-visualization-msgs
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This library provides functionality to simplify working with the navigation
messages defined in marti_nav_msgs.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Wed Jan 18 2023 P. J. Reed <preed@swri.org> - 3.5.1-2
- Autogenerated by Bloom

* Tue Nov 29 2022 P. J. Reed <preed@swri.org> - 3.5.1-1
- Autogenerated by Bloom

* Thu Nov 03 2022 P. J. Reed <preed@swri.org> - 3.5.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 P. J. Reed <preed@swri.org> - 3.4.0-3
- Autogenerated by Bloom

* Tue Feb 08 2022 P. J. Reed <preed@swri.org> - 3.4.0-2
- Autogenerated by Bloom

