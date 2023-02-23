# Maintainer: Gaetan Bisson <bisson@archlinux.org>
# Contributor: dorphell <dorphell@archlinux.org>

pkgname=w3m
_gitcommit=fee038d7180e3d69276f55167a0d1da5233bc9c2
_pkgver=0.5.3.git20230121-1
pkgver=${_pkgver/-/_}
pkgrel=1
pkgdesc='Text-based Web browser as well as pager'
url='https://salsa.debian.org/debian/w3m'
license=('custom')
arch=('x86_64')
makedepends=('git' 'imlib2')
optdepends=('imlib2: for graphics support')
depends=('openssl' 'gc' 'ncurses' 'gpm')
source=("git+https://salsa.debian.org/debian/w3m.git#commit=${_gitcommit}")
sha256sums=('SKIP')

# There's also the maintainer's github repo, usually in sync with Debian's:
# https://github.com/tats/w3m

build() {
  cd ${pkgname}

  # Remove all baked in keybindings except for escape mappings
  for i in $(cat keybind.c | grep -E -v '\*|#|=|;|^    //' \
                           | sed -e 's|\t//.*||g' \
                                 -e 's/, /\n/g' \
                                 -e 's/^ *//' \
                                 -e 's/,/\n/g' \
                           | sort -u \
                           | sort -r \
                           | grep -E -v 'escbmap|escmap'); do
    sed -i "s/ $i/ nulcmd/g" keybind.c
  done

  # force scrolling via cursor on last line to be one line at a time,
  #   NOT a half page
  sed -i -e 's/buf->topLine = lineSkip(buf, buf->topLine, n, FALSE);/buf->topLine = lineSkip(buf, buf->topLine, 1, FALSE);/' \
         -e 's/buf->topLine = lineSkip(buf, buf->topLine, -n, FALSE);/buf->topLine = lineSkip(buf, buf->topLine, -1, FALSE);/' display.c

  ./configure \
    --prefix=/usr \
    --libexecdir=/usr/lib \
    --with-termlib=ncurses \
    --disable-w3mmailer \
    #--enable-image=x11,fb \
    #--with-imagelib=imlib2 \

  make
}

package() {
  cd ${pkgname}
  make DESTDIR="${pkgdir}" install

  install -d "${pkgdir}"/usr/share/{doc,licenses}/w3m
  install -m644 doc/* "${pkgdir}/usr/share/doc/w3m"
  ln -s ../../doc/w3m/README "${pkgdir}/usr/share/licenses/w3m"
}
