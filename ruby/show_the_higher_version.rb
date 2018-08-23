#!/usr/bin/env ruby

# Define variables
var1 = "vault/index.json"
puts "https://releases.hashicorp.com/#{var1}"

# Load modules
require "http"

api = HTTP.persistent("https://releases.hashicorp.com")

response = api.get("/#{var1}")

max_ver = "0.0.0"

if response.status.success?
    # Success, the response attributes are available here.
    out = response.parse["versions"]
    out.count do |item|
        item.each do |key|
            current_ver = key["version"] unless key["version"].nil?

            # if current_ver > max_ver then we store current_ver
            if  Gem::Version.new(max_ver) < Gem::Version.new(current_ver)
                max_ver = current_ver unless ( current_ver.include? "rc" or current_ver.include? "beta" )
            end

        end
    end

    puts max_ver
else
    # Error, inspect the `errors` key for more information.
    p response.code, response.body
end
