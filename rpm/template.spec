Name:           ros-indigo-swri-dbw-interface
Version:        2.4.0
Release:        0%{?dist}
Summary:        ROS swri_dbw_interface package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_common
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin

%description
This package provides documentation on common interface conventions for drive-
by-wire systems.

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
* Tue Oct 09 2018 Marc Alban <malban@swri.org> - 2.4.0-0
- Autogenerated by Bloom

* Fri May 25 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.3.0-0
- Autogenerated by Bloom

* Fri May 11 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.2.1-0
- Autogenerated by Bloom

* Mon Feb 12 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.2.0-0
- Autogenerated by Bloom

* Fri Jan 26 2018 Elliot Johnson <elliot.johnson@swri.org> - 2.1.0-0
- Autogenerated by Bloom

