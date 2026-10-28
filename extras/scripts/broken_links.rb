# frozen_string_literal: true

require "html-proofer"

options = {
  only_4xx: true,
  ignore_status_codes: [400, 401, 403, 405, 429],
  ignore_files: [
    # don't want to bother fixing links in example projects
    %r{^_build/html/final_project/}
  ],
  # applied in order
  swap_urls: {
    # make absolute links relative, first so that the hash handling below applies to them
    %r{^https://python-public-policy\.afeld\.me/en/\w+} => "",
    # ignore PDF page hash
    # https://github.com/gjtorikian/html-proofer/issues/663#issuecomment-989274727
    /(?<=\.pdf)#.*$/ => "",
    # Redirect files generated from old JB1 .html URLs don't contain anchors.
    # Strip hashes so linkcheck validates file existence without false anchor failures.
    /(?<=\.html)#.*$/ => "",
    # Folder-style pages (/syllabus/) coexist with redirect files (syllabus.html), which html-proofer's assume_extension picks first. Point at the real page so anchors get checked.
    %r{\A((?:/[^/.#?]+)+)/?(?=#|\z)} => "\\1/index.html"
  }
}
HTMLProofer.check_directory("_build/html", options).run
