#!/usr/bin/env ruby

# Define variables
var1 = "/vault/index.json"

# puts "https://releases.hashicorp.com#{var1}"

# Load modules
require "http"

api = HTTP.persistent("https://releases.hashicorp.com")

response = api.get("#{var1}")

if response.status.success?

# Success, the response attributes are available here.

out = response.parse["versions"]
out.count do |item|
	item.each do |key|
		p key
	end
#	p item
end
else

# Error, inspect the `errors` key for more information.

p response.code, response.body

end


