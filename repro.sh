#! /usr/bin/bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

pkgs=(ffmpeg fontconfig freetype2 harfbuzz)
ns="tamas/repro"
export CONAN_USER_HOME=$DIR/conan_cache

rm -rf $CONAN_USER_HOME

for pkg in "${pkgs[@]}"; do
  pushd $pkg
  conan export . $ns
  popd
done

cd ffmpeg
conan create . $ns --build missing
