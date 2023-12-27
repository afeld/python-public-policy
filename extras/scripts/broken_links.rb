# frozen_string_literal: true

require "html-proofer"

options = {
  only_4xx: true,
  ignore_files: [
    "_build/html/_static/webpack-macros.html",
    "_build/html/_static/sbt-webpack-macros.html",
    # don't want to bother fixing links in example projects
    %r{^_build/html/final_project/}
  ],
  ignore_urls: [
    %r{^_static/images/logo_},
    %r{^https://vergil\.registrar\.columbia\.edu/#},
    # gives a 400
    %r{^https://twitter\.com/},
    # give 403s for some reason
    %r{^https://support\.zoom\.us/},
    %r{^https://support\.socrata\.com/},
    %r{^https://(www\.)?kaggle\.com/},
    "https://hobbylark.com/party-games/How-to-Make-Your-Own-Mad-Libs"
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
