Name:           ros-hydro-rqt-bhand
Version:        0.1.0
Release:        0%{?dist}
Summary:        ROS rqt_bhand package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_bhand
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-hydro-bhand-controller
Requires:       ros-hydro-rostopic
Requires:       ros-hydro-rqt-gui
Requires:       ros-hydro-rqt-gui-py
BuildRequires:  ros-hydro-catkin

%description
The rqt_bhand package is intended to test the Barrett Hand in graphical mode

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Sep 02 2014 Román Navarro <rnavarro@robotnik.es> - 0.1.0-0
- Autogenerated by Bloom

