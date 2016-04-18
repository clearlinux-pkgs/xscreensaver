#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xscreensaver
Version  : 5.32
Release  : 8
URL      : http://www.jwz.org/xscreensaver/xscreensaver-5.32.tar.gz
Source0  : http://www.jwz.org/xscreensaver/xscreensaver-5.32.tar.gz
Summary  : A minimal installation of xscreensaver.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause
Requires: xscreensaver-bin
Requires: xscreensaver-locales
Requires: xscreensaver-doc
Requires: xscreensaver-data
BuildRequires : Linux-PAM-dev
BuildRequires : bc
BuildRequires : gdk-pixbuf-dev
BuildRequires : gettext
BuildRequires : glibc-staticdev
BuildRequires : gtk+-dev
BuildRequires : intltool
BuildRequires : libXext-dev
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xpm)
BuildRequires : pkgconfig(xrandr)
Patch1: 0001-Do-not-warn-about-invalid-PAM-directories.patch

%description
A modular screen saver and locker for the X Window System.
More than 200 display modes are included in this package.

%package bin
Summary: bin components for the xscreensaver package.
Group: Binaries
Requires: xscreensaver-data

%description bin
bin components for the xscreensaver package.


%package data
Summary: data components for the xscreensaver package.
Group: Data

%description data
data components for the xscreensaver package.


%package doc
Summary: doc components for the xscreensaver package.
Group: Documentation

%description doc
doc components for the xscreensaver package.


%package locales
Summary: locales components for the xscreensaver package.
Group: Default

%description locales
locales components for the xscreensaver package.


%prep
%setup -q -n xscreensaver-5.32
%patch1 -p1

%build
%configure --disable-static --without-pixbuf --with-xpm --without-gtk --with-pam --with-dpms-ext
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
%find_lang xscreensaver
## make_install_append content
install -m 00644 -D driver/xscreensaver.pam $RPM_BUILD_ROOT/usr/share/pam.d/xscreensaver
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/X11/app-defaults/XScreenSaver

%files bin
%defattr(-,root,root,-)
%exclude /usr/libexec/xscreensaver/abstractile
%exclude /usr/libexec/xscreensaver/anemone
%exclude /usr/libexec/xscreensaver/anemotaxis
%exclude /usr/libexec/xscreensaver/apollonian
%exclude /usr/libexec/xscreensaver/apple2
%exclude /usr/libexec/xscreensaver/attraction
%exclude /usr/libexec/xscreensaver/barcode
%exclude /usr/libexec/xscreensaver/binaryring
%exclude /usr/libexec/xscreensaver/blaster
%exclude /usr/libexec/xscreensaver/blitspin
%exclude /usr/libexec/xscreensaver/bouboule
%exclude /usr/libexec/xscreensaver/boxfit
%exclude /usr/libexec/xscreensaver/braid
%exclude /usr/libexec/xscreensaver/bsod
%exclude /usr/libexec/xscreensaver/bumps
%exclude /usr/libexec/xscreensaver/ccurve
%exclude /usr/libexec/xscreensaver/celtic
%exclude /usr/libexec/xscreensaver/cloudlife
%exclude /usr/libexec/xscreensaver/compass
%exclude /usr/libexec/xscreensaver/coral
%exclude /usr/libexec/xscreensaver/crystal
%exclude /usr/libexec/xscreensaver/cwaves
%exclude /usr/libexec/xscreensaver/cynosure
%exclude /usr/libexec/xscreensaver/decayscreen
%exclude /usr/libexec/xscreensaver/deco
%exclude /usr/libexec/xscreensaver/deluxe
%exclude /usr/libexec/xscreensaver/demon
%exclude /usr/libexec/xscreensaver/discrete
%exclude /usr/libexec/xscreensaver/distort
%exclude /usr/libexec/xscreensaver/drift
%exclude /usr/libexec/xscreensaver/epicycle
%exclude /usr/libexec/xscreensaver/eruption
%exclude /usr/libexec/xscreensaver/euler2d
%exclude /usr/libexec/xscreensaver/fadeplot
%exclude /usr/libexec/xscreensaver/fiberlamp
%exclude /usr/libexec/xscreensaver/fireworkx
%exclude /usr/libexec/xscreensaver/flame
%exclude /usr/libexec/xscreensaver/flow
%exclude /usr/libexec/xscreensaver/fluidballs
%exclude /usr/libexec/xscreensaver/fontglide
%exclude /usr/libexec/xscreensaver/fuzzyflakes
%exclude /usr/libexec/xscreensaver/galaxy
%exclude /usr/libexec/xscreensaver/goop
%exclude /usr/libexec/xscreensaver/grav
%exclude /usr/libexec/xscreensaver/greynetic
%exclude /usr/libexec/xscreensaver/halftone
%exclude /usr/libexec/xscreensaver/halo
%exclude /usr/libexec/xscreensaver/helix
%exclude /usr/libexec/xscreensaver/hexadrop
%exclude /usr/libexec/xscreensaver/hopalong
%exclude /usr/libexec/xscreensaver/ifs
%exclude /usr/libexec/xscreensaver/imsmap
%exclude /usr/libexec/xscreensaver/interaggregate
%exclude /usr/libexec/xscreensaver/interference
%exclude /usr/libexec/xscreensaver/intermomentary
%exclude /usr/libexec/xscreensaver/julia
%exclude /usr/libexec/xscreensaver/kaleidescope
%exclude /usr/libexec/xscreensaver/kumppa
%exclude /usr/libexec/xscreensaver/lcdscrub
%exclude /usr/libexec/xscreensaver/ljlatest
%exclude /usr/libexec/xscreensaver/loop
%exclude /usr/libexec/xscreensaver/m6502
%exclude /usr/libexec/xscreensaver/maze
%exclude /usr/libexec/xscreensaver/memscroller
%exclude /usr/libexec/xscreensaver/metaballs
%exclude /usr/libexec/xscreensaver/moire
%exclude /usr/libexec/xscreensaver/moire2
%exclude /usr/libexec/xscreensaver/mountain
%exclude /usr/libexec/xscreensaver/munch
%exclude /usr/libexec/xscreensaver/nerverot
%exclude /usr/libexec/xscreensaver/noseguy
%exclude /usr/libexec/xscreensaver/pacman
%exclude /usr/libexec/xscreensaver/pedal
%exclude /usr/libexec/xscreensaver/penetrate
%exclude /usr/libexec/xscreensaver/penrose
%exclude /usr/libexec/xscreensaver/petri
%exclude /usr/libexec/xscreensaver/phosphor
%exclude /usr/libexec/xscreensaver/piecewise
%exclude /usr/libexec/xscreensaver/polyominoes
%exclude /usr/libexec/xscreensaver/pong
%exclude /usr/libexec/xscreensaver/popsquares
%exclude /usr/libexec/xscreensaver/pyro
%exclude /usr/libexec/xscreensaver/qix
%exclude /usr/libexec/xscreensaver/rd-bomb
%exclude /usr/libexec/xscreensaver/ripples
%exclude /usr/libexec/xscreensaver/rocks
%exclude /usr/libexec/xscreensaver/rorschach
%exclude /usr/libexec/xscreensaver/rotzoomer
%exclude /usr/libexec/xscreensaver/shadebobs
%exclude /usr/libexec/xscreensaver/sierpinski
%exclude /usr/libexec/xscreensaver/slidescreen
%exclude /usr/libexec/xscreensaver/slip
%exclude /usr/libexec/xscreensaver/speedmine
%exclude /usr/libexec/xscreensaver/spotlight
%exclude /usr/libexec/xscreensaver/squiral
%exclude /usr/libexec/xscreensaver/starfish
%exclude /usr/libexec/xscreensaver/strange
%exclude /usr/libexec/xscreensaver/substrate
%exclude /usr/libexec/xscreensaver/swirl
%exclude /usr/libexec/xscreensaver/tessellimage
%exclude /usr/libexec/xscreensaver/thornbird
%exclude /usr/libexec/xscreensaver/triangle
%exclude /usr/libexec/xscreensaver/truchet
%exclude /usr/libexec/xscreensaver/twang
%exclude /usr/libexec/xscreensaver/vermiculate
%exclude /usr/libexec/xscreensaver/vidwhacker
%exclude /usr/libexec/xscreensaver/wander
%exclude /usr/libexec/xscreensaver/webcollage
%exclude /usr/libexec/xscreensaver/whirlwindwarp
%exclude /usr/libexec/xscreensaver/wormhole
%exclude /usr/libexec/xscreensaver/xanalogtv
%exclude /usr/libexec/xscreensaver/xflame
%exclude /usr/libexec/xscreensaver/xjack
%exclude /usr/libexec/xscreensaver/xlyap
%exclude /usr/libexec/xscreensaver/xmatrix
%exclude /usr/libexec/xscreensaver/xrayswarm
%exclude /usr/libexec/xscreensaver/xspirograph
%exclude /usr/libexec/xscreensaver/zoom
/usr/bin/xscreensaver
/usr/bin/xscreensaver-command
/usr/bin/xscreensaver-getimage
/usr/bin/xscreensaver-getimage-file
/usr/bin/xscreensaver-getimage-video
/usr/bin/xscreensaver-text

%files data
%defattr(-,root,root,-)
%exclude /usr/share/xscreensaver/config/abstractile.xml
%exclude /usr/share/xscreensaver/config/anemone.xml
%exclude /usr/share/xscreensaver/config/anemotaxis.xml
%exclude /usr/share/xscreensaver/config/apollonian.xml
%exclude /usr/share/xscreensaver/config/apple2.xml
%exclude /usr/share/xscreensaver/config/attraction.xml
%exclude /usr/share/xscreensaver/config/barcode.xml
%exclude /usr/share/xscreensaver/config/binaryring.xml
%exclude /usr/share/xscreensaver/config/blaster.xml
%exclude /usr/share/xscreensaver/config/blitspin.xml
%exclude /usr/share/xscreensaver/config/bouboule.xml
%exclude /usr/share/xscreensaver/config/boxfit.xml
%exclude /usr/share/xscreensaver/config/braid.xml
%exclude /usr/share/xscreensaver/config/bsod.xml
%exclude /usr/share/xscreensaver/config/bumps.xml
%exclude /usr/share/xscreensaver/config/ccurve.xml
%exclude /usr/share/xscreensaver/config/celtic.xml
%exclude /usr/share/xscreensaver/config/cloudlife.xml
%exclude /usr/share/xscreensaver/config/compass.xml
%exclude /usr/share/xscreensaver/config/coral.xml
%exclude /usr/share/xscreensaver/config/crystal.xml
%exclude /usr/share/xscreensaver/config/cwaves.xml
%exclude /usr/share/xscreensaver/config/cynosure.xml
%exclude /usr/share/xscreensaver/config/decayscreen.xml
%exclude /usr/share/xscreensaver/config/deco.xml
%exclude /usr/share/xscreensaver/config/deluxe.xml
%exclude /usr/share/xscreensaver/config/demon.xml
%exclude /usr/share/xscreensaver/config/discrete.xml
%exclude /usr/share/xscreensaver/config/distort.xml
%exclude /usr/share/xscreensaver/config/drift.xml
%exclude /usr/share/xscreensaver/config/epicycle.xml
%exclude /usr/share/xscreensaver/config/eruption.xml
%exclude /usr/share/xscreensaver/config/euler2d.xml
%exclude /usr/share/xscreensaver/config/fadeplot.xml
%exclude /usr/share/xscreensaver/config/fiberlamp.xml
%exclude /usr/share/xscreensaver/config/fireworkx.xml
%exclude /usr/share/xscreensaver/config/flame.xml
%exclude /usr/share/xscreensaver/config/flow.xml
%exclude /usr/share/xscreensaver/config/fluidballs.xml
%exclude /usr/share/xscreensaver/config/fontglide.xml
%exclude /usr/share/xscreensaver/config/fuzzyflakes.xml
%exclude /usr/share/xscreensaver/config/galaxy.xml
%exclude /usr/share/xscreensaver/config/goop.xml
%exclude /usr/share/xscreensaver/config/grav.xml
%exclude /usr/share/xscreensaver/config/greynetic.xml
%exclude /usr/share/xscreensaver/config/halftone.xml
%exclude /usr/share/xscreensaver/config/halo.xml
%exclude /usr/share/xscreensaver/config/helix.xml
%exclude /usr/share/xscreensaver/config/hexadrop.xml
%exclude /usr/share/xscreensaver/config/hopalong.xml
%exclude /usr/share/xscreensaver/config/ifs.xml
%exclude /usr/share/xscreensaver/config/imsmap.xml
%exclude /usr/share/xscreensaver/config/interaggregate.xml
%exclude /usr/share/xscreensaver/config/interference.xml
%exclude /usr/share/xscreensaver/config/intermomentary.xml
%exclude /usr/share/xscreensaver/config/julia.xml
%exclude /usr/share/xscreensaver/config/kaleidescope.xml
%exclude /usr/share/xscreensaver/config/kumppa.xml
%exclude /usr/share/xscreensaver/config/lcdscrub.xml
%exclude /usr/share/xscreensaver/config/loop.xml
%exclude /usr/share/xscreensaver/config/m6502.xml
%exclude /usr/share/xscreensaver/config/maze.xml
%exclude /usr/share/xscreensaver/config/memscroller.xml
%exclude /usr/share/xscreensaver/config/metaballs.xml
%exclude /usr/share/xscreensaver/config/moire.xml
%exclude /usr/share/xscreensaver/config/moire2.xml
%exclude /usr/share/xscreensaver/config/mountain.xml
%exclude /usr/share/xscreensaver/config/munch.xml
%exclude /usr/share/xscreensaver/config/nerverot.xml
%exclude /usr/share/xscreensaver/config/noseguy.xml
%exclude /usr/share/xscreensaver/config/pacman.xml
%exclude /usr/share/xscreensaver/config/pedal.xml
%exclude /usr/share/xscreensaver/config/penetrate.xml
%exclude /usr/share/xscreensaver/config/penrose.xml
%exclude /usr/share/xscreensaver/config/petri.xml
%exclude /usr/share/xscreensaver/config/phosphor.xml
%exclude /usr/share/xscreensaver/config/piecewise.xml
%exclude /usr/share/xscreensaver/config/polyominoes.xml
%exclude /usr/share/xscreensaver/config/pong.xml
%exclude /usr/share/xscreensaver/config/popsquares.xml
%exclude /usr/share/xscreensaver/config/pyro.xml
%exclude /usr/share/xscreensaver/config/qix.xml
%exclude /usr/share/xscreensaver/config/rd-bomb.xml
%exclude /usr/share/xscreensaver/config/ripples.xml
%exclude /usr/share/xscreensaver/config/rocks.xml
%exclude /usr/share/xscreensaver/config/rorschach.xml
%exclude /usr/share/xscreensaver/config/rotzoomer.xml
%exclude /usr/share/xscreensaver/config/shadebobs.xml
%exclude /usr/share/xscreensaver/config/sierpinski.xml
%exclude /usr/share/xscreensaver/config/slidescreen.xml
%exclude /usr/share/xscreensaver/config/slip.xml
%exclude /usr/share/xscreensaver/config/speedmine.xml
%exclude /usr/share/xscreensaver/config/spotlight.xml
%exclude /usr/share/xscreensaver/config/squiral.xml
%exclude /usr/share/xscreensaver/config/starfish.xml
%exclude /usr/share/xscreensaver/config/strange.xml
%exclude /usr/share/xscreensaver/config/substrate.xml
%exclude /usr/share/xscreensaver/config/swirl.xml
%exclude /usr/share/xscreensaver/config/tessellimage.xml
%exclude /usr/share/xscreensaver/config/thornbird.xml
%exclude /usr/share/xscreensaver/config/triangle.xml
%exclude /usr/share/xscreensaver/config/truchet.xml
%exclude /usr/share/xscreensaver/config/twang.xml
%exclude /usr/share/xscreensaver/config/vermiculate.xml
%exclude /usr/share/xscreensaver/config/vidwhacker.xml
%exclude /usr/share/xscreensaver/config/wander.xml
%exclude /usr/share/xscreensaver/config/webcollage.xml
%exclude /usr/share/xscreensaver/config/whirlwindwarp.xml
%exclude /usr/share/xscreensaver/config/wormhole.xml
%exclude /usr/share/xscreensaver/config/xanalogtv.xml
%exclude /usr/share/xscreensaver/config/xflame.xml
%exclude /usr/share/xscreensaver/config/xjack.xml
%exclude /usr/share/xscreensaver/config/xlyap.xml
%exclude /usr/share/xscreensaver/config/xmatrix.xml
%exclude /usr/share/xscreensaver/config/xrayswarm.xml
%exclude /usr/share/xscreensaver/config/xspirograph.xml
%exclude /usr/share/xscreensaver/config/zoom.xml
/usr/share/pam.d/xscreensaver
/usr/share/xscreensaver/config/README

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man6/*

%files locales -f xscreensaver.lang 
%defattr(-,root,root,-)

