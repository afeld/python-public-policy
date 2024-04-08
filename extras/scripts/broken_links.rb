# frozen_string_literal: true

require "html-proofer"

options = {
  only_4xx: true,
  ignore_status_codes: [400, 401, 403, 405, 429],
  ignore_files: [
    "_build/html/_static/webpack-macros.html",
    "_build/html/_static/sbt-webpack-macros.html",
    # don't want to bother fixing links in example projects
    %r{^_build/html/final_project/}
  ],
  ignore_urls: [
    # https://github.com/executablebooks/sphinx-book-theme/pull/831
    %r{_static/images/logo_},
  ],
  swap_urls: {
    # ignore PDF page hash
    # https://github.com/gjtorikian/html-proofer/issues/663#issuecomment-989274727
    /(?<=\.pdf)#.*$/ => "",
    # make absolute links relative
    %r{^https://python-public-policy\.afeld\.me/en/\w+} => ""
  }
}
HTMLProofer.check_directory("_build/html", options).run
