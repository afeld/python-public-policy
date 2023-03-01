# frozen_string_literal: true

require 'html-proofer'

options = {
  ignore_missing_alt: true,
  allow_missing_href: true,
  check_external_hash: false,
  only_4xx: true,
  ignore_files: ['_build/html/_static/webpack-macros.html', '_build/html/_static/sbt-webpack-macros.html'],
  # make absolute links relative
  swap_urls: { %r{^https://python-public-policy\.afeld\.me/en/\w+} => '' }
}
HTMLProofer.check_directory('_build/html', options).run
