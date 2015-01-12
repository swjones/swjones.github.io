# swjones.github.io
Website of Samuel Jones

Notes for using Jekyll and GitHub pages:

* Make new jekyll site: `jekyll new <name_of_dir_for_site>`
* To build and serve locally: `bundle exec jekyll serve` (add `--watch` to
watch for updates while developing)
* No need to add or commit the local `_site` directory, which contains
the static site after jekyll has generated it. GitHub Pages will either
not use this directory or will anyway overwrite it when it generates
the site on the server side.
