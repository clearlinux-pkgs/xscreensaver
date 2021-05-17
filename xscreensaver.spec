#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xscreensaver
Version  : 6.00
Release  : 30
URL      : https://www.jwz.org/xscreensaver/xscreensaver-6.00.tar.gz
Source0  : https://www.jwz.org/xscreensaver/xscreensaver-6.00.tar.gz
Summary  : A minimal installation of xscreensaver.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: xscreensaver-bin = %{version}-%{release}
Requires: xscreensaver-data = %{version}-%{release}
Requires: xscreensaver-libexec = %{version}-%{release}
Requires: xscreensaver-locales = %{version}-%{release}
Requires: xscreensaver-man = %{version}-%{release}
Requires: xorg-fonts
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bc
BuildRequires : gdk-pixbuf-dev
BuildRequires : gdk-pixbuf-xlib-dev
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : glibc-staticdev
BuildRequires : glu-dev
BuildRequires : gtk+-dev
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : krb5-dev
BuildRequires : libXext-dev
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : lightdm
BuildRequires : m4
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xpm)
BuildRequires : pkgconfig(xrandr)
BuildRequires : xorg-fonts
Patch1: 0001-Do-not-warn-about-invalid-PAM-directories.patch
Patch2: build.patch

%description
A modular screen saver and locker for the X Window System.
More than 200 display modes are included in this package.

%package bin
Summary: bin components for the xscreensaver package.
Group: Binaries
Requires: xscreensaver-data = %{version}-%{release}
Requires: xscreensaver-libexec = %{version}-%{release}

%description bin
bin components for the xscreensaver package.


%package data
Summary: data components for the xscreensaver package.
Group: Data

%description data
data components for the xscreensaver package.


%package extras
Summary: extras components for the xscreensaver package.
Group: Default

%description extras
extras components for the xscreensaver package.


%package libexec
Summary: libexec components for the xscreensaver package.
Group: Default

%description libexec
libexec components for the xscreensaver package.


%package locales
Summary: locales components for the xscreensaver package.
Group: Default

%description locales
locales components for the xscreensaver package.


%package man
Summary: man components for the xscreensaver package.
Group: Default

%description man
man components for the xscreensaver package.


%prep
%setup -q -n xscreensaver-6.00
cd %{_builddir}/xscreensaver-6.00
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621290201
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%reconfigure --disable-static --with-xpm --with-pam --with-dpms-ext
make  %{?_smp_mflags}  all

%install
export SOURCE_DATE_EPOCH=1621290201
rm -rf %{buildroot}
%make_install
%find_lang xscreensaver
## install_append content
# Makefile.in is just too ancient to reconf, checks for /etc/pam.d existence
install -m 00644 -D driver/xscreensaver.pam $RPM_BUILD_ROOT/usr/share/pam.d/xscreensaver
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/X11/app-defaults/XScreenSaver

%files bin
%defattr(-,root,root,-)
/usr/bin/xscreensaver
/usr/bin/xscreensaver-command
/usr/bin/xscreensaver-demo
/usr/bin/xscreensaver-settings

%files data
%defattr(-,root,root,-)
/usr/share/applications/xscreensaver-properties.desktop
/usr/share/fonts/xscreensaver/OCRAStd.otf
/usr/share/fonts/xscreensaver/SpecialElite.ttf
/usr/share/fonts/xscreensaver/clacon.ttf
/usr/share/fonts/xscreensaver/gallant12x22.ttf
/usr/share/fonts/xscreensaver/luximr.ttf
/usr/share/pam.d/xscreensaver
/usr/share/pixmaps/xscreensaver.xpm
/usr/share/xscreensaver/config/README
/usr/share/xscreensaver/config/scooter.xml
/usr/share/xscreensaver/config/sphereeversion.xml
/usr/share/xscreensaver/ui/screensaver-cmndln.png
/usr/share/xscreensaver/ui/screensaver-colorselector.png
/usr/share/xscreensaver/ui/screensaver-diagnostic.png
/usr/share/xscreensaver/ui/screensaver-locking.png
/usr/share/xscreensaver/ui/screensaver-power.png
/usr/share/xscreensaver/ui/screensaver-snap.png
/usr/share/xscreensaver/ui/xscreensaver.ui

%files extras
%defattr(-,root,root,-)
/usr/libexec/xscreensaver/abstractile
/usr/libexec/xscreensaver/anemone
/usr/libexec/xscreensaver/anemotaxis
/usr/libexec/xscreensaver/antinspect
/usr/libexec/xscreensaver/antmaze
/usr/libexec/xscreensaver/antspotlight
/usr/libexec/xscreensaver/apollonian
/usr/libexec/xscreensaver/apple2
/usr/libexec/xscreensaver/atlantis
/usr/libexec/xscreensaver/attraction
/usr/libexec/xscreensaver/atunnel
/usr/libexec/xscreensaver/barcode
/usr/libexec/xscreensaver/beats
/usr/libexec/xscreensaver/binaryring
/usr/libexec/xscreensaver/blaster
/usr/libexec/xscreensaver/blinkbox
/usr/libexec/xscreensaver/blitspin
/usr/libexec/xscreensaver/blocktube
/usr/libexec/xscreensaver/boing
/usr/libexec/xscreensaver/bouboule
/usr/libexec/xscreensaver/bouncingcow
/usr/libexec/xscreensaver/boxed
/usr/libexec/xscreensaver/boxfit
/usr/libexec/xscreensaver/braid
/usr/libexec/xscreensaver/bsod
/usr/libexec/xscreensaver/bubble3d
/usr/libexec/xscreensaver/bumps
/usr/libexec/xscreensaver/cage
/usr/libexec/xscreensaver/carousel
/usr/libexec/xscreensaver/ccurve
/usr/libexec/xscreensaver/celtic
/usr/libexec/xscreensaver/circuit
/usr/libexec/xscreensaver/cityflow
/usr/libexec/xscreensaver/cloudlife
/usr/libexec/xscreensaver/companioncube
/usr/libexec/xscreensaver/compass
/usr/libexec/xscreensaver/coral
/usr/libexec/xscreensaver/covid19
/usr/libexec/xscreensaver/crackberg
/usr/libexec/xscreensaver/crumbler
/usr/libexec/xscreensaver/crystal
/usr/libexec/xscreensaver/cube21
/usr/libexec/xscreensaver/cubenetic
/usr/libexec/xscreensaver/cubestack
/usr/libexec/xscreensaver/cubestorm
/usr/libexec/xscreensaver/cubetwist
/usr/libexec/xscreensaver/cubicgrid
/usr/libexec/xscreensaver/cwaves
/usr/libexec/xscreensaver/cynosure
/usr/libexec/xscreensaver/dangerball
/usr/libexec/xscreensaver/decayscreen
/usr/libexec/xscreensaver/deco
/usr/libexec/xscreensaver/deepstars
/usr/libexec/xscreensaver/deluxe
/usr/libexec/xscreensaver/demon
/usr/libexec/xscreensaver/discoball
/usr/libexec/xscreensaver/discrete
/usr/libexec/xscreensaver/distort
/usr/libexec/xscreensaver/drift
/usr/libexec/xscreensaver/dymaxionmap
/usr/libexec/xscreensaver/endgame
/usr/libexec/xscreensaver/energystream
/usr/libexec/xscreensaver/engine
/usr/libexec/xscreensaver/epicycle
/usr/libexec/xscreensaver/eruption
/usr/libexec/xscreensaver/esper
/usr/libexec/xscreensaver/etruscanvenus
/usr/libexec/xscreensaver/euler2d
/usr/libexec/xscreensaver/fadeplot
/usr/libexec/xscreensaver/fiberlamp
/usr/libexec/xscreensaver/filmleader
/usr/libexec/xscreensaver/fireworkx
/usr/libexec/xscreensaver/flame
/usr/libexec/xscreensaver/flipflop
/usr/libexec/xscreensaver/flipscreen3d
/usr/libexec/xscreensaver/fliptext
/usr/libexec/xscreensaver/flow
/usr/libexec/xscreensaver/fluidballs
/usr/libexec/xscreensaver/flurry
/usr/libexec/xscreensaver/flyingtoasters
/usr/libexec/xscreensaver/fontglide
/usr/libexec/xscreensaver/fuzzyflakes
/usr/libexec/xscreensaver/galaxy
/usr/libexec/xscreensaver/gears
/usr/libexec/xscreensaver/geodesic
/usr/libexec/xscreensaver/geodesicgears
/usr/libexec/xscreensaver/gflux
/usr/libexec/xscreensaver/gibson
/usr/libexec/xscreensaver/glblur
/usr/libexec/xscreensaver/glcells
/usr/libexec/xscreensaver/gleidescope
/usr/libexec/xscreensaver/glhanoi
/usr/libexec/xscreensaver/glitchpeg
/usr/libexec/xscreensaver/glknots
/usr/libexec/xscreensaver/glmatrix
/usr/libexec/xscreensaver/glplanet
/usr/libexec/xscreensaver/glschool
/usr/libexec/xscreensaver/glslideshow
/usr/libexec/xscreensaver/glsnake
/usr/libexec/xscreensaver/gltext
/usr/libexec/xscreensaver/goop
/usr/libexec/xscreensaver/grav
/usr/libexec/xscreensaver/gravitywell
/usr/libexec/xscreensaver/greynetic
/usr/libexec/xscreensaver/halftone
/usr/libexec/xscreensaver/halo
/usr/libexec/xscreensaver/handsy
/usr/libexec/xscreensaver/headroom
/usr/libexec/xscreensaver/helix
/usr/libexec/xscreensaver/hexadrop
/usr/libexec/xscreensaver/hexstrut
/usr/libexec/xscreensaver/hilbert
/usr/libexec/xscreensaver/hopalong
/usr/libexec/xscreensaver/hydrostat
/usr/libexec/xscreensaver/hypertorus
/usr/libexec/xscreensaver/hypnowheel
/usr/libexec/xscreensaver/ifs
/usr/libexec/xscreensaver/imsmap
/usr/libexec/xscreensaver/interaggregate
/usr/libexec/xscreensaver/interference
/usr/libexec/xscreensaver/intermomentary
/usr/libexec/xscreensaver/jigglypuff
/usr/libexec/xscreensaver/jigsaw
/usr/libexec/xscreensaver/juggler3d
/usr/libexec/xscreensaver/julia
/usr/libexec/xscreensaver/kaleidescope
/usr/libexec/xscreensaver/kaleidocycle
/usr/libexec/xscreensaver/klein
/usr/libexec/xscreensaver/kumppa
/usr/libexec/xscreensaver/lament
/usr/libexec/xscreensaver/lavalite
/usr/libexec/xscreensaver/lcdscrub
/usr/libexec/xscreensaver/lockward
/usr/libexec/xscreensaver/loop
/usr/libexec/xscreensaver/m6502
/usr/libexec/xscreensaver/maze
/usr/libexec/xscreensaver/maze3d
/usr/libexec/xscreensaver/memscroller
/usr/libexec/xscreensaver/menger
/usr/libexec/xscreensaver/metaballs
/usr/libexec/xscreensaver/mirrorblob
/usr/libexec/xscreensaver/moebius
/usr/libexec/xscreensaver/moebiusgears
/usr/libexec/xscreensaver/moire
/usr/libexec/xscreensaver/moire2
/usr/libexec/xscreensaver/molecule
/usr/libexec/xscreensaver/morph3d
/usr/libexec/xscreensaver/mountain
/usr/libexec/xscreensaver/munch
/usr/libexec/xscreensaver/nerverot
/usr/libexec/xscreensaver/noof
/usr/libexec/xscreensaver/noseguy
/usr/libexec/xscreensaver/pacman
/usr/libexec/xscreensaver/pedal
/usr/libexec/xscreensaver/peepers
/usr/libexec/xscreensaver/penetrate
/usr/libexec/xscreensaver/penrose
/usr/libexec/xscreensaver/petri
/usr/libexec/xscreensaver/phosphor
/usr/libexec/xscreensaver/photopile
/usr/libexec/xscreensaver/piecewise
/usr/libexec/xscreensaver/pinion
/usr/libexec/xscreensaver/pipes
/usr/libexec/xscreensaver/polyhedra
/usr/libexec/xscreensaver/polyominoes
/usr/libexec/xscreensaver/polytopes
/usr/libexec/xscreensaver/pong
/usr/libexec/xscreensaver/popsquares
/usr/libexec/xscreensaver/projectiveplane
/usr/libexec/xscreensaver/providence
/usr/libexec/xscreensaver/pulsar
/usr/libexec/xscreensaver/pyro
/usr/libexec/xscreensaver/qix
/usr/libexec/xscreensaver/quasicrystal
/usr/libexec/xscreensaver/queens
/usr/libexec/xscreensaver/raverhoop
/usr/libexec/xscreensaver/razzledazzle
/usr/libexec/xscreensaver/rd-bomb
/usr/libexec/xscreensaver/ripples
/usr/libexec/xscreensaver/rocks
/usr/libexec/xscreensaver/romanboy
/usr/libexec/xscreensaver/rorschach
/usr/libexec/xscreensaver/rotzoomer
/usr/libexec/xscreensaver/rubik
/usr/libexec/xscreensaver/rubikblocks
/usr/libexec/xscreensaver/sballs
/usr/libexec/xscreensaver/shadebobs
/usr/libexec/xscreensaver/sierpinski
/usr/libexec/xscreensaver/sierpinski3d
/usr/libexec/xscreensaver/skytentacles
/usr/libexec/xscreensaver/slidescreen
/usr/libexec/xscreensaver/slip
/usr/libexec/xscreensaver/sonar
/usr/libexec/xscreensaver/speedmine
/usr/libexec/xscreensaver/sphereeversion
/usr/libexec/xscreensaver/spheremonics
/usr/libexec/xscreensaver/splitflap
/usr/libexec/xscreensaver/splodesic
/usr/libexec/xscreensaver/spotlight
/usr/libexec/xscreensaver/sproingies
/usr/libexec/xscreensaver/squiral
/usr/libexec/xscreensaver/stairs
/usr/libexec/xscreensaver/starfish
/usr/libexec/xscreensaver/starwars
/usr/libexec/xscreensaver/stonerview
/usr/libexec/xscreensaver/strange
/usr/libexec/xscreensaver/substrate
/usr/libexec/xscreensaver/superquadrics
/usr/libexec/xscreensaver/surfaces
/usr/libexec/xscreensaver/swirl
/usr/libexec/xscreensaver/tangram
/usr/libexec/xscreensaver/tessellimage
/usr/libexec/xscreensaver/thornbird
/usr/libexec/xscreensaver/timetunnel
/usr/libexec/xscreensaver/topblock
/usr/libexec/xscreensaver/triangle
/usr/libexec/xscreensaver/tronbit
/usr/libexec/xscreensaver/truchet
/usr/libexec/xscreensaver/twang
/usr/libexec/xscreensaver/unicrud
/usr/libexec/xscreensaver/unknownpleasures
/usr/libexec/xscreensaver/vermiculate
/usr/libexec/xscreensaver/vfeedback
/usr/libexec/xscreensaver/vidwhacker
/usr/libexec/xscreensaver/vigilance
/usr/libexec/xscreensaver/voronoi
/usr/libexec/xscreensaver/wander
/usr/libexec/xscreensaver/webcollage
/usr/libexec/xscreensaver/whirlwindwarp
/usr/libexec/xscreensaver/winduprobot
/usr/libexec/xscreensaver/wormhole
/usr/libexec/xscreensaver/xanalogtv
/usr/libexec/xscreensaver/xflame
/usr/libexec/xscreensaver/xjack
/usr/libexec/xscreensaver/xlyap
/usr/libexec/xscreensaver/xmatrix
/usr/libexec/xscreensaver/xrayswarm
/usr/libexec/xscreensaver/xspirograph
/usr/libexec/xscreensaver/zoom
/usr/share/xscreensaver/config/abstractile.xml
/usr/share/xscreensaver/config/anemone.xml
/usr/share/xscreensaver/config/anemotaxis.xml
/usr/share/xscreensaver/config/antinspect.xml
/usr/share/xscreensaver/config/antmaze.xml
/usr/share/xscreensaver/config/antspotlight.xml
/usr/share/xscreensaver/config/apollonian.xml
/usr/share/xscreensaver/config/apple2.xml
/usr/share/xscreensaver/config/atlantis.xml
/usr/share/xscreensaver/config/attraction.xml
/usr/share/xscreensaver/config/atunnel.xml
/usr/share/xscreensaver/config/barcode.xml
/usr/share/xscreensaver/config/beats.xml
/usr/share/xscreensaver/config/binaryring.xml
/usr/share/xscreensaver/config/blaster.xml
/usr/share/xscreensaver/config/blinkbox.xml
/usr/share/xscreensaver/config/blitspin.xml
/usr/share/xscreensaver/config/blocktube.xml
/usr/share/xscreensaver/config/boing.xml
/usr/share/xscreensaver/config/bouboule.xml
/usr/share/xscreensaver/config/bouncingcow.xml
/usr/share/xscreensaver/config/boxed.xml
/usr/share/xscreensaver/config/boxfit.xml
/usr/share/xscreensaver/config/braid.xml
/usr/share/xscreensaver/config/bsod.xml
/usr/share/xscreensaver/config/bubble3d.xml
/usr/share/xscreensaver/config/bumps.xml
/usr/share/xscreensaver/config/cage.xml
/usr/share/xscreensaver/config/carousel.xml
/usr/share/xscreensaver/config/ccurve.xml
/usr/share/xscreensaver/config/celtic.xml
/usr/share/xscreensaver/config/circuit.xml
/usr/share/xscreensaver/config/cityflow.xml
/usr/share/xscreensaver/config/cloudlife.xml
/usr/share/xscreensaver/config/companioncube.xml
/usr/share/xscreensaver/config/compass.xml
/usr/share/xscreensaver/config/coral.xml
/usr/share/xscreensaver/config/covid19.xml
/usr/share/xscreensaver/config/crackberg.xml
/usr/share/xscreensaver/config/crumbler.xml
/usr/share/xscreensaver/config/crystal.xml
/usr/share/xscreensaver/config/cube21.xml
/usr/share/xscreensaver/config/cubenetic.xml
/usr/share/xscreensaver/config/cubestack.xml
/usr/share/xscreensaver/config/cubestorm.xml
/usr/share/xscreensaver/config/cubetwist.xml
/usr/share/xscreensaver/config/cubicgrid.xml
/usr/share/xscreensaver/config/cwaves.xml
/usr/share/xscreensaver/config/cynosure.xml
/usr/share/xscreensaver/config/dangerball.xml
/usr/share/xscreensaver/config/decayscreen.xml
/usr/share/xscreensaver/config/deco.xml
/usr/share/xscreensaver/config/deepstars.xml
/usr/share/xscreensaver/config/deluxe.xml
/usr/share/xscreensaver/config/demon.xml
/usr/share/xscreensaver/config/discoball.xml
/usr/share/xscreensaver/config/discrete.xml
/usr/share/xscreensaver/config/distort.xml
/usr/share/xscreensaver/config/drift.xml
/usr/share/xscreensaver/config/dymaxionmap.xml
/usr/share/xscreensaver/config/endgame.xml
/usr/share/xscreensaver/config/energystream.xml
/usr/share/xscreensaver/config/engine.xml
/usr/share/xscreensaver/config/epicycle.xml
/usr/share/xscreensaver/config/eruption.xml
/usr/share/xscreensaver/config/esper.xml
/usr/share/xscreensaver/config/etruscanvenus.xml
/usr/share/xscreensaver/config/euler2d.xml
/usr/share/xscreensaver/config/fadeplot.xml
/usr/share/xscreensaver/config/fiberlamp.xml
/usr/share/xscreensaver/config/filmleader.xml
/usr/share/xscreensaver/config/fireworkx.xml
/usr/share/xscreensaver/config/flame.xml
/usr/share/xscreensaver/config/flipflop.xml
/usr/share/xscreensaver/config/flipscreen3d.xml
/usr/share/xscreensaver/config/fliptext.xml
/usr/share/xscreensaver/config/flow.xml
/usr/share/xscreensaver/config/fluidballs.xml
/usr/share/xscreensaver/config/flurry.xml
/usr/share/xscreensaver/config/flyingtoasters.xml
/usr/share/xscreensaver/config/fontglide.xml
/usr/share/xscreensaver/config/fuzzyflakes.xml
/usr/share/xscreensaver/config/galaxy.xml
/usr/share/xscreensaver/config/gears.xml
/usr/share/xscreensaver/config/geodesic.xml
/usr/share/xscreensaver/config/geodesicgears.xml
/usr/share/xscreensaver/config/gflux.xml
/usr/share/xscreensaver/config/gibson.xml
/usr/share/xscreensaver/config/glblur.xml
/usr/share/xscreensaver/config/glcells.xml
/usr/share/xscreensaver/config/gleidescope.xml
/usr/share/xscreensaver/config/glhanoi.xml
/usr/share/xscreensaver/config/glitchpeg.xml
/usr/share/xscreensaver/config/glknots.xml
/usr/share/xscreensaver/config/glmatrix.xml
/usr/share/xscreensaver/config/glplanet.xml
/usr/share/xscreensaver/config/glschool.xml
/usr/share/xscreensaver/config/glslideshow.xml
/usr/share/xscreensaver/config/glsnake.xml
/usr/share/xscreensaver/config/gltext.xml
/usr/share/xscreensaver/config/goop.xml
/usr/share/xscreensaver/config/grav.xml
/usr/share/xscreensaver/config/gravitywell.xml
/usr/share/xscreensaver/config/greynetic.xml
/usr/share/xscreensaver/config/halftone.xml
/usr/share/xscreensaver/config/halo.xml
/usr/share/xscreensaver/config/handsy.xml
/usr/share/xscreensaver/config/headroom.xml
/usr/share/xscreensaver/config/helix.xml
/usr/share/xscreensaver/config/hexadrop.xml
/usr/share/xscreensaver/config/hexstrut.xml
/usr/share/xscreensaver/config/hilbert.xml
/usr/share/xscreensaver/config/hopalong.xml
/usr/share/xscreensaver/config/hydrostat.xml
/usr/share/xscreensaver/config/hypertorus.xml
/usr/share/xscreensaver/config/hypnowheel.xml
/usr/share/xscreensaver/config/ifs.xml
/usr/share/xscreensaver/config/imsmap.xml
/usr/share/xscreensaver/config/interaggregate.xml
/usr/share/xscreensaver/config/interference.xml
/usr/share/xscreensaver/config/intermomentary.xml
/usr/share/xscreensaver/config/jigglypuff.xml
/usr/share/xscreensaver/config/jigsaw.xml
/usr/share/xscreensaver/config/juggler3d.xml
/usr/share/xscreensaver/config/julia.xml
/usr/share/xscreensaver/config/kaleidescope.xml
/usr/share/xscreensaver/config/kaleidocycle.xml
/usr/share/xscreensaver/config/klein.xml
/usr/share/xscreensaver/config/kumppa.xml
/usr/share/xscreensaver/config/lament.xml
/usr/share/xscreensaver/config/lavalite.xml
/usr/share/xscreensaver/config/lcdscrub.xml
/usr/share/xscreensaver/config/lockward.xml
/usr/share/xscreensaver/config/loop.xml
/usr/share/xscreensaver/config/m6502.xml
/usr/share/xscreensaver/config/maze.xml
/usr/share/xscreensaver/config/maze3d.xml
/usr/share/xscreensaver/config/memscroller.xml
/usr/share/xscreensaver/config/menger.xml
/usr/share/xscreensaver/config/metaballs.xml
/usr/share/xscreensaver/config/mirrorblob.xml
/usr/share/xscreensaver/config/moebius.xml
/usr/share/xscreensaver/config/moebiusgears.xml
/usr/share/xscreensaver/config/moire.xml
/usr/share/xscreensaver/config/moire2.xml
/usr/share/xscreensaver/config/molecule.xml
/usr/share/xscreensaver/config/morph3d.xml
/usr/share/xscreensaver/config/mountain.xml
/usr/share/xscreensaver/config/munch.xml
/usr/share/xscreensaver/config/nerverot.xml
/usr/share/xscreensaver/config/noof.xml
/usr/share/xscreensaver/config/noseguy.xml
/usr/share/xscreensaver/config/pacman.xml
/usr/share/xscreensaver/config/pedal.xml
/usr/share/xscreensaver/config/peepers.xml
/usr/share/xscreensaver/config/penetrate.xml
/usr/share/xscreensaver/config/penrose.xml
/usr/share/xscreensaver/config/petri.xml
/usr/share/xscreensaver/config/phosphor.xml
/usr/share/xscreensaver/config/photopile.xml
/usr/share/xscreensaver/config/piecewise.xml
/usr/share/xscreensaver/config/pinion.xml
/usr/share/xscreensaver/config/pipes.xml
/usr/share/xscreensaver/config/polyhedra.xml
/usr/share/xscreensaver/config/polyominoes.xml
/usr/share/xscreensaver/config/polytopes.xml
/usr/share/xscreensaver/config/pong.xml
/usr/share/xscreensaver/config/popsquares.xml
/usr/share/xscreensaver/config/projectiveplane.xml
/usr/share/xscreensaver/config/providence.xml
/usr/share/xscreensaver/config/pulsar.xml
/usr/share/xscreensaver/config/pyro.xml
/usr/share/xscreensaver/config/qix.xml
/usr/share/xscreensaver/config/quasicrystal.xml
/usr/share/xscreensaver/config/queens.xml
/usr/share/xscreensaver/config/raverhoop.xml
/usr/share/xscreensaver/config/razzledazzle.xml
/usr/share/xscreensaver/config/rd-bomb.xml
/usr/share/xscreensaver/config/ripples.xml
/usr/share/xscreensaver/config/rocks.xml
/usr/share/xscreensaver/config/romanboy.xml
/usr/share/xscreensaver/config/rorschach.xml
/usr/share/xscreensaver/config/rotzoomer.xml
/usr/share/xscreensaver/config/rubik.xml
/usr/share/xscreensaver/config/rubikblocks.xml
/usr/share/xscreensaver/config/sballs.xml
/usr/share/xscreensaver/config/shadebobs.xml
/usr/share/xscreensaver/config/sierpinski.xml
/usr/share/xscreensaver/config/sierpinski3d.xml
/usr/share/xscreensaver/config/skytentacles.xml
/usr/share/xscreensaver/config/slidescreen.xml
/usr/share/xscreensaver/config/slip.xml
/usr/share/xscreensaver/config/sonar.xml
/usr/share/xscreensaver/config/speedmine.xml
/usr/share/xscreensaver/config/spheremonics.xml
/usr/share/xscreensaver/config/splitflap.xml
/usr/share/xscreensaver/config/splodesic.xml
/usr/share/xscreensaver/config/spotlight.xml
/usr/share/xscreensaver/config/sproingies.xml
/usr/share/xscreensaver/config/squiral.xml
/usr/share/xscreensaver/config/stairs.xml
/usr/share/xscreensaver/config/starfish.xml
/usr/share/xscreensaver/config/starwars.xml
/usr/share/xscreensaver/config/stonerview.xml
/usr/share/xscreensaver/config/strange.xml
/usr/share/xscreensaver/config/substrate.xml
/usr/share/xscreensaver/config/superquadrics.xml
/usr/share/xscreensaver/config/surfaces.xml
/usr/share/xscreensaver/config/swirl.xml
/usr/share/xscreensaver/config/tangram.xml
/usr/share/xscreensaver/config/tessellimage.xml
/usr/share/xscreensaver/config/thornbird.xml
/usr/share/xscreensaver/config/timetunnel.xml
/usr/share/xscreensaver/config/topblock.xml
/usr/share/xscreensaver/config/triangle.xml
/usr/share/xscreensaver/config/tronbit.xml
/usr/share/xscreensaver/config/truchet.xml
/usr/share/xscreensaver/config/twang.xml
/usr/share/xscreensaver/config/unicrud.xml
/usr/share/xscreensaver/config/unknownpleasures.xml
/usr/share/xscreensaver/config/vermiculate.xml
/usr/share/xscreensaver/config/vfeedback.xml
/usr/share/xscreensaver/config/vidwhacker.xml
/usr/share/xscreensaver/config/vigilance.xml
/usr/share/xscreensaver/config/voronoi.xml
/usr/share/xscreensaver/config/wander.xml
/usr/share/xscreensaver/config/webcollage.xml
/usr/share/xscreensaver/config/whirlwindwarp.xml
/usr/share/xscreensaver/config/winduprobot.xml
/usr/share/xscreensaver/config/wormhole.xml
/usr/share/xscreensaver/config/xanalogtv.xml
/usr/share/xscreensaver/config/xflame.xml
/usr/share/xscreensaver/config/xjack.xml
/usr/share/xscreensaver/config/xlyap.xml
/usr/share/xscreensaver/config/xmatrix.xml
/usr/share/xscreensaver/config/xrayswarm.xml
/usr/share/xscreensaver/config/xspirograph.xml
/usr/share/xscreensaver/config/zoom.xml

%files libexec
%defattr(-,root,root,-)
/usr/libexec/xscreensaver/scooter
/usr/libexec/xscreensaver/webcollage-helper
/usr/libexec/xscreensaver/xscreensaver-auth
/usr/libexec/xscreensaver/xscreensaver-getimage
/usr/libexec/xscreensaver/xscreensaver-getimage-file
/usr/libexec/xscreensaver/xscreensaver-getimage-video
/usr/libexec/xscreensaver/xscreensaver-gfx
/usr/libexec/xscreensaver/xscreensaver-gl-visual
/usr/libexec/xscreensaver/xscreensaver-systemd
/usr/libexec/xscreensaver/xscreensaver-text

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xscreensaver-command.1
/usr/share/man/man1/xscreensaver-demo.1
/usr/share/man/man1/xscreensaver-settings.1
/usr/share/man/man1/xscreensaver.1
/usr/share/man/man6/abstractile.6
/usr/share/man/man6/anemone.6
/usr/share/man/man6/anemotaxis.6
/usr/share/man/man6/antinspect.6
/usr/share/man/man6/antmaze.6
/usr/share/man/man6/antspotlight.6
/usr/share/man/man6/apollonian.6
/usr/share/man/man6/apple2.6
/usr/share/man/man6/atlantis.6
/usr/share/man/man6/attraction.6
/usr/share/man/man6/atunnel.6
/usr/share/man/man6/barcode.6
/usr/share/man/man6/beats.6
/usr/share/man/man6/binaryring.6
/usr/share/man/man6/blaster.6
/usr/share/man/man6/blinkbox.6
/usr/share/man/man6/blitspin.6
/usr/share/man/man6/blocktube.6
/usr/share/man/man6/boing.6
/usr/share/man/man6/bouboule.6
/usr/share/man/man6/bouncingcow.6
/usr/share/man/man6/boxed.6
/usr/share/man/man6/boxfit.6
/usr/share/man/man6/braid.6
/usr/share/man/man6/bsod.6
/usr/share/man/man6/bubble3d.6
/usr/share/man/man6/bumps.6
/usr/share/man/man6/cage.6
/usr/share/man/man6/carousel.6
/usr/share/man/man6/ccurve.6
/usr/share/man/man6/celtic.6
/usr/share/man/man6/circuit.6
/usr/share/man/man6/cityflow.6
/usr/share/man/man6/cloudlife.6
/usr/share/man/man6/companioncube.6
/usr/share/man/man6/compass.6
/usr/share/man/man6/coral.6
/usr/share/man/man6/covid19.6
/usr/share/man/man6/crackberg.6
/usr/share/man/man6/crumbler.6
/usr/share/man/man6/crystal.6
/usr/share/man/man6/cube21.6
/usr/share/man/man6/cubenetic.6
/usr/share/man/man6/cubestack.6
/usr/share/man/man6/cubestorm.6
/usr/share/man/man6/cubetwist.6
/usr/share/man/man6/cubicgrid.6
/usr/share/man/man6/cwaves.6
/usr/share/man/man6/cynosure.6
/usr/share/man/man6/dangerball.6
/usr/share/man/man6/decayscreen.6
/usr/share/man/man6/deco.6
/usr/share/man/man6/deepstars.6
/usr/share/man/man6/deluxe.6
/usr/share/man/man6/demon.6
/usr/share/man/man6/discoball.6
/usr/share/man/man6/discrete.6
/usr/share/man/man6/distort.6
/usr/share/man/man6/drift.6
/usr/share/man/man6/dymaxionmap.6
/usr/share/man/man6/endgame.6
/usr/share/man/man6/energystream.6
/usr/share/man/man6/engine.6
/usr/share/man/man6/epicycle.6
/usr/share/man/man6/eruption.6
/usr/share/man/man6/esper.6
/usr/share/man/man6/etruscanvenus.6
/usr/share/man/man6/euler2d.6
/usr/share/man/man6/extrusion.6
/usr/share/man/man6/fadeplot.6
/usr/share/man/man6/fiberlamp.6
/usr/share/man/man6/filmleader.6
/usr/share/man/man6/fireworkx.6
/usr/share/man/man6/flame.6
/usr/share/man/man6/flipflop.6
/usr/share/man/man6/flipscreen3d.6
/usr/share/man/man6/fliptext.6
/usr/share/man/man6/flow.6
/usr/share/man/man6/fluidballs.6
/usr/share/man/man6/flurry.6
/usr/share/man/man6/flyingtoasters.6
/usr/share/man/man6/fontglide.6
/usr/share/man/man6/fuzzyflakes.6
/usr/share/man/man6/galaxy.6
/usr/share/man/man6/gears.6
/usr/share/man/man6/geodesic.6
/usr/share/man/man6/geodesicgears.6
/usr/share/man/man6/gflux.6
/usr/share/man/man6/gibson.6
/usr/share/man/man6/glblur.6
/usr/share/man/man6/glcells.6
/usr/share/man/man6/gleidescope.6
/usr/share/man/man6/glhanoi.6
/usr/share/man/man6/glitchpeg.6
/usr/share/man/man6/glknots.6
/usr/share/man/man6/glmatrix.6
/usr/share/man/man6/glplanet.6
/usr/share/man/man6/glschool.6
/usr/share/man/man6/glslideshow.6
/usr/share/man/man6/glsnake.6
/usr/share/man/man6/gltext.6
/usr/share/man/man6/goop.6
/usr/share/man/man6/grav.6
/usr/share/man/man6/gravitywell.6
/usr/share/man/man6/greynetic.6
/usr/share/man/man6/halftone.6
/usr/share/man/man6/halo.6
/usr/share/man/man6/handsy.6
/usr/share/man/man6/headroom.6
/usr/share/man/man6/helix.6
/usr/share/man/man6/hexadrop.6
/usr/share/man/man6/hexstrut.6
/usr/share/man/man6/hilbert.6
/usr/share/man/man6/hopalong.6
/usr/share/man/man6/hydrostat.6
/usr/share/man/man6/hypertorus.6
/usr/share/man/man6/hypnowheel.6
/usr/share/man/man6/ifs.6
/usr/share/man/man6/imsmap.6
/usr/share/man/man6/interaggregate.6
/usr/share/man/man6/interference.6
/usr/share/man/man6/intermomentary.6
/usr/share/man/man6/jigglypuff.6
/usr/share/man/man6/jigsaw.6
/usr/share/man/man6/juggler3d.6
/usr/share/man/man6/julia.6
/usr/share/man/man6/kaleidescope.6
/usr/share/man/man6/kaleidocycle.6
/usr/share/man/man6/klein.6
/usr/share/man/man6/kumppa.6
/usr/share/man/man6/lament.6
/usr/share/man/man6/lavalite.6
/usr/share/man/man6/lcdscrub.6
/usr/share/man/man6/lockward.6
/usr/share/man/man6/loop.6
/usr/share/man/man6/maze.6
/usr/share/man/man6/maze3d.6
/usr/share/man/man6/memscroller.6
/usr/share/man/man6/menger.6
/usr/share/man/man6/metaballs.6
/usr/share/man/man6/mirrorblob.6
/usr/share/man/man6/moebius.6
/usr/share/man/man6/moebiusgears.6
/usr/share/man/man6/moire.6
/usr/share/man/man6/moire2.6
/usr/share/man/man6/molecule.6
/usr/share/man/man6/morph3d.6
/usr/share/man/man6/mountain.6
/usr/share/man/man6/munch.6
/usr/share/man/man6/nerverot.6
/usr/share/man/man6/noof.6
/usr/share/man/man6/noseguy.6
/usr/share/man/man6/pacman.6
/usr/share/man/man6/pedal.6
/usr/share/man/man6/peepers.6
/usr/share/man/man6/penetrate.6
/usr/share/man/man6/penrose.6
/usr/share/man/man6/petri.6
/usr/share/man/man6/phosphor.6
/usr/share/man/man6/photopile.6
/usr/share/man/man6/piecewise.6
/usr/share/man/man6/pinion.6
/usr/share/man/man6/pipes.6
/usr/share/man/man6/polyhedra.6
/usr/share/man/man6/polyominoes.6
/usr/share/man/man6/polytopes.6
/usr/share/man/man6/pong.6
/usr/share/man/man6/projectiveplane.6
/usr/share/man/man6/providence.6
/usr/share/man/man6/pulsar.6
/usr/share/man/man6/pyro.6
/usr/share/man/man6/qix.6
/usr/share/man/man6/quasicrystal.6
/usr/share/man/man6/queens.6
/usr/share/man/man6/raverhoop.6
/usr/share/man/man6/razzledazzle.6
/usr/share/man/man6/rd-bomb.6
/usr/share/man/man6/ripples.6
/usr/share/man/man6/rocks.6
/usr/share/man/man6/romanboy.6
/usr/share/man/man6/rorschach.6
/usr/share/man/man6/rotzoomer.6
/usr/share/man/man6/rubik.6
/usr/share/man/man6/rubikblocks.6
/usr/share/man/man6/sballs.6
/usr/share/man/man6/scooter.6
/usr/share/man/man6/shadebobs.6
/usr/share/man/man6/sierpinski.6
/usr/share/man/man6/sierpinski3d.6
/usr/share/man/man6/skytentacles.6
/usr/share/man/man6/slidescreen.6
/usr/share/man/man6/slip.6
/usr/share/man/man6/sonar.6
/usr/share/man/man6/speedmine.6
/usr/share/man/man6/sphereeversion.6
/usr/share/man/man6/spheremonics.6
/usr/share/man/man6/splitflap.6
/usr/share/man/man6/splodesic.6
/usr/share/man/man6/spotlight.6
/usr/share/man/man6/sproingies.6
/usr/share/man/man6/squiral.6
/usr/share/man/man6/stairs.6
/usr/share/man/man6/starfish.6
/usr/share/man/man6/starwars.6
/usr/share/man/man6/stonerview.6
/usr/share/man/man6/strange.6
/usr/share/man/man6/substrate.6
/usr/share/man/man6/superquadrics.6
/usr/share/man/man6/surfaces.6
/usr/share/man/man6/swirl.6
/usr/share/man/man6/tangram.6
/usr/share/man/man6/tessellimage.6
/usr/share/man/man6/thornbird.6
/usr/share/man/man6/timetunnel.6
/usr/share/man/man6/topblock.6
/usr/share/man/man6/triangle.6
/usr/share/man/man6/tronbit.6
/usr/share/man/man6/truchet.6
/usr/share/man/man6/twang.6
/usr/share/man/man6/unicrud.6
/usr/share/man/man6/unknownpleasures.6
/usr/share/man/man6/vermiculate.6
/usr/share/man/man6/vfeedback.6
/usr/share/man/man6/vidwhacker.6
/usr/share/man/man6/vigilance.6
/usr/share/man/man6/voronoi.6
/usr/share/man/man6/wander.6
/usr/share/man/man6/webcollage.6
/usr/share/man/man6/whirlwindwarp.6
/usr/share/man/man6/winduprobot.6
/usr/share/man/man6/wormhole.6
/usr/share/man/man6/xanalogtv.6
/usr/share/man/man6/xflame.6
/usr/share/man/man6/xjack.6
/usr/share/man/man6/xlyap.6
/usr/share/man/man6/xmatrix.6
/usr/share/man/man6/xrayswarm.6
/usr/share/man/man6/xscreensaver-auth.6
/usr/share/man/man6/xscreensaver-command.6
/usr/share/man/man6/xscreensaver-getimage-file.6
/usr/share/man/man6/xscreensaver-getimage-video.6
/usr/share/man/man6/xscreensaver-getimage.6
/usr/share/man/man6/xscreensaver-gfx.6
/usr/share/man/man6/xscreensaver-gl-visual.6
/usr/share/man/man6/xscreensaver-systemd.6
/usr/share/man/man6/xscreensaver-text.6
/usr/share/man/man6/xspirograph.6
/usr/share/man/man6/zoom.6

%files locales -f xscreensaver.lang
%defattr(-,root,root,-)

