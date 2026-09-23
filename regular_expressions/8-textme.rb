#!/usr/bin/env ruby

log_line = ARGV[0]

if log_line =~ /\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\]/
  puts "#{$1},#{$2},#{$3}"
end
