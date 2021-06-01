#!/usr/bin/env sh
set -eu

echo '# Changelog'
echo

tag=
# we skip v0.0.0 tags, so these can be used on branches without updating release notes
git tag -l 'v*' | grep -v 0.0.0 | sort -rV | while read last; do
  if [ "$tag" != "" ]; then
    echo "## $tag ($(git log $tag -n1 --format=%as))"
    echo
    git_log='git --no-pager log --no-merges --invert-grep --grep=\(build\|chore\|ci\|docs\|test\):'
	  $git_log --format=' * [%h](https://github.com/argoproj/argo-workflows/commit/%H) %s' $last..$tag
	  echo
	  echo "### Contributors"
	  echo
	  $git_log --format=' * %an'  $last..$tag | sort -u
	  echo
  fi
  tag=$last
done